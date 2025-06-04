#!/usr/bin/env python3
"""
🌐 WEB SETUP SCRIPT
Quick setup for the web-based AI system
"""

import os
import subprocess
import sys
from pathlib import Path

def print_banner():
    print("🌐" * 25)
    print("🎭 PRACTICAL AI SYSTEM - WEB INTERFACE SETUP")
    print("🌐" * 25)
    print()

def install_web_dependencies():
    print("📦 Installing web dependencies...")
    
    dependencies = [
        "fastapi",
        "uvicorn[standard]",
        "python-multipart"
    ]
    
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {dep} installed")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to install {dep}")

def create_web_files():
    print("\n📝 Creating web interface files...")
    
    # Create HTML file from the artifact
    html_content = '''<!-- The HTML content from the web frontend artifact goes here -->
<!-- Save the HTML artifact as index.html manually -->'''
    
    html_path = Path("index.html")
    if not html_path.exists():
        with open(html_path, "w", encoding="utf-8") as f:
            f.write("<!-- Save the HTML artifact here as index.html -->")
        print("📄 index.html placeholder created")
        print("⚠️  IMPORTANT: Copy the HTML artifact content into index.html")
    else:
        print("✅ index.html already exists")

def create_run_web_script():
    print("🚀 Creating web run script...")
    
    script_lines = [
        "#!/usr/bin/env python3",
        "# Run the web-based AI system",
        "",
        "import os",
        "import asyncio",
        "import webbrowser",
        "import time",
        "from threading import Timer",
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
        "def open_browser():",
        "    time.sleep(2)  # Wait for server to start",
        "    webbrowser.open('http://localhost:8000')",
        "",
        "def main():",
        "    print('🌐 Starting Web-based AI System...')",
        "    load_env()",
        "    ",
        "    # Open browser after delay",
        "    Timer(2.0, open_browser).start()",
        "    ",
        "    # Start the FastAPI server",
        "    os.system('python fastapi_backend.py')",
        "",
        "if __name__ == '__main__':",
        "    main()"
    ]
    
    with open("run_web.py", "w", encoding="utf-8") as f:
        for line in script_lines:
            f.write(line + "\n")
    
    # Make executable on Unix
    if os.name != 'nt':
        os.chmod("run_web.py", 0o755)
    
    print("✅ run_web.py created")

def print_instructions():
    print("\n" + "🌟" * 25)
    print("🎉 WEB SETUP COMPLETE!")
    print("🌟" * 25)
    
    print("\n📋 NEXT STEPS:")
    print()
    print("1. 📄 SAVE HTML FRONTEND:")
    print("   • Copy the 'Web Frontend for AI System' artifact")
    print("   • Save it as 'index.html' in this folder")
    print("   • Replace the placeholder content")
    print()
    print("2. 🚀 START THE WEB SYSTEM:")
    print("   python run_web.py")
    print("   OR")
    print("   python fastapi_backend.py")
    print()
    print("3. 🌐 OPEN IN BROWSER:")
    print("   http://localhost:8000")
    print("   (Browser should open automatically)")
    print()
    print("4. 🎭 WEB FEATURES:")
    print("   • Beautiful visual interface")
    print("   • Real-time AI orchestration")
    print("   • Multiple consciousness levels")
    print("   • Live solution generation")
    print("   • Interactive code previews")
    print()
    print("5. 🧠 CONSCIOUSNESS LEVELS:")
    print("   • LUCID: Clean, practical solutions")
    print("   • TRANSCENDENT: Optimized solutions")
    print("   • COSMIC: Universal harmony (default)")
    print("   • OMNISCIENT: All-knowing solutions")
    print("   • CREATIVE GOD: Reality-bending solutions")
    print()
    print("6. 📚 API DOCUMENTATION:")
    print("   http://localhost:8000/docs")

def main():
    print_banner()
    
    # Install dependencies
    install_web_dependencies()
    
    # Create files
    create_web_files()
    create_run_web_script()
    
    # Instructions
    print_instructions()

if __name__ == "__main__":
    main()
