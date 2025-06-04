#!/usr/bin/env python3
# Simple run script for Practical AI System

import asyncio
import os

def load_env():
    env_file = '.env'
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

async def main():
    print('Starting Practical AI System...')
    load_env()
    
    # Import and run the demo
    from practical_ai_system import run_practical_ai_demo
    await run_practical_ai_demo()

if __name__ == '__main__':
    asyncio.run(main())
