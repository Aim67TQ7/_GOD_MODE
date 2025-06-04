#!/usr/bin/env python3
"""
🚀 SIMPLE SETUP SCRIPT - NO SYNTAX ERRORS
Clean, minimal setup for the Practical AI System
"""

import os
import subprocess
import sys
from pathlib import Path

def print_banner():
    print("🚀" * 20)
    print("🔧 PRACTICAL AI SYSTEM SETUP")
    print("🚀" * 20)
    print()

def check_python_version():
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    print("\n📦 Installing dependencies...")
    
    dependencies = ["supabase"]
    
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {dep} installed")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {dep}")

def create_env_file():
    print("\n📝 Creating .env file...")
    
    env_path = Path(".env")
    
    if env_path.exists():
        print("✅ .env file already exists")
        return
    
    # Simple string without complex quotes
    env_lines = [
        "# Supabase Configuration",
        "SUPABASE_URL=your_supabase_url_here",
        "SUPABASE_KEY=your_supabase_anon_key_here",
        "",
        "# Optional: OpenAI API Key",
        "OPENAI_API_KEY=your_openai_key_here",
        "",
        "# System Configuration", 
        "LOG_LEVEL=INFO",
        "DEBUG_MODE=false"
    ]
    
    with open(env_path, "w", encoding='utf-8') as f:
        for line in env_lines:
            f.write(line + "\n")
    
    print("✅ .env file created")
    print("📝 Edit .env with your Supabase credentials")

def create_simple_run_script():
    print("\n🏃 Creating run script...")
    
    # Write script line by line to avoid quote issues
    lines = [
        "#!/usr/bin/env python3",
        "# Simple run script for Practical AI System",
        "",
        "import asyncio",
        "import os",
        "",
        "def load_env():",
        "    env_file = '.env'",
        "    if os.path.exists(env_file):",
        "        with open(env_file, 'r') as f:",
        "            for line in f:",
        "                line = line.strip()",
        "                if line and not line.startswith('#') and '=' in line:",
        "                    key, value = line.split('=', 1)",
        "                    os.environ[key] = value",
        "",
        "async def main():",
        "    print('Starting Practical AI System...')",
        "    load_env()",
        "    ",
        "    # Import and run the demo",
        "    from practical_ai_system import run_practical_ai_demo",
        "    await run_practical_ai_demo()",
        "",
        "if __name__ == '__main__':",
        "    asyncio.run(main())"
    ]
    
    with open("run_ai.py", "w", encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")
    
    # Make executable on Unix
    if os.name != 'nt':
        os.chmod("run_ai.py", 0o755)
    
    print("✅ run_ai.py created")

def create_cursor_config():
    print("\n🎯 Creating Cursor configuration...")
    
    current_dir = os.path.abspath(".")
    mcp_server_path = os.path.join(current_dir, "cursor_mcp_integration.py")
    
    # Create config as lines to avoid JSON quote issues
    config_lines = [
        "{",
        '  "mcpServers": {',
        '    "practical-ai": {',
        '      "command": "python",',
        f'      "args": ["{mcp_server_path.replace(os.sep, "/")}"],',
        '      "env": {',
        '        "SUPABASE_URL": "${SUPABASE_URL}",',
        '        "SUPABASE_KEY": "${SUPABASE_KEY}"',
        '      }',
        '    }',
        '  }',
        "}"
    ]
    
    with open("cursor-mcp-config.json", "w", encoding='utf-8') as f:
        for line in config_lines:
            f.write(line + "\n")
    
    print("✅ cursor-mcp-config.json created")

def test_system():
    print("\n🧪 Testing system...")
    
    try:
        # Test import
        from practical_ai_system import PracticalAIMaster, ConsciousnessLevel
        print("✅ Practical AI System imports working")
        
        # Test creation
        ai = PracticalAIMaster()
        print("✅ AI Master initialization working")
        
        # Test orchestras
        orchestras = list(ai.orchestras.keys())
        print(f"✅ {len(orchestras)} orchestras loaded: {', '.join(orchestras)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def print_instructions():
    print("\n" + "🌟" * 20)
    print("🎉 SETUP COMPLETE!")
    print("🌟" * 20)
    
    print("\n📋 NEXT STEPS:")
    print()
    print("1. 🗄️  CONFIGURE DATABASE:")
    print("   • Edit .env file with your Supabase URL and key")
    print("   • Your database schema should already be set up")
    print()
    print("2. 🚀 TEST THE SYSTEM:")
    print("   python run_ai.py")
    print()
    print("3. 🌟 RUN FULL DEMO:")
    print("   python full_demo_script.py")
    print()
    print("4. 🎯 CURSOR INTEGRATION (Optional):")
    print("   • Open Cursor settings")
    print("   • Import cursor-mcp-config.json")
    print("   • Use @practical-ai commands")
    print()
    print("5. 🎭 EXAMPLE USAGE:")
    print("   from practical_ai_system import PracticalAIMaster")
    print("   ai = PracticalAIMaster()")
    print("   task_id = await ai.solve_problem('Build a todo app')")

def main():
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    install_dependencies()
    
    # Create files
    create_env_file()
    create_simple_run_script()
    create_cursor_config()
    
    # Test the system
    if test_system():
        print_instructions()
    else:
        print("\n❌ Setup completed with errors")
        print("🔧 Try running the individual components manually")

if __name__ == "__main__":
    main()
