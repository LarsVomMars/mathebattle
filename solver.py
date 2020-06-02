# CLI for the tool - yay
import os
import sys
from importlib import import_module
import asyncio
from dotenv import load_dotenv

os.environ["MB_HEADLESS"] = '--headless' in sys.argv  # Production mode - Run browser headless

while True:
    battle_id = input("Battle: ")
    task_id = input("Task: ")
    auto_solver = input("Autosolver (y/N): ")

    try:
        solver = import_module(f"battles.b{battle_id}.t{task_id}").Solver
        break
    except ModuleNotFoundError as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(e)
        print(f"Battle {battle_id}|{task_id} not found - Retry!")
    except Exception as e:
        print(e)
        sys.exit(1)

if auto_solver.lower() == "y":
    load_dotenv()
    asyncio.get_event_loop().run_until_complete(solver.autosolve())
else:
    solver.cli()
