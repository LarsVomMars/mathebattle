# CLI for the tool - yay
import os
import sys
from importlib import import_module

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
    solver.autosolve()
else:
    solver.cli()
