from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from collections import defaultdict, deque

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pipeline(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]


def check_is_dag(nodes: list, edges: list) -> bool:
    """
    Returns True if the graph formed by nodes+edges is a Directed Acyclic Graph.
    Uses Kahn's algorithm:
      1. Count how many edges point INTO each node (in-degree).
      2. Start from nodes with in-degree 0 (no incoming edges).
      3. Remove those nodes and reduce in-degrees of their neighbours.
      4. If we process ALL nodes, there is no cycle → it IS a DAG.
      5. If any nodes are left over, a cycle exists → NOT a DAG.
    """
    node_ids = {n["id"] for n in nodes}
    in_degree = {nid: 0 for nid in node_ids}
    graph     = defaultdict(list)

    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if src in node_ids and tgt in node_ids:
            graph[src].append(tgt)
            in_degree[tgt] += 1

    queue   = deque([nid for nid, deg in in_degree.items() if deg == 0])
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    return visited == len(node_ids)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.post("/pipelines/parse")
def parse_pipeline(pipeline: Pipeline):
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)
    is_dag    = check_is_dag(pipeline.nodes, pipeline.edges)
    return {"num_nodes": num_nodes, "num_edges": num_edges, "is_dag": is_dag}

