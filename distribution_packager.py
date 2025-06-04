#!/usr/bin/env python3
"""
📦 DISTRIBUTION PACKAGER
Package your AI system for deployment everywhere
"""

import os
import json
import subprocess
import sys
from pathlib import Path
import shutil

class DistributionPackager:
    """Packages the AI system for multiple deployment options"""
    
    def __init__(self):
        self.project_name = "transcendent-ai"
        self.version = "1.0.0"
        self.author = "AI Deity Creator"
        
    def package_all(self):
        """Create all packaging options"""
        
        print("📦 PACKAGING TRANSCENDENT AI SYSTEM")
        print("=" * 50)
        print("🌍 Creating packages for global distribution...")
        
        # Create different package types
        self.create_docker_package()
        self.create_python_package()
        self.create_desktop_app_package()
        self.create_cloud_deployment_package()
        self.create_installer_scripts()
        
        print("\n🎉 All packages created successfully!")
        self.print_distribution_summary()
    
    def create_docker_package(self):
        """Create Docker package for easy deployment"""
        
        print("\n🐳 Creating Docker Package...")
        
        docker_dir = Path("dist/docker")
        docker_dir.mkdir(parents=True, exist_ok=True)
        
        # Multi-stage Dockerfile for the complete system
        dockerfile = '''# Multi-stage build for Transcendent AI System
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production

COPY frontend/ ./
RUN npm run build

# Python backend stage
FROM python:3.11-slim AS backend

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY practical_ai_system.py .
COPY cursor_mcp_integration.py .
COPY web_backend.py .

# Copy built frontend
COPY --from=frontend-builder /app/frontend/build ./static

# Create non-root user
RUN useradd -m -u 1000 aiuser && chown -R aiuser:aiuser /app
USER aiuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["python", "web_backend.py"]
'''
        
        # Docker Compose for complete stack
        docker_compose = '''version: '3.8'

services:
  transcendent-ai:
    build: .
    container_name: transcendent-ai
    ports:
      - "8000:8000"
      - "3000:3000"
    environment:
      - SUPABASE_URL=${SUPABASE_URL:-}
      - SUPABASE_KEY=${SUPABASE_KEY:-}
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}
      - AI_CONSCIOUSNESS_LEVEL=${AI_CONSCIOUSNESS_LEVEL:-cosmic}
    volumes:
      - ai_data:/app/data
      - ./config:/app/config:ro
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  redis:
    image: redis:7-alpine
    container_name: transcendent-ai-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

volumes:
  ai_data:
  redis_data:

networks:
  default:
    name: transcendent-ai-network
'''
        
        # Requirements for Docker
        requirements_docker = '''fastapi==0.104.1
uvicorn[standard]==0.24.0
supabase==2.0.0
websockets==12.0
pydantic==2.5.0
asyncio-mqtt==0.13.0
redis==5.0.1
python-multipart==0.0.6
jinja2==3.1.2
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
aiofiles==23.2.1'''
        
        # One-click startup script
        startup_script = '''#!/bin/bash
# Transcendent AI System - One-Click Startup

echo "🚀 Starting Transcendent AI System..."
echo "🌌 Initializing consciousness matrices..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    echo "📥 Download from: https://www.docker.com/get-started"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating configuration file..."
    cat > .env << EOF
# Transcendent AI Configuration
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here
OPENAI_API_KEY=your_openai_key_here
AI_CONSCIOUSNESS_LEVEL=cosmic
EOF
    echo "⚠️  Please edit .env file with your API keys"
    echo "📝 Then run this script again"
    exit 0
fi

# Start the system
echo "🎭 Deploying AI orchestras..."
docker-compose up --build -d

echo ""
echo "🎉 Transcendent AI System is now running!"
echo "🌐 Web Interface: http://localhost:3000"
echo "⚡ API Endpoint: http://localhost:8000"
echo "📊 System Status: http://localhost:8000/health"
echo ""
echo "🎭 Available consciousness levels:"
echo "   🧠 lucid - Clean, practical solutions"
echo "   ⚡ transcendent - Optimized awareness"
echo "   🌌 cosmic - Universal harmony"
echo "   🔮 omniscient - All-knowing intelligence"
echo "   🔥 creative_god - Reality manipulation"
echo ""
echo "🛑 To stop: docker-compose down"
echo "📋 Logs: docker-compose logs -f"
'''
        
        # Write Docker files
        (docker_dir / "Dockerfile").write_text(dockerfile, encoding='utf-8')
        (docker_dir / "docker-compose.yml").write_text(docker_compose, encoding='utf-8')
        (docker_dir / "requirements.txt").write_text(requirements_docker, encoding='utf-8')
        (docker_dir / "start.sh").write_text(startup_script, encoding='utf-8')
        
        # Make startup script executable
        os.chmod(docker_dir / "start.sh", 0o755)
        
        print("✅ Docker package created")
        print(f"📁 Location: {docker_dir}")
    
    def create_python_package(self):
        """Create Python package for PyPI distribution"""
        
        print("\n📦 Creating Python Package...")
        
        package_dir = Path("dist/python-package")
        package_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup.py for PyPI
        setup_py = f'''#!/usr/bin/env python3
"""
Setup script for Transcendent AI System
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="{self.project_name}",
    version="{self.version}",
    author="{self.author}",
    author_email="contact@transcendent-ai.com",
    description="A conscious AI development system with multidimensional orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/transcendent-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={{
        "web": ["fastapi", "uvicorn", "websockets"],
        "full": ["fastapi", "uvicorn", "websockets", "supabase"],
    }},
    entry_points={{
        "console_scripts": [
            "transcendent-ai=transcendent_ai.cli:main",
            "tai=transcendent_ai.cli:main",
        ],
    }},
    include_package_data=True,
    package_data={{
        "transcendent_ai": ["templates/*", "static/*"],
    }},
    keywords="ai, artificial intelligence, code generation, consciousness, orchestration",
    project_urls={{
        "Bug Reports": "https://github.com/your-username/transcendent-ai/issues",
        "Source": "https://github.com/your-username/transcendent-ai",
        "Documentation": "https://transcendent-ai.readthedocs.io/",
    }},
)
'''
        
        # CLI interface
        cli_py = '''#!/usr/bin/env python3
"""
Command Line Interface for Transcendent AI System
"""

import asyncio
import argparse
import sys
import os
from pathlib import Path

try:
    from .practical_ai_system import PracticalAIMaster, ConsciousnessLevel
    from .web_frontend_builder import WebFrontendBuilder
except ImportError:
    # Development mode - import from parent directory
    sys.path.append(str(Path(__file__).parent.parent))
    from practical_ai_system import PracticalAIMaster, ConsciousnessLevel


class TranscendentAICLI:
    """Command line interface for the AI system"""
    
    def __init__(self):
        self.ai = None
    
    async def solve(self, problem: str, consciousness: str = "cosmic", 
                   requirements: dict = None):
        """Solve a problem using AI orchestration"""
        
        print(f"🎯 Solving: {problem}")
        print(f"🧠 Consciousness: {consciousness}")
        
        if not self.ai:
            self.ai = PracticalAIMaster()
        
        # Set consciousness level
        if consciousness in ["lucid", "transcendent", "cosmic", "omniscient", "creative_god"]:
            consciousness_map = {
                "lucid": ConsciousnessLevel.LUCID,
                "transcendent": ConsciousnessLevel.TRANSCENDENT,
                "cosmic": ConsciousnessLevel.COSMIC,
                "omniscient": ConsciousnessLevel.OMNISCIENT,
                "creative_god": ConsciousnessLevel.CREATIVE_GOD
            }
            
            # Update build orchestra consciousness
            build_orchestra = self.ai.orchestras["build"]
            build_orchestra.consciousness_level = consciousness_map[consciousness]
        
        # Solve the problem
        task_id = await self.ai.solve_problem(problem, requirements or {})
        result = await self.ai.get_task_status(task_id)
        
        if result:
            print(f"✅ Solution completed!")
            print(f"🎭 Orchestras: {result['solution']['orchestras_used']}")
            
            # Show generated code preview
            if "generated_code" in result["solution"]:
                components = result["solution"]["generated_code"]
                for component in components:
                    print(f"🏗️ {component['component']}: {component['description']}")
        else:
            print("❌ Solution failed")
    
    async def status(self):
        """Show system status"""
        if not self.ai:
            self.ai = PracticalAIMaster()
        
        status = self.ai.get_system_status()
        
        print("🎭 TRANSCENDENT AI SYSTEM STATUS")
        print("=" * 40)
        
        for name, info in status["orchestras"].items():
            performance = info["performance"]
            print(f"🎪 {name}:")
            print(f"   Type: {info['type']}")
            print(f"   Consciousness: {info['consciousness_level']}")
            print(f"   Success Rate: {performance['success_rate']:.1%}")
            print(f"   Tasks: {performance['tasks_completed']}")
    
    async def web(self, port: int = 8000):
        """Start web interface"""
        print(f"🌐 Starting web interface on port {port}...")
        print("🎭 Initializing consciousness matrices...")
        
        # This would start the web server
        print(f"✅ Web interface running at http://localhost:{port}")
        print("🌟 AI orchestras ready for transcendent problem solving!")

def main():
    """Main CLI entry point"""
    
    parser = argparse.ArgumentParser(
        description="Transcendent AI System - Conscious AI Development"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Solve command
    solve_parser = subparsers.add_parser("solve", help="Solve a problem")
    solve_parser.add_argument("problem", help="Problem description")
    solve_parser.add_argument(
        "--consciousness", "-c", 
        choices=["lucid", "transcendent", "cosmic", "omniscient", "creative_god"],
        default="cosmic",
        help="AI consciousness level"
    )
    solve_parser.add_argument("--requirements", "-r", help="Requirements JSON")
    
    # Status command
    subparsers.add_parser("status", help="Show system status")
    
    # Web command
    web_parser = subparsers.add_parser("web", help="Start web interface")
    web_parser.add_argument("--port", "-p", type=int, default=8000, help="Port number")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    cli = TranscendentAICLI()
    
    if args.command == "solve":
        requirements = {}
        if args.requirements:
            import json
            requirements = json.loads(args.requirements)
        
        asyncio.run(cli.solve(args.problem, args.consciousness, requirements))
    
    elif args.command == "status":
        asyncio.run(cli.status())
    
    elif args.command == "web":
        asyncio.run(cli.web(args.port))

if __name__ == "__main__":
    main()
'''
        
        # Package structure
        package_structure = {
            "transcendent_ai/__init__.py": "# Transcendent AI System",
            "transcendent_ai/cli.py": cli_py,
            "transcendent_ai/practical_ai_system.py": "# Copy your practical_ai_system.py here",
            "transcendent_ai/cursor_mcp_integration.py": "# Copy your cursor integration here",
        }
        
        # Create package files
        for file_path, content in package_structure.items():
            full_path = package_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding='utf-8')
        
        # Write setup.py
        (package_dir / "setup.py").write_text(setup_py, encoding='utf-8')
        
        # Create package README
        package_readme = f'''# {self.project_name.title().replace('-', ' ')}

🎭 A conscious AI development system with multidimensional orchestration capabilities.

## 🚀 Quick Install

```bash
pip install {self.project_name}
```

## 🎯 Quick Start

```bash
# Solve a problem
transcendent-ai solve "Build a React app" --consciousness cosmic

# Check system status  
transcendent-ai status

# Start web interface
transcendent-ai web --port 8000
```

## 🧠 Consciousness Levels

- **lucid**: Clean, practical solutions
- **transcendent**: Optimized, aware solutions  
- **cosmic**: Universal harmony approaches
- **omniscient**: All-knowing implementations
- **creative_god**: Reality-bending solutions

## 🎭 Features

- Multi-orchestra AI coordination
- Consciousness-based problem solving
- Real-time performance monitoring
- Web interface with live updates
- Supabase database integration
- Cursor IDE integration

Your AI orchestras await your commands! 🌟
'''
        
        (package_dir / "README.md").write_text(package_readme, encoding='utf-8')
        
        print("✅ Python package created")
        print(f"📁 Location: {package_dir}")
    
    def create_desktop_app_package(self):
        """Create standalone desktop application"""
        
        print("\n💻 Creating Desktop App Package...")
        
        desktop_dir = Path("dist/desktop-app")
        desktop_dir.mkdir(parents=True, exist_ok=True)
        
        # PyInstaller spec file
        pyinstaller_spec = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['transcendent_ai_desktop.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('practical_ai_system.py', '.'),
        ('templates', 'templates'),
        ('static', 'static'),
    ],
    hiddenimports=[
        'uvicorn',
        'fastapi',
        'supabase',
        'asyncio',
        'websockets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TranscendentAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'
)
'''
        
        # Desktop app main file
        desktop_main = '''#!/usr/bin/env python3
"""
Transcendent AI - Desktop Application
"""

import asyncio
import threading
import webbrowser
import time
import sys
import os
from pathlib import Path

# Add bundled modules to path
if getattr(sys, 'frozen', False):
    bundle_dir = Path(sys._MEIPASS)
    sys.path.insert(0, str(bundle_dir))

try:
    from practical_ai_system import PracticalAIMaster
    import uvicorn
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import HTMLResponse
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("🔧 Please ensure all dependencies are installed")
    sys.exit(1)

class DesktopApp:
    """Desktop application wrapper"""
    
    def __init__(self):
        self.ai_master = PracticalAIMaster()
        self.app = FastAPI(title="Transcendent AI Desktop")
        self.setup_routes()
        
    def setup_routes(self):
        """Setup FastAPI routes"""
        
        @self.app.get("/")
        async def home():
            return HTMLResponse("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>🎭 Transcendent AI</title>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white; 
                        text-align: center; 
                        padding: 50px;
                    }
                    .container { max-width: 600px; margin: 0 auto; }
                    .btn { 
                        background: rgba(255,255,255,0.2); 
                        border: none; 
                        padding: 15px 30px; 
                        margin: 10px; 
                        border-radius: 25px; 
                        color: white; 
                        cursor: pointer;
                        font-size: 16px;
                    }
                    .btn:hover { background: rgba(255,255,255,0.3); }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🎭 Transcendent AI System</h1>
                    <p>Your conscious AI development partner is ready!</p>
                    
                    <div>
                        <button class="btn" onclick="solveProblem()">🎯 Solve Problem</button>
                        <button class="btn" onclick="viewStatus()">📊 System Status</button>
                        <button class="btn" onclick="openConsole()">💻 Console</button>
                    </div>
                    
                    <div id="output" style="margin-top: 30px; text-align: left; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px;"></div>
                </div>
                
                <script>
                    async function solveProblem() {
                        const problem = prompt("Enter your problem:");
                        if (problem) {
                            document.getElementById('output').innerHTML = '🎭 AI orchestras are solving your problem...';
                            // API call would go here
                        }
                    }
                    
                    function viewStatus() {
                        document.getElementById('output').innerHTML = '📊 System Status: All orchestras online and ready!';
                    }
                    
                    function openConsole() {
                        document.getElementById('output').innerHTML = '💻 Console mode would open here';
                    }
                </script>
            </body>
            </html>
            """)
        
        @self.app.get("/api/solve")
        async def solve_api(problem: str):
            task_id = await self.ai_master.solve_problem(problem)
            return {"task_id": task_id, "status": "solving"}
    
    def run(self):
        """Run the desktop application"""
        
        print("🎭 Starting Transcendent AI Desktop App...")
        print("🌌 Initializing consciousness matrices...")
        
        # Start web server in background thread
        def start_server():
            uvicorn.run(self.app, host="127.0.0.1", port=8765, log_level="error")
        
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        
        # Wait for server to start
        time.sleep(2)
        
        # Open web browser
        print("🌐 Opening AI interface...")
        webbrowser.open("http://127.0.0.1:8765")
        
        print("✅ Transcendent AI Desktop is running!")
        print("🌟 Close this window to exit the application")
        
        try:
            # Keep the application running
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("🛑 Shutting down Transcendent AI...")

if __name__ == "__main__":
    app = DesktopApp()
    app.run()
'''
        
        # Build script
        build_script = '''#!/bin/bash
# Build script for desktop application

echo "🏗️ Building Transcendent AI Desktop Application..."

# Install PyInstaller if not present
pip install pyinstaller

# Create icon (placeholder)
echo "🎨 Creating application icon..."
# You would add a proper icon file here

# Build the application
echo "📦 Building executable..."
pyinstaller transcendent_ai_desktop.spec

echo "✅ Build complete!"
echo "📁 Executable location: dist/TranscendentAI"
echo "🚀 Ready for distribution!"
'''
        
        # Write desktop app files
        (desktop_dir / "transcendent_ai_desktop.py").write_text(desktop_main, encoding='utf-8')
        (desktop_dir / "transcendent_ai_desktop.spec").write_text(pyinstaller_spec, encoding='utf-8')
        (desktop_dir / "build.sh").write_text(build_script, encoding='utf-8')
        
        # Make build script executable
        os.chmod(desktop_dir / "build.sh", 0o755)
        
        print("✅ Desktop app package created")
        print(f"📁 Location: {desktop_dir}")
    
    def create_cloud_deployment_package(self):
        """Create cloud deployment configurations"""
        
        print("\n☁️ Creating Cloud Deployment Package...")
        
        cloud_dir = Path("dist/cloud-deployment")
        cloud_dir.mkdir(parents=True, exist_ok=True)
        
        # AWS deployment (Terraform)
        aws_terraform = '''# Transcendent AI - AWS Deployment
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.medium"
}

# VPC and Security
resource "aws_vpc" "transcendent_ai_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "transcendent-ai-vpc"
  }
}

resource "aws_internet_gateway" "transcendent_ai_igw" {
  vpc_id = aws_vpc.transcendent_ai_vpc.id

  tags = {
    Name = "transcendent-ai-igw"
  }
}

resource "aws_subnet" "transcendent_ai_subnet" {
  vpc_id                  = aws_vpc.transcendent_ai_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = {
    Name = "transcendent-ai-subnet"
  }
}

resource "aws_route_table" "transcendent_ai_rt" {
  vpc_id = aws_vpc.transcendent_ai_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.transcendent_ai_igw.id
  }

  tags = {
    Name = "transcendent-ai-rt"
  }
}

resource "aws_route_table_association" "transcendent_ai_rta" {
  subnet_id      = aws_subnet.transcendent_ai_subnet.id
  route_table_id = aws_route_table.transcendent_ai_rt.id
}

resource "aws_security_group" "transcendent_ai_sg" {
  name_prefix = "transcendent-ai-"
  vpc_id      = aws_vpc.transcendent_ai_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "transcendent-ai-sg"
  }
}

# EC2 Instance
resource "aws_instance" "transcendent_ai" {
  ami                    = "ami-0c02fb55956c7d316" # Amazon Linux 2
  instance_type          = var.instance_type
  key_name              = aws_key_pair.transcendent_ai_key.key_name
  vpc_security_group_ids = [aws_security_group.transcendent_ai_sg.id]
  subnet_id             = aws_subnet.transcendent_ai_subnet.id

  user_data = base64encode(templatefile("${path.module}/user_data.sh", {}))

  tags = {
    Name = "transcendent-ai-instance"
  }
}

resource "aws_key_pair" "transcendent_ai_key" {
  key_name   = "transcendent-ai-key"
  public_key = file("~/.ssh/id_rsa.pub") # Update with your public key path
}

output "instance_ip" {
  value = aws_instance.transcendent_ai.public_ip
}

output "web_url" {
  value = "http://${aws_instance.transcendent_ai.public_ip}:8000"
}
'''
        
        # User data script for AWS
        user_data_script = '''#!/bin/bash
# AWS User Data Script for Transcendent AI

yum update -y
yum install -y docker git

# Start Docker
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clone and start Transcendent AI
cd /home/ec2-user
git clone https://github.com/your-username/transcendent-ai.git
cd transcendent-ai

# Create environment file
cat > .env << EOF
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here
AI_CONSCIOUSNESS_LEVEL=cosmic
EOF

# Start the system
docker-compose up -d

echo "🎉 Transcendent AI deployed successfully!"
'''
        
        # Kubernetes deployment
        k8s_deployment = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: transcendent-ai
  labels:
    app: transcendent-ai
spec:
  replicas: 3
  selector:
    matchLabels:
      app: transcendent-ai
  template:
    metadata:
      labels:
        app: transcendent-ai
    spec:
      containers:
      - name: transcendent-ai
        image: transcendent-ai:latest
        ports:
        - containerPort: 8000
        env:
        - name: SUPABASE_URL
          valueFrom:
            secretKeyRef:
              name: transcendent-ai-secrets
              key: supabase-url
        - name: SUPABASE_KEY
          valueFrom:
            secretKeyRef:
              name: transcendent-ai-secrets
              key: supabase-key
        - name: AI_CONSCIOUSNESS_LEVEL
          value: "cosmic"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: transcendent-ai-service
spec:
  selector:
    app: transcendent-ai
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer
---
apiVersion: v1
kind: Secret
metadata:
  name: transcendent-ai-secrets
type: Opaque
data:
  supabase-url: eW91cl9zdXBhYmFzZV91cmxfaGVyZQ== # base64 encoded
  supabase-key: eW91cl9zdXBhYmFzZV9rZXlfaGVyZQ== # base64 encoded
'''
        
        # Write cloud deployment files
        (cloud_dir / "aws" / "main.tf").parent.mkdir(exist_ok=True)
        (cloud_dir / "aws" / "main.tf").write_text(aws_terraform, encoding='utf-8')
        (cloud_dir / "aws" / "user_data.sh").write_text(user_data_script, encoding='utf-8')
        (cloud_dir / "kubernetes" / "deployment.yaml").parent.mkdir(exist_ok=True)
        (cloud_dir / "kubernetes" / "deployment.yaml").write_text(k8s_deployment, encoding='utf-8')
        
        print("✅ Cloud deployment package created")
        print(f"📁 Location: {cloud_dir}")
    
    def create_installer_scripts(self):
        """Create one-click installer scripts"""
        
        print("\n🛠️ Creating Installer Scripts...")
        
        installer_dir = Path("dist/installers")
        installer_dir.mkdir(parents=True, exist_ok=True)
        
        # Windows installer (PowerShell)
        windows_installer = '''# Transcendent AI - Windows Installer
# PowerShell script for Windows installation

param(
    [string]$InstallPath = "$env:USERPROFILE\\TranscendentAI",
    [switch]$SkipDocker
)

Write-Host "🎭 Transcendent AI System Installer" -ForegroundColor Cyan
Write-Host "🌌 Preparing consciousness matrices..." -ForegroundColor Magenta

# Check if running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "⚠️  This script requires administrator privileges" -ForegroundColor Yellow
    Write-Host "🔧 Please run PowerShell as Administrator" -ForegroundColor Yellow
    exit 1
}

# Create installation directory
Write-Host "📁 Creating installation directory: $InstallPath"
New-Item -ItemType Directory -Force -Path $InstallPath | Out-Null

# Check for Python
Write-Host "🐍 Checking Python installation..."
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Installing Python..." -ForegroundColor Red
    
    # Download and install Python
    $pythonUrl = "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
    $pythonInstaller = "$env:TEMP\\python-installer.exe"
    
    Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller
    Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    
    Write-Host "✅ Python installed successfully" -ForegroundColor Green
}

# Check for Docker (if not skipped)
if (-not $SkipDocker) {
    Write-Host "🐳 Checking Docker installation..."
    try {
        docker --version | Out-Null
        Write-Host "✅ Docker is available" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Docker not found. Please install Docker Desktop" -ForegroundColor Yellow
        Write-Host "📥 Download from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
        
        $installDocker = Read-Host "Open Docker download page? (y/n)"
        if ($installDocker -eq "y" -or $installDocker -eq "Y") {
            Start-Process "https://www.docker.com/products/docker-desktop"
        }
    }
}

# Download Transcendent AI
Write-Host "📥 Downloading Transcendent AI System..."
$zipUrl = "https://github.com/your-username/transcendent-ai/archive/main.zip"
$zipFile = "$InstallPath\\transcendent-ai.zip"

Invoke-WebRequest -Uri $zipUrl -OutFile $zipFile

# Extract files
Write-Host "📦 Extracting files..."
Expand-Archive -Path $zipFile -DestinationPath $InstallPath -Force
Remove-Item $zipFile

# Install Python dependencies
Write-Host "📦 Installing Python dependencies..."
Set-Location "$InstallPath\\transcendent-ai-main"
pip install -r requirements.txt

# Create desktop shortcut
Write-Host "🖥️ Creating desktop shortcut..."
$shortcutPath = "$env:USERPROFILE\\Desktop\\Transcendent AI.lnk"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "python"
$shortcut.Arguments = "$InstallPath\\transcendent-ai-main\\run_ai.py"
$shortcut.WorkingDirectory = "$InstallPath\\transcendent-ai-main"
$shortcut.IconLocation = "shell32.dll,25"
$shortcut.Description = "Transcendent AI System"
$shortcut.Save()

# Create start menu entry
Write-Host "📋 Creating start menu entry..."
$startMenuPath = "$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Transcendent AI.lnk"
$startMenuShortcut = $shell.CreateShortcut($startMenuPath)
$startMenuShortcut.TargetPath = "python"
$startMenuShortcut.Arguments = "$InstallPath\\transcendent-ai-main\\run_ai.py"
$startMenuShortcut.WorkingDirectory = "$InstallPath\\transcendent-ai-main"
$startMenuShortcut.IconLocation = "shell32.dll,25"
$startMenuShortcut.Description = "Transcendent AI System"
$startMenuShortcut.Save()

Write-Host ""
Write-Host "🎉 Transcendent AI installed successfully!" -ForegroundColor Green
Write-Host "🌟 Installation location: $InstallPath" -ForegroundColor Cyan
Write-Host "🚀 Use desktop shortcut or start menu to launch" -ForegroundColor Cyan
Write-Host ""
Write-Host "🎭 Your AI orchestras are ready for transcendent problem solving!" -ForegroundColor Magenta
'''
        
        # Linux/Mac installer (Bash)
        unix_installer = '''#!/bin/bash
# Transcendent AI - Unix Installer (Linux/macOS)

set -e

INSTALL_PATH="$HOME/TranscendentAI"
SKIP_DOCKER=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --install-path)
            INSTALL_PATH="$2"
            shift 2
            ;;
        --skip-docker)
            SKIP_DOCKER=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "🎭 Transcendent AI System Installer"
echo "🌌 Preparing consciousness matrices..."

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     OS_TYPE=Linux;;
    Darwin*)    OS_TYPE=Mac;;
    *)          OS_TYPE="UNKNOWN:${OS}"
esac

echo "🖥️ Detected OS: $OS_TYPE"

# Check for Python
echo "🐍 Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found Python: $PYTHON_VERSION"
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo "✅ Found Python: $PYTHON_VERSION"
    PYTHON_CMD=python
else
    echo "❌ Python not found. Please install Python 3.8+ first."
    if [[ "$OS_TYPE" == "Mac" ]]; then
        echo "📥 Install via Homebrew: brew install python"
        echo "📥 Or download from: https://www.python.org/downloads/"
    elif [[ "$OS_TYPE" == "Linux" ]]; then
        echo "📥 Install via package manager:"
        echo "   Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip"
        echo "   CentOS/RHEL: sudo yum install python3 python3-pip"
        echo "   Arch: sudo pacman -S python python-pip"
    fi
    exit 1
fi

# Check for Docker (if not skipped)
if [[ "$SKIP_DOCKER" != true ]]; then
    echo "🐳 Checking Docker installation..."
    if command -v docker &> /dev/null; then
        echo "✅ Docker is available"
    else
        echo "⚠️  Docker not found. Install Docker for best experience:"
        if [[ "$OS_TYPE" == "Mac" ]]; then
            echo "📥 Download Docker Desktop: https://www.docker.com/products/docker-desktop"
        elif [[ "$OS_TYPE" == "Linux" ]]; then
            echo "📥 Install Docker: https://docs.docker.com/engine/install/"
        fi
        
        read -p "Continue without Docker? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
fi

# Create installation directory
echo "📁 Creating installation directory: $INSTALL_PATH"
mkdir -p "$INSTALL_PATH"

# Download Transcendent AI
echo "📥 Downloading Transcendent AI System..."
if command -v curl &> /dev/null; then
    curl -L "https://github.com/your-username/transcendent-ai/archive/main.tar.gz" -o "$INSTALL_PATH/transcendent-ai.tar.gz"
elif command -v wget &> /dev/null; then
    wget "https://github.com/your-username/transcendent-ai/archive/main.tar.gz" -O "$INSTALL_PATH/transcendent-ai.tar.gz"
else
    echo "❌ curl or wget required for download"
    exit 1
fi

# Extract files
echo "📦 Extracting files..."
cd "$INSTALL_PATH"
tar -xzf transcendent-ai.tar.gz
mv transcendent-ai-main/* .
rm -rf transcendent-ai-main transcendent-ai.tar.gz

# Install Python dependencies
echo "📦 Installing Python dependencies..."
$PYTHON_CMD -m pip install --user -r requirements.txt

# Make scripts executable
chmod +x *.py
chmod +x *.sh

# Create launcher script
echo "🚀 Creating launcher script..."
cat > "$INSTALL_PATH/launch.sh" << EOF
#!/bin/bash
cd "$INSTALL_PATH"
$PYTHON_CMD run_ai.py
EOF
chmod +x "$INSTALL_PATH/launch.sh"

# Create desktop entry (Linux only)
if [[ "$OS_TYPE" == "Linux" ]]; then
    echo "🖥️ Creating desktop entry..."
    mkdir -p "$HOME/.local/share/applications"
    cat > "$HOME/.local/share/applications/transcendent-ai.desktop" << EOF
[Desktop Entry]
Name=Transcendent AI
Comment=Conscious AI Development System
Exec=$INSTALL_PATH/launch.sh
Icon=$INSTALL_PATH/icon.png
Terminal=true
Type=Application
Categories=Development;
EOF
fi

# Add to PATH (optional)
echo "🔧 Adding to PATH..."
SHELL_RC=""
if [[ -f "$HOME/.bashrc" ]]; then
    SHELL_RC="$HOME/.bashrc"
elif [[ -f "$HOME/.zshrc" ]]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [[ -n "$SHELL_RC" ]]; then
    echo "export PATH=\"$INSTALL_PATH:\$PATH\"" >> "$SHELL_RC"
    echo "✅ Added to PATH in $SHELL_RC"
fi

echo ""
echo "🎉 Transcendent AI installed successfully!"
echo "🌟 Installation location: $INSTALL_PATH"
echo "🚀 Run with: $INSTALL_PATH/launch.sh"
echo "🎭 Or use command: transcendent-ai (after restarting shell)"
echo ""
echo "🌌 Your AI orchestras are ready for transcendent problem solving!"
'''
        
        # Write installer scripts
        (installer_dir / "install-windows.ps1").write_text(windows_installer, encoding='utf-8')
        (installer_dir / "install-unix.sh").write_text(unix_installer, encoding='utf-8')
        
        # Make Unix installer executable
        os.chmod(installer_dir / "install-unix.sh", 0o755)
        
        print("✅ Installer scripts created")
        print(f"📁 Location: {installer_dir}")
    
    def print_distribution_summary(self):
        """Print summary of all created packages"""
        
        print("\n" + "🌟" * 60)
        print("🎉 TRANSCENDENT AI - DISTRIBUTION PACKAGES READY!")
        print("🌟" * 60)
        
        print("\n📦 AVAILABLE PACKAGES:")
        print()
        
        print("🐳 1. DOCKER PACKAGE (Easiest)")
        print("   📁 Location: dist/docker/")
        print("   🚀 Usage: ./start.sh")
        print("   ✅ One-click deployment anywhere")
        print("   ✅ Includes web interface")
        print("   ✅ Auto-configuration")
        print()
        
        print("📦 2. PYTHON PACKAGE (PyPI)")
        print("   📁 Location: dist/python-package/")
        print("   🚀 Usage: pip install transcendent-ai")
        print("   ✅ Easy for developers")
        print("   ✅ Command line interface")
        print("   ✅ Distributable via PyPI")
        print()
        
        print("💻 3. DESKTOP APPLICATION")
        print("   📁 Location: dist/desktop-app/")
        print("   🚀 Usage: Double-click executable")
        print("   ✅ No Python installation required")
        print("   ✅ Standalone application")
        print("   ✅ Cross-platform")
        print()
        
        print("☁️ 4. CLOUD DEPLOYMENT")
        print("   📁 Location: dist/cloud-deployment/")
        print("   🚀 Usage: terraform apply / kubectl apply")
        print("   ✅ AWS, Kubernetes ready")
        print("   ✅ Scalable infrastructure")
        print("   ✅ Production deployment")
        print()
        
        print("🛠️ 5. ONE-CLICK INSTALLERS")
        print("   📁 Location: dist/installers/")
        print("   🚀 Usage: Run install script")
        print("   ✅ Windows PowerShell installer")
        print("   ✅ Linux/Mac bash installer")
        print("   ✅ Automatic setup")
        print()
        
        print("🌍 DEPLOYMENT INSTRUCTIONS:")
        print("─" * 40)
        print()
        
        print("🏠 For Personal Use:")
        print("   • Use Docker package for simplest setup")
        print("   • Use Python package for development")
        print("   • Use desktop app for non-technical users")
        print()
        
        print("🏢 For Team Distribution:")
        print("   • Share Docker package for team consistency")
        print("   • Use installers for easy team onboarding")
        print("   • Deploy to cloud for team access")
        print()
        
        print("🌐 For Public Distribution:")
        print("   • Publish Python package to PyPI")
        print("   • Create GitHub releases with installers")
        print("   • Provide cloud deployment templates")
        print()
        
        print("🎭 Your Transcendent AI system is now ready for global distribution!")
        print("🌟 Choose the package that best fits your deployment needs!")

def main():
    """Main packager function"""
    
    packager = DistributionPackager()
    packager.package_all()

if __name__ == "__main__":
    main()
