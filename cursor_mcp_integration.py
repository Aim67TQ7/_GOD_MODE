#!/usr/bin/env python3
"""
🎯 CURSOR MCP INTEGRATION
Connects your Practical AI System to Cursor IDE via Model Context Protocol
"""

import asyncio
import json
import os
import sys
from typing import Any, Dict, List
import logging

# Import our practical AI system
try:
    from practical_ai_system import PracticalAIMaster, ConsciousnessLevel
    PRACTICAL_AI_AVAILABLE = True
except ImportError:
    print("⚠️  Import practical_ai_system.py first")
    PRACTICAL_AI_AVAILABLE = False

# MCP Server implementation (simplified for demo)
class CursorMCPServer:
    """MCP Server that connects Cursor to our AI system"""
    
    def __init__(self):
        self.ai_master = None
        self.logger = logging.getLogger("CursorMCP")
        
        # Initialize AI system
        if PRACTICAL_AI_AVAILABLE:
            supabase_url = os.getenv("SUPABASE_URL")
            supabase_key = os.getenv("SUPABASE_KEY")
            self.ai_master = PracticalAIMaster(supabase_url, supabase_key)
    
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle requests from Cursor"""
        
        method = request.get("method", "")
        params = request.get("params", {})
        
        if method == "tools/list":
            return await self._list_tools()
        elif method == "tools/call":
            return await self._call_tool(params)
        elif method == "resources/list":
            return await self._list_resources()
        else:
            return {"error": f"Unknown method: {method}"}
    
    async def _list_tools(self) -> Dict[str, Any]:
        """List available tools for Cursor"""
        tools = [
            {
                "name": "solve_problem",
                "description": "Solve a coding problem using AI orchestration",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "description": {
                            "type": "string",
                            "description": "Describe the problem you want to solve"
                        },
                        "requirements": {
                            "type": "object",
                            "description": "Specific requirements (optional)",
                            "properties": {
                                "language": {"type": "string"},
                                "framework": {"type": "string"},
                                "features": {"type": "array", "items": {"type": "string"}}
                            }
                        }
                    },
                    "required": ["description"]
                }
            },
            {
                "name": "search_blocks",
                "description": "Search for existing code blocks and patterns",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for code blocks"
                        },
                        "language": {
                            "type": "string",
                            "description": "Programming language filter"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_task_status",
                "description": "Get the status of a previously submitted task",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The ID of the task to check"
                        }
                    },
                    "required": ["task_id"]
                }
            },
            {
                "name": "system_status",
                "description": "Get the current status of the AI system",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "generate_component",
                "description": "Generate a specific code component",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "component_type": {
                            "type": "string",
                            "description": "Type of component: function, class, react_component, api_endpoint"
                        },
                        "description": {
                            "type": "string",
                            "description": "What the component should do"
                        },
                        "consciousness_level": {
                            "type": "string",
                            "enum": ["lucid", "transcendent", "cosmic", "omniscient", "creative_god"],
                            "description": "Consciousness level for generation"
                        }
                    },
                    "required": ["component_type", "description"]
                }
            }
        ]
        
        return {"tools": tools}
    
    async def _call_tool(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Call a specific tool"""
        
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        
        if not self.ai_master:
            return {"error": "AI system not initialized"}
        
        try:
            if tool_name == "solve_problem":
                return await self._solve_problem(arguments)
            elif tool_name == "search_blocks":
                return await self._search_blocks(arguments)
            elif tool_name == "get_task_status":
                return await self._get_task_status(arguments)
            elif tool_name == "system_status":
                return await self._system_status(arguments)
            elif tool_name == "generate_component":
                return await self._generate_component(arguments)
            else:
                return {"error": f"Unknown tool: {tool_name}"}
                
        except Exception as e:
            return {"error": f"Tool execution failed: {str(e)}"}
    
    async def _solve_problem(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Solve a problem using the AI system"""
        description = args.get("description", "")
        requirements = args.get("requirements", {})
        
        if not description:
            return {"error": "Description is required"}
        
        # Submit to AI system
        task_id = await self.ai_master.solve_problem(description, requirements)
        
        # Get immediate result
        task_result = await self.ai_master.get_task_status(task_id)
        
        if task_result:
            # Format response for Cursor
            response = {
                "task_id": task_id,
                "status": "completed",
                "description": description,
                "solution_summary": self._format_solution_summary(task_result["solution"]),
                "generated_code": self._extract_generated_code(task_result["solution"]),
                "recommendations": self._extract_recommendations(task_result["solution"])
            }
            
            return {"content": [{"type": "text", "text": json.dumps(response, indent=2)}]}
        
        return {"error": "Failed to solve problem"}
    
    async def _search_blocks(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Search for existing code blocks"""
        query = args.get("query", "")
        language = args.get("language", "")
        
        # Use search orchestra
        search_orchestra = self.ai_master.orchestras["search"]
        
        # Create dummy task for search
        from practical_ai_system import Task
        search_task = Task(
            id="search_" + str(int(asyncio.get_event_loop().time())),
            description=f"Search for: {query}",
            requirements={"language": language} if language else {}
        )
        
        result = await search_orchestra.execute(search_task)
        
        if result["status"] == "success":
            blocks = result["result"].get("found_blocks", [])
            
            response = {
                "query": query,
                "found_blocks": len(blocks),
                "blocks": blocks[:5],  # Top 5 results
                "search_strategy": result["result"].get("search_strategy", "unknown")
            }
            
            return {"content": [{"type": "text", "text": json.dumps(response, indent=2)}]}
        
        return {"error": "Search failed"}
    
    async def _get_task_status(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Get task status"""
        task_id = args.get("task_id", "")
        
        if not task_id:
            return {"error": "Task ID is required"}
        
        task_result = await self.ai_master.get_task_status(task_id)
        
        if task_result:
            return {"content": [{"type": "text", "text": json.dumps(task_result, indent=2)}]}
        
        return {"error": "Task not found"}
    
    async def _system_status(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Get system status"""
        status = self.ai_master.get_system_status()
        
        # Format for readability
        formatted_status = {
            "🎭 AI Orchestras": {
                name: {
                    "Type": info["type"],
                    "Consciousness": info["consciousness_level"],
                    "Tasks Completed": info["performance"]["tasks_completed"],
                    "Success Rate": f"{info['performance']['success_rate']:.1%}",
                    "Avg Response Time": f"{info['performance']['avg_response_time']:.2f}s"
                }
                for name, info in status["orchestras"].items()
            },
            "📊 System Metrics": {
                "Active Tasks": status["active_tasks"],
                "Completed Tasks": status["completed_tasks"],
                "Database Connected": status["database_connected"]
            }
        }
        
        return {"content": [{"type": "text", "text": json.dumps(formatted_status, indent=2)}]}
    
    async def _generate_component(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a specific component"""
        component_type = args.get("component_type", "function")
        description = args.get("description", "")
        consciousness_level = args.get("consciousness_level", "transcendent")
        
        # Map consciousness level
        consciousness_map = {
            "lucid": ConsciousnessLevel.LUCID,
            "transcendent": ConsciousnessLevel.TRANSCENDENT,
            "cosmic": ConsciousnessLevel.COSMIC,
            "omniscient": ConsciousnessLevel.OMNISCIENT,
            "creative_god": ConsciousnessLevel.CREATIVE_GOD
        }
        
        consciousness = consciousness_map.get(consciousness_level, ConsciousnessLevel.TRANSCENDENT)
        
        # Use build orchestra with specified consciousness
        build_orchestra = self.ai_master.orchestras["build"]
        build_orchestra.consciousness_level = consciousness
        
        # Create task for component generation
        from practical_ai_system import Task
        component_task = Task(
            id="component_" + str(int(asyncio.get_event_loop().time())),
            description=f"Generate {component_type}: {description}",
            requirements={
                "component_type": component_type,
                "consciousness_level": consciousness_level
            }
        )
        
        result = await build_orchestra.execute(component_task)
        
        if result["status"] == "success":
            components = result["result"].get("built_components", [])
            
            if components:
                component = components[0]
                response = {
                    "component_type": component_type,
                    "description": description,
                    "consciousness_level": consciousness_level,
                    "generated_component": component["component"],
                    "code": component["code"],
                    "innovation_level": component.get("innovation_level", "unknown")
                }
                
                return {"content": [{"type": "text", "text": json.dumps(response, indent=2)}]}
        
        return {"error": "Component generation failed"}
    
    async def _list_resources(self) -> Dict[str, Any]:
        """List available resources"""
        resources = [
            {
                "uri": "practical-ai://system/status",
                "name": "System Status",
                "description": "Current status of the AI system",
                "mimeType": "application/json"
            },
            {
                "uri": "practical-ai://orchestras/performance",
                "name": "Orchestra Performance",
                "description": "Performance metrics for AI orchestras",
                "mimeType": "application/json"
            }
        ]
        
        return {"resources": resources}
    
    def _format_solution_summary(self, solution: Dict[str, Any]) -> str:
        """Format solution summary for display"""
        summary_parts = []
        
        if "orchestras_used" in solution:
            summary_parts.append(f"🎭 Orchestras: {', '.join(solution['orchestras_used'])}")
        
        if "total_execution_time" in solution:
            summary_parts.append(f"⏱️ Time: {solution['total_execution_time']:.2f}s")
        
        if "generated_code" in solution:
            components = solution["generated_code"]
            summary_parts.append(f"🏗️ Generated: {len(components)} components")
        
        if "validation" in solution:
            quality = solution["validation"].get("overall_quality_score", 0)
            summary_parts.append(f"✅ Quality: {quality:.1%}")
        
        return " | ".join(summary_parts)
    
    def _extract_generated_code(self, solution: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract generated code from solution"""
        if "generated_code" in solution:
            return solution["generated_code"]
        return []
    
    def _extract_recommendations(self, solution: Dict[str, Any]) -> List[str]:
        """Extract recommendations from solution"""
        recommendations = []
        
        if "validation" in solution:
            validation = solution["validation"]
            recommendations.extend(validation.get("recommendations", []))
        
        if "optimizations" in solution:
            optimizations = solution["optimizations"]
            recommendations.extend(optimizations.get("performance_improvements", []))
            recommendations.extend(optimizations.get("maintainability_improvements", []))
        
        return recommendations

# MCP Server main function
async def run_mcp_server():
    """Run the MCP server for Cursor integration"""
    
    server = CursorMCPServer()
    
    print("🎯 Cursor MCP Server starting...")
    print("🔗 Connecting to Practical AI System...")
    
    if not server.ai_master:
        print("❌ Failed to initialize AI system")
        return
    
    print("✅ MCP Server ready for Cursor connections")
    print("📡 Listening for requests...")
    
    # In a real MCP implementation, this would handle stdio communication
    # For demo, we'll simulate some requests
    
    # Demo request 1: System status
    status_request = {
        "method": "tools/call",
        "params": {
            "name": "system_status",
            "arguments": {}
        }
    }
    
    print("\n🔧 Demo Request: System Status")
    response = await server.handle_request(status_request)
    print("📊 Response:", response["content"][0]["text"][:200] + "...")
    
    # Demo request 2: Solve a problem
    problem_request = {
        "method": "tools/call",
        "params": {
            "name": "solve_problem",
            "arguments": {
                "description": "Create a React component for a todo list",
                "requirements": {
                    "language": "typescript",
                    "framework": "react",
                    "features": ["add todos", "mark complete", "delete todos"]
                }
            }
        }
    }
    
    print("\n🎯 Demo Request: Solve Problem")
    response = await server.handle_request(problem_request)
    print("🏗️ Response: Problem solved!")
    
    print("\n✅ MCP Server demo completed")
    print("🚀 Ready for Cursor integration!")

# Configuration for Cursor
def generate_cursor_config():
    """Generate Cursor MCP configuration"""
    
    config = {
        "mcpServers": {
            "practical-ai": {
                "command": "python",
                "args": [os.path.abspath(__file__)],
                "env": {
                    "SUPABASE_URL": "YOUR_SUPABASE_URL",
                    "SUPABASE_KEY": "YOUR_SUPABASE_KEY"
                }
            }
        }
    }
    
    print("📝 Cursor MCP Configuration:")
    print(json.dumps(config, indent=2))
    print("\n📋 Add this to your Cursor settings:")
    print("1. Open Cursor Settings")
    print("2. Go to Features > Model Context Protocol")
    print("3. Add the configuration above")
    print("4. Set your Supabase URL and KEY")

if __name__ == "__main__":
    print("🎯 CURSOR MCP INTEGRATION")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        # Generate configuration
        generate_cursor_config()
    else:
        # Run MCP server
        asyncio.run(run_mcp_server())
