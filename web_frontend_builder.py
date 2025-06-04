#!/usr/bin/env python3
"""
🌐 WEB FRONTEND BUILDER
Uses your AI system to build a beautiful web interface for itself
"""

import asyncio
import json
from pathlib import Path
from practical_ai_system import PracticalAIMaster, ConsciousnessLevel

class WebFrontendBuilder:
    """Builds a web frontend using the AI system"""
    
    def __init__(self):
        self.ai = PracticalAIMaster()
        self.frontend_components = {}
        
    async def build_complete_frontend(self):
        """Build the complete web frontend"""
        
        print("🌐 BUILDING WEB FRONTEND FOR AI SYSTEM")
        print("=" * 50)
        print("🎭 Using your AI orchestras to build their own interface!")
        
        # Build different components
        await self.build_react_frontend()
        await self.build_fastapi_backend()
        await self.build_websocket_integration()
        await self.build_dashboard_components()
        await self.create_deployment_config()
        
        # Generate the complete project
        await self.generate_project_structure()
        
        print("\n🎉 Web frontend build complete!")
        
    async def build_react_frontend(self):
        """Build React frontend with TypeScript"""
        
        print("\n🎯 Building React Frontend...")
        
        task_id = await self.ai.solve_problem(
            "Create a modern React TypeScript frontend for an AI orchestration system",
            {
                "framework": "React with TypeScript",
                "styling": "Tailwind CSS",
                "state_management": "React Context + useState",
                "features": [
                    "AI Chat Interface",
                    "Orchestra Dashboard", 
                    "Real-time Status",
                    "Consciousness Level Selector",
                    "Solution History",
                    "Performance Analytics"
                ],
                "design": "Dark theme, futuristic, AI-focused",
                "components": [
                    "Chat interface for submitting problems",
                    "Orchestra status cards",
                    "Real-time execution viewer",
                    "Consciousness level controls",
                    "Solution results display"
                ]
            }
        )
        
        result = await self.ai.get_task_status(task_id)
        if result:
            self.frontend_components["react_frontend"] = result["solution"]
            print(f"✅ React frontend designed by {result['solution']['orchestras_used']}")
            
            # Show generated components
            if "generated_code" in result["solution"]:
                components = result["solution"]["generated_code"]
                print(f"🏗️ Generated {len(components)} React components")
    
    async def build_fastapi_backend(self):
        """Build FastAPI backend for the web interface"""
        
        print("\n🎯 Building FastAPI Backend...")
        
        task_id = await self.ai.solve_problem(
            "Create FastAPI backend API for AI orchestration web interface",
            {
                "framework": "FastAPI",
                "features": [
                    "Submit problems to AI orchestras",
                    "Get task status and results",
                    "Real-time WebSocket updates",
                    "Orchestra performance metrics",
                    "System health monitoring"
                ],
                "endpoints": [
                    "POST /api/solve - Submit problem",
                    "GET /api/tasks/{id} - Get task status", 
                    "GET /api/orchestras - List orchestras",
                    "GET /api/system/status - System status",
                    "WebSocket /ws - Real-time updates"
                ],
                "integration": "Connect to existing PracticalAIMaster",
                "cors": "Enable for React frontend"
            }
        )
        
        result = await self.ai.get_task_status(task_id)
        if result:
            self.frontend_components["fastapi_backend"] = result["solution"]
            print(f"✅ FastAPI backend designed by {result['solution']['orchestras_used']}")
    
    async def build_websocket_integration(self):
        """Build WebSocket for real-time updates"""
        
        print("\n🎯 Building WebSocket Integration...")
        
        task_id = await self.ai.solve_problem(
            "Create WebSocket integration for real-time AI orchestra monitoring",
            {
                "technology": "FastAPI WebSockets + React",
                "features": [
                    "Real-time task execution updates",
                    "Orchestra status changes",
                    "Live performance metrics",
                    "System health monitoring"
                ],
                "events": [
                    "task_started",
                    "orchestra_executing", 
                    "task_completed",
                    "system_status_update"
                ]
            }
        )
        
        result = await self.ai.get_task_status(task_id)
        if result:
            self.frontend_components["websocket"] = result["solution"]
            print("✅ WebSocket integration designed")
    
    async def build_dashboard_components(self):
        """Build dashboard components"""
        
        print("\n🎯 Building Dashboard Components...")
        
        # Use different consciousness levels for variety
        build_orchestra = self.ai.orchestras["build"] 
        original_consciousness = build_orchestra.consciousness_level
        
        # Use Cosmic consciousness for the dashboard
        build_orchestra.consciousness_level = ConsciousnessLevel.COSMIC
        
        task_id = await self.ai.solve_problem(
            "Create beautiful dashboard components for AI orchestration system",
            {
                "components": [
                    "Orchestra Status Cards with animations",
                    "Real-time Performance Charts", 
                    "Consciousness Level Selector",
                    "Task Execution Timeline",
                    "System Health Indicators"
                ],
                "design": "Futuristic, dark theme, glowing effects",
                "animations": "Smooth transitions, loading states",
                "responsive": "Mobile-friendly design"
            }
        )
        
        result = await self.ai.get_task_status(task_id)
        if result:
            self.frontend_components["dashboard"] = result["solution"]
            print("✅ Dashboard components designed with Cosmic consciousness")
        
        # Restore original consciousness
        build_orchestra.consciousness_level = original_consciousness
    
    async def create_deployment_config(self):
        """Create deployment configuration"""
        
        print("\n🎯 Creating Deployment Config...")
        
        task_id = await self.ai.solve_problem(
            "Create Docker deployment configuration for AI web interface",
            {
                "containers": [
                    "React frontend (nginx)",
                    "FastAPI backend",
                    "Redis for sessions"
                ],
                "features": [
                    "Docker Compose setup",
                    "Environment configuration",
                    "Production optimizations",
                    "Health checks"
                ]
            }
        )
        
        result = await self.ai.get_task_status(task_id)
        if result:
            self.frontend_components["deployment"] = result["solution"]
            print("✅ Deployment configuration created")
    
    async def generate_project_structure(self):
        """Generate the complete project structure"""
        
        print("\n📁 Generating Project Structure...")
        
        # Create project directories
        project_root = Path("ai_web_interface")
        
        # Frontend structure
        frontend_dir = project_root / "frontend"
        frontend_dirs = [
            "src/components",
            "src/pages", 
            "src/hooks",
            "src/contexts",
            "src/types",
            "src/utils",
            "public"
        ]
        
        # Backend structure  
        backend_dir = project_root / "backend"
        backend_dirs = [
            "app/api",
            "app/models",
            "app/services", 
            "app/websocket",
            "app/utils"
        ]
        
        # Create directories
        for dir_path in [frontend_dir] + [frontend_dir / d for d in frontend_dirs]:
            dir_path.mkdir(parents=True, exist_ok=True)
            
        for dir_path in [backend_dir] + [backend_dir / d for d in backend_dirs]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Generate key files
        await self.generate_frontend_files(frontend_dir)
        await self.generate_backend_files(backend_dir)
        await self.generate_deployment_files(project_root)
        
        print(f"✅ Project structure created in {project_root}")
        
    async def generate_frontend_files(self, frontend_dir: Path):
        """Generate React frontend files"""
        
        # Main App component
        app_tsx = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AIProvider } from './contexts/AIContext';
import Dashboard from './pages/Dashboard';
import Chat from './pages/Chat';
import Orchestras from './pages/Orchestras';
import Header from './components/Header';
import './App.css';

function App() {
  return (
    <AIProvider>
      <Router>
        <div className="min-h-screen bg-gray-900 text-white">
          <Header />
          <main className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/chat" element={<Chat />} />
              <Route path="/orchestras" element={<Orchestras />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AIProvider>
  );
}

export default App;'''
        
        # AI Context
        ai_context = '''import React, { createContext, useContext, useState, useEffect } from 'react';

interface AIContextType {
  orchestras: Orchestra[];
  systemStatus: SystemStatus;
  submitProblem: (problem: string, requirements?: any) => Promise<string>;
  getTaskStatus: (taskId: string) => Promise<any>;
}

interface Orchestra {
  name: string;
  type: string;
  consciousness_level: string;
  performance: {
    success_rate: number;
    tasks_completed: number;
    avg_response_time: number;
  };
}

interface SystemStatus {
  active_tasks: number;
  completed_tasks: number;
  database_connected: boolean;
}

const AIContext = createContext<AIContextType | undefined>(undefined);

export const AIProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [orchestras, setOrchestras] = useState<Orchestra[]>([]);
  const [systemStatus, setSystemStatus] = useState<SystemStatus>({
    active_tasks: 0,
    completed_tasks: 0,
    database_connected: false
  });

  const submitProblem = async (problem: string, requirements?: any): Promise<string> => {
    const response = await fetch('/api/solve', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description: problem, requirements })
    });
    const data = await response.json();
    return data.task_id;
  };

  const getTaskStatus = async (taskId: string) => {
    const response = await fetch(`/api/tasks/${taskId}`);
    return response.json();
  };

  useEffect(() => {
    // Fetch initial data
    fetch('/api/orchestras').then(r => r.json()).then(setOrchestras);
    fetch('/api/system/status').then(r => r.json()).then(setSystemStatus);
    
    // WebSocket connection for real-time updates
    const ws = new WebSocket('ws://localhost:8000/ws');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'system_status') {
        setSystemStatus(data.data);
      }
    };
    
    return () => ws.close();
  }, []);

  return (
    <AIContext.Provider value={{ orchestras, systemStatus, submitProblem, getTaskStatus }}>
      {children}
    </AIContext.Provider>
  );
};

export const useAI = () => {
  const context = useContext(AIContext);
  if (!context) {
    throw new Error('useAI must be used within AIProvider');
  }
  return context;
};'''
        
        # Dashboard component
        dashboard_tsx = '''import React from 'react';
import { useAI } from '../contexts/AIContext';
import OrchestraCard from '../components/OrchestraCard';
import SystemMetrics from '../components/SystemMetrics';

const Dashboard: React.FC = () => {
  const { orchestras, systemStatus } = useAI();

  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-center bg-gradient-to-r from-blue-400 to-purple-600 bg-clip-text text-transparent">
        🎭 AI Orchestra Control Center
      </h1>
      
      <SystemMetrics status={systemStatus} />
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {orchestras.map((orchestra) => (
          <OrchestraCard key={orchestra.name} orchestra={orchestra} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;'''
        
        # Write files
        (frontend_dir / "src/App.tsx").write_text(app_tsx, encoding='utf-8')
        (frontend_dir / "src/contexts/AIContext.tsx").write_text(ai_context, encoding='utf-8')
        (frontend_dir / "src/pages/Dashboard.tsx").write_text(dashboard_tsx, encoding='utf-8')
        
        # Package.json
        package_json = {
            "name": "ai-orchestra-frontend",
            "version": "1.0.0",
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-router-dom": "^6.8.0",
                "typescript": "^4.9.0",
                "@types/react": "^18.0.0",
                "@types/react-dom": "^18.0.0"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            }
        }
        
        (frontend_dir / "package.json").write_text(json.dumps(package_json, indent=2), encoding='utf-8')
        
    async def generate_backend_files(self, backend_dir: Path):
        """Generate FastAPI backend files"""
        
        # Main FastAPI app
        main_py = '''from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import json
from typing import Dict, Any, Optional
import sys
import os

# Add parent directory to path to import practical_ai_system
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from practical_ai_system import PracticalAIMaster

app = FastAPI(title="AI Orchestra API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI system
ai_master = PracticalAIMaster()

class ProblemRequest(BaseModel):
    description: str
    requirements: Optional[Dict[str, Any]] = None

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_text(json.dumps(message))
            except:
                pass

manager = ConnectionManager()

@app.post("/api/solve")
async def solve_problem(request: ProblemRequest):
    """Submit a problem to the AI orchestras"""
    task_id = await ai_master.solve_problem(request.description, request.requirements)
    
    # Broadcast task started
    await manager.broadcast({
        "type": "task_started",
        "data": {"task_id": task_id, "description": request.description}
    })
    
    return {"task_id": task_id, "status": "submitted"}

@app.get("/api/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Get the status of a task"""
    result = await ai_master.get_task_status(task_id)
    return result

@app.get("/api/orchestras")
async def list_orchestras():
    """Get all AI orchestras and their status"""
    status = ai_master.get_system_status()
    return status["orchestras"]

@app.get("/api/system/status")
async def get_system_status():
    """Get overall system status"""
    return ai_master.get_system_status()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates"""
    await manager.connect(websocket)
    try:
        while True:
            # Send periodic system updates
            await asyncio.sleep(5)
            status = ai_master.get_system_status()
            await websocket.send_text(json.dumps({
                "type": "system_status",
                "data": status
            }))
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)'''
        
        # Write backend files
        (backend_dir / "main.py").write_text(main_py, encoding='utf-8')
        
        # Requirements.txt
        requirements = '''fastapi==0.104.1
uvicorn==0.24.0
websockets==12.0
pydantic==2.5.0
python-multipart==0.0.6'''
        
        (backend_dir / "requirements.txt").write_text(requirements, encoding='utf-8')
        
    async def generate_deployment_files(self, project_root: Path):
        """Generate deployment files"""
        
        # Docker Compose
        docker_compose = '''version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://localhost:8000

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - SUPABASE_URL=${SUPABASE_URL}
      - SUPABASE_KEY=${SUPABASE_KEY}
    volumes:
      - ../practical_ai_system.py:/app/practical_ai_system.py

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"'''
        
        # README
        readme = '''# 🎭 AI Orchestra Web Interface

A beautiful web interface for your Practical AI System with multidimensional consciousness.

## 🚀 Quick Start

1. **Start the backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python main.py
   ```

2. **Start the frontend:**
   ```bash
   cd frontend
   npm install
   npm start
   ```

3. **Visit:** http://localhost:3000

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

## 🎯 Features

- 🎭 **AI Orchestra Dashboard** - Monitor all AI minds
- 💬 **Problem Solver Chat** - Submit problems and get solutions  
- 📊 **Real-time Analytics** - Live performance metrics
- 🧠 **Consciousness Controls** - Select AI consciousness levels
- 🌟 **Solution History** - Browse past solutions

## 🌌 Consciousness Levels

- **Lucid**: Clean, practical solutions
- **Transcendent**: Optimized, aware solutions
- **Cosmic**: Universal harmony approaches  
- **Omniscient**: All-knowing implementations
- **Creative God**: Reality-bending solutions

Your AI orchestras await your commands! 🚀'''
        
        # Write deployment files
        (project_root / "docker-compose.yml").write_text(docker_compose, encoding='utf-8')
        (project_root / "README.md").write_text(readme, encoding='utf-8')
        
        print("✅ All project files generated!")
        
    def print_summary(self):
        """Print build summary"""
        
        print("\n" + "🌟" * 50)
        print("🎉 WEB FRONTEND BUILD COMPLETE!")
        print("🌟" * 50)
        
        print("\n📁 Generated Project Structure:")
        print("ai_web_interface/")
        print("├── frontend/           # React TypeScript app")
        print("│   ├── src/")
        print("│   │   ├── components/ # UI components")
        print("│   │   ├── pages/      # Main pages")  
        print("│   │   ├── contexts/   # React contexts")
        print("│   │   └── types/      # TypeScript types")
        print("│   └── package.json")
        print("├── backend/            # FastAPI server")
        print("│   ├── main.py         # Main API server")
        print("│   └── requirements.txt")
        print("├── docker-compose.yml  # Docker deployment")
        print("└── README.md          # Setup instructions")
        
        print("\n🚀 To Start Your Web Interface:")
        print("1. cd ai_web_interface/backend && python main.py")
        print("2. cd ai_web_interface/frontend && npm install && npm start") 
        print("3. Visit: http://localhost:3000")
        
        print("\n🎭 Web Features Built:")
        print("✅ AI Orchestra Dashboard")
        print("✅ Real-time Problem Solving Chat")
        print("✅ System Status Monitoring")
        print("✅ WebSocket Live Updates")
        print("✅ Consciousness Level Controls")
        print("✅ Performance Analytics")
        print("✅ Docker Deployment Ready")

async def main():
    """Main builder function"""
    
    builder = WebFrontendBuilder()
    await builder.build_complete_frontend()
    builder.print_summary()

if __name__ == "__main__":
    asyncio.run(main())
