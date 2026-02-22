🚀  Pipeline Builder

A drag-and-drop visual pipeline builder built using React Flow (frontend) and FastAPI (backend).
This project was developed as part of the VectorShift Frontend Technical Assessment.

✨ Features

🎨 Modern dark-theme UI

🧩 Reusable BaseNode abstraction

➕ 9 draggable node types

🔗 Visual edge connections between nodes

🧠 Dynamic Text node with {{variables}}

📏 Auto-resizing text area

📡 Frontend → Backend pipeline analysis

✅ DAG (cycle) detection using Kahn’s Algorithm

🗺️ MiniMap and smooth canvas navigation

🏗️ Tech Stack
Frontend

React

React Flow

JavaScript

CSS

Backend

FastAPI

Uvicorn

Python

📂 Project Structure
.
├── frontend/
│   ├── src/
│   │   ├── nodes/
│   │   │   ├── BaseNode.js
│   │   │   ├── inputNode.js
│   │   │   ├── outputNode.js
│   │   │   ├── llmNode.js
│   │   │   ├── textNode.js
│   │   │   └── newNodes.js
│   │   ├── ui.js
│   │   ├── toolbar.js
│   │   └── submit.js
│   └── package.json
│
└── backend/
    └── main.py
⚙️ Prerequisites

Make sure you have installed:

✅ Node.js (v16+ recommended)

✅ npm

✅ Python (3.9+ recommended)

✅ pip

Check versions:

node -v
npm -v
python3 --version
🚀 How to Run the Project

⚠️ IMPORTANT: You must run frontend and backend in parallel.

🔹 Step 1 — Clone the Repository
git clone https://github.com/YOUR_USERNAME/pipeline-builder.git
cd pipeline-builder
🔹 Step 2 — Setup Frontend

Open terminal:

cd frontend
npm install
npm start

✅ Frontend runs at:

http://localhost:3000
🔹 Step 3 — Setup Backend

Open a new terminal tab/window:

cd backend
pip install fastapi uvicorn
uvicorn main:app --reload

✅ Backend runs at:

http://127.0.0.1:8000
🧪 How to Test the App

Open browser → http://localhost:3000

Drag nodes from toolbar

Connect nodes with edges

Add a Text node

Type:

Hello {{name}} how are you {{age}}

✅ New input handles should appear automatically.

Click ▶ Submit Pipeline

You should see:

Number of nodes

Number of edges

Whether the graph is a DAG

🧠 Key Implementation Details
✅ Node Abstraction

Implemented reusable BaseNode

Eliminated duplicate node boilerplate

New nodes can be created in <20 lines

✅ Dynamic Text Node

Auto-resizes using scrollHeight

Extracts variables using regex:

\{\{([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}

Uses useUpdateNodeInternals() to refresh handles

✅ DAG Detection

Backend uses Kahn’s Algorithm (BFS-based topological sort):

Counts in-degrees

Processes zero-in-degree nodes

Detects cycles reliably
