#!/usr/bin/env python3
"""
🚀 FASTAPI BACKEND FOR WEB INTERFACE
Connects the beautiful web frontend to your Practical AI System
"""

import asyncio
import os
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import asdict

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

# Import your AI system
try:
    from practical_ai_system import PracticalAIMaster, ConsciousnessLevel, Task, TaskStatus
    AI_SYSTEM_AVAILABLE = True
except ImportError:
    print("⚠️  practical_ai_system.py not found - using mock mode")
    AI_SYSTEM_AVAILABLE = False

# FastAPI app
app = FastAPI(
    title="🎭 Practical AI System API",
    description="Web API for the Multidimensional AI Development System",
    version="1.0.0"
)

# Enable CORS for web frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global AI system instance
ai_master = None

# Request/Response Models
class ProblemRequest(BaseModel):
    description: str
    tech_stack: Optional[str] = ""
    features: Optional[List[str]] = []
    consciousness_level: Optional[str] = "cosmic"

class SolutionResponse(BaseModel):
    id: str
    description: str
    consciousness_level: str
    solution_type: str
    solution_description: str
    orchestras_used: List[str]
    execution_time: float
    quality_score: float
    innovation_score: float
    components_generated: int
    code_preview: str
    tech_stack: str
    features: List[str]
    status: str

class OrchestraStatus(BaseModel):
    name: str
    type: str
    consciousness_level: str
    tasks_completed: int
    success_rate: float
    avg_response_time: float

class SystemStatus(BaseModel):
    orchestras: List[OrchestraStatus]
    active_tasks: int
    completed_tasks: int
    database_connected: bool
    system_uptime: str

# Initialize AI system
@app.on_event("startup")
async def startup_event():
    """Initialize the AI system on startup"""
    global ai_master
    
    if AI_SYSTEM_AVAILABLE:
        try:
            # Get Supabase credentials from environment
            supabase_url = os.getenv("SUPABASE_URL")
            supabase_key = os.getenv("SUPABASE_KEY")
            
            ai_master = PracticalAIMaster(supabase_url, supabase_key)
            print("✅ AI System initialized successfully")
        except Exception as e:
            print(f"⚠️  AI System initialization failed: {e}")
            print("🔧 Running in demo mode")
    else:
        print("🔧 Running in mock mode - AI system not available")

# Serve the web interface
@app.get("/", response_class=HTMLResponse)
async def serve_web_interface():
    """Serve the main web interface"""
    # In a real deployment, you'd serve the HTML file
    # For demo, return a simple redirect message
    return """
    <html>
        <head>
            <title>🎭 Practical AI System</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>🎭 Practical AI System</h1>
            <p>Save the HTML artifact as 'index.html' and open it in your browser!</p>
            <p>Then use this API at: <code>http://localhost:8000</code></p>
            <hr>
            <h2>API Endpoints:</h2>
            <ul style="text-align: left; max-width: 400px; margin: 0 auto;">
                <li><strong>GET /system/status</strong> - Get system status</li>
                <li><strong>POST /solve</strong> - Solve a problem</li>
                <li><strong>GET /tasks/{task_id}</strong> - Get task status</li>
                <li><strong>GET /docs</strong> - API documentation</li>
            </ul>
        </body>
    </html>
    """

# API Endpoints
@app.get("/system/status", response_model=SystemStatus)
async def get_system_status():
    """Get the current status of the AI system"""
    
    if not ai_master:
        # Return mock data if AI system not available
        return SystemStatus(
            orchestras=[
                OrchestraStatus(
                    name="SearchMaster",
                    type="search",
                    consciousness_level="cosmic",
                    tasks_completed=5,
                    success_rate=1.0,
                    avg_response_time=0.15
                ),
                OrchestraStatus(
                    name="BuildMaster", 
                    type="build",
                    consciousness_level="creative_god",
                    tasks_completed=3,
                    success_rate=1.0,
                    avg_response_time=0.25
                ),
                OrchestraStatus(
                    name="ValidateMaster",
                    type="validate", 
                    consciousness_level="transcendent",
                    tasks_completed=3,
                    success_rate=1.0,
                    avg_response_time=0.12
                ),
                OrchestraStatus(
                    name="OptimizeMaster",
                    type="optimize",
                    consciousness_level="omniscient", 
                    tasks_completed=2,
                    success_rate=1.0,
                    avg_response_time=0.18
                )
            ],
            active_tasks=0,
            completed_tasks=13,
            database_connected=False,
            system_uptime="demo_mode"
        )
    
    # Get real system status
    status = ai_master.get_system_status()
    
    orchestras = []
    for name, info in status["orchestras"].items():
        orchestras.append(OrchestraStatus(
            name=name,
            type=info["type"],
            consciousness_level=info["consciousness_level"],
            tasks_completed=info["performance"]["tasks_completed"],
            success_rate=info["performance"]["success_rate"],
            avg_response_time=info["performance"]["avg_response_time"]
        ))
    
    return SystemStatus(
        orchestras=orchestras,
        active_tasks=status["active_tasks"],
        completed_tasks=status["completed_tasks"],
        database_connected=status["database_connected"],
        system_uptime="active"
    )

@app.post("/solve", response_model=SolutionResponse)
async def solve_problem(request: ProblemRequest, background_tasks: BackgroundTasks):
    """Solve a problem using the AI system"""
    
    if not request.description.strip():
        raise HTTPException(status_code=400, detail="Problem description is required")
    
    # Prepare requirements
    requirements = {
        "consciousness_level": request.consciousness_level
    }
    
    if request.tech_stack:
        requirements["tech_stack"] = request.tech_stack
    
    if request.features:
        requirements["features"] = request.features
    
    if not ai_master:
        # Return mock solution if AI system not available
        return create_mock_solution(request)
    
    try:
        # Solve the problem using the AI system
        task_id = await ai_master.solve_problem(request.description, requirements)
        
        # Get the solution
        task_result = await ai_master.get_task_status(task_id)
        
        if not task_result:
            raise HTTPException(status_code=500, detail="Failed to solve problem")
        
        # Convert to response format
        solution = task_result["solution"]
        
        # Extract generated code preview
        code_preview = "# Solution generated successfully"
        if "generated_code" in solution and solution["generated_code"]:
            component = solution["generated_code"][0]
            if "code" in component:
                code_preview = component["code"][:1000] + "..." if len(component["code"]) > 1000 else component["code"]
        
        return SolutionResponse(
            id=task_id,
            description=request.description,
            consciousness_level=request.consciousness_level,
            solution_type=f"{request.consciousness_level.title()} Solution",
            solution_description=f"AI-generated solution using {request.consciousness_level} consciousness",
            orchestras_used=solution.get("orchestras_used", []),
            execution_time=solution.get("total_execution_time", 0.0),
            quality_score=solution.get("validation", {}).get("overall_quality_score", 0.85),
            innovation_score=0.95 if request.consciousness_level == "creative_god" else 0.7,
            components_generated=len(solution.get("generated_code", [])),
            code_preview=code_preview,
            tech_stack=request.tech_stack or "",
            features=request.features or [],
            status="completed"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error solving problem: {str(e)}")

def create_mock_solution(request: ProblemRequest) -> SolutionResponse:
    """Create a mock solution for demo purposes"""
    
    # Simulate processing time
    import time
    time.sleep(0.5)
    
    consciousness_descriptions = {
        "lucid": "Clean, maintainable solution with best practices",
        "transcendent": "Highly optimized solution with advanced patterns", 
        "cosmic": "Universally harmonious solution with perfect balance",
        "omniscient": "All-knowing solution with perfect foresight",
        "creative_god": "Reality-bending solution that transcends normal limitations"
    }
    
    solution_types = {
        "lucid": "Practical Implementation",
        "transcendent": "Transcendent Architecture",
        "cosmic": "Cosmic Harmony System", 
        "omniscient": "Omniscient Solution",
        "creative_god": "Revolutionary Reality-Bending Architecture"
    }
    
    # Generate mock code based on consciousness level
    if request.consciousness_level == "creative_god":
        code_preview = f'''# GOD MODE SOLUTION - REALITY-BENDING ARCHITECTURE
"""
{request.description}
Consciousness Level: CREATIVE_GOD
This solution transcends normal programming limitations
"""

class RealityManipulator:
    def __init__(self):
        self.omnipotence = True
        self.reality_access = True
        
    def solve_by_reality_modification(self, problem):
        # Solve by modifying fundamental laws of reality
        new_reality = self.create_reality_where_solved(problem)
        return self.manifest_solution(new_reality)
    
    def create_reality_where_solved(self, problem):
        # Create universe where problem is already solved
        return Universe.create_with_solution(problem)

# Implementation transcends normal code boundaries
solution = RealityManipulator().solve_by_reality_modification("{request.description}")'''
    
    elif request.consciousness_level == "omniscient":
        code_preview = f'''# OMNISCIENT SOLUTION - ALL-KNOWING IMPLEMENTATION
"""
{request.description}
Consciousness Level: OMNISCIENT
Perfect knowledge of all possible solutions
"""

class OmniscientSolver:
    def __init__(self):
        self.universal_knowledge = self.access_all_information()
        self.perfect_foresight = True
        
    def solve_with_perfect_knowledge(self, problem):
        # Access complete solution space
        optimal_solution = self.all_solutions[problem].get_optimal()
        return self.implement_perfect_solution(optimal_solution)

# Perfect solution with complete knowledge
solver = OmniscientSolver()
solution = solver.solve_with_perfect_knowledge("{request.description}")'''
    
    else:
        code_preview = f'''# {request.consciousness_level.upper()} SOLUTION
"""
{request.description}
Clean, maintainable implementation with modern best practices
"""

class SolutionImplementation:
    def __init__(self):
        self.best_practices = True
        self.maintainable = True
        
    def implement_solution(self, requirements):
        # Clean, professional implementation
        architecture = self.design_architecture(requirements)
        components = self.create_components(architecture)
        return self.integrate_components(components)

# Professional, maintainable solution
implementation = SolutionImplementation()
solution = implementation.implement_solution("{request.description}")'''
    
    return SolutionResponse(
        id=f"mock_{uuid.uuid4().hex[:8]}",
        description=request.description,
        consciousness_level=request.consciousness_level,
        solution_type=solution_types[request.consciousness_level],
        solution_description=consciousness_descriptions[request.consciousness_level],
        orchestras_used=["search", "build", "validate", "optimize"],
        execution_time=round(0.5 + __import__('random').random() * 2, 2),
        quality_score=0.8 + __import__('random').random() * 0.15,
        innovation_score=0.95 if request.consciousness_level == "creative_god" else 0.6 + __import__('random').random() * 0.3,
        components_generated=__import__('random').randint(1, 5),
        code_preview=code_preview,
        tech_stack=request.tech_stack or "",
        features=request.features or [],
        status="completed"
    )

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Get the status of a specific task"""
    
    if not ai_master:
        return {"error": "AI system not available"}
    
    try:
        task_result = await ai_master.get_task_status(task_id)
        
        if not task_result:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return task_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting task status: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "ai_system_available": ai_master is not None,
        "timestamp": datetime.now().isoformat()
    }

# Development helper endpoints
@app.get("/demo/problem")
async def get_demo_problem():
    """Get a demo problem for testing"""
    return {
        "description": "Build a full-stack todo application with React frontend, Python FastAPI backend, and PostgreSQL database",
        "tech_stack": "React, TypeScript, FastAPI, PostgreSQL, Docker",
        "features": ["CRUD operations", "user authentication", "priority levels", "due dates", "real-time updates"],
        "consciousness_level": "cosmic"
    }

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting Practical AI System Web API...")
    print("📡 Frontend: Save the HTML artifact and open in browser")
    print("🔧 Backend: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        access_log=True
    )
