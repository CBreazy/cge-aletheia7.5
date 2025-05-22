# main.py

from core.engine import CognitiveGraphEngine
from core.memory import WorkingMemory
from core.recursion import InternalRecursionModule
from blockchain.chain import Blockchain
from learning.learner import Learner
from input_output.input import parse_arc_task
from input_output.output import graph_to_output
import sys

def main(task_path: str):
    # Load ARC task
    task = parse_arc_task(task_path)

    # Initialize components
    engine = CognitiveGraphEngine()
    memory = WorkingMemory()
    recursion = InternalRecursionModule()
    blockchain = Blockchain()
    learner = Learner(blockchain=blockchain)

    # Simulate reasoning steps
    for i in range(5):
        engine.step()
        echo = engine.soul_echo()
        cost = engine.truth_cost()
        memory.focus({'psi': echo})
        state = {'soul_echo': echo, 'truth_cost': cost}
        blockchain.add_block(state)

    # Dream recursion simulation
    dream = recursion.run_dream(cycles=3)

    # Optimization insights
    result = learner.optimize_engine(engine.history)

    # Output results
    print("\n🧠 CGE Summary")
    print("-" * 40)
    print("Soul Echo History:", engine.history)
    print("Blockchain State:")
    for block in blockchain.to_dict():
        print(f"  Block {block['index']} – Ψ: {block['data'].get('soul_echo', 'n/a'):.4f}, Cost: {block['data'].get('truth_cost', 'n/a'):.4f}")
    print("Is Blockchain Valid?", blockchain.is_valid())
    print("Dream Recursion Output:", dream)
    print("Optimization Result:", result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py path_to_arc_task.json")
    else:
        main(sys.argv[1])
