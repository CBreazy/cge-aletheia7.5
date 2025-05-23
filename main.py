# main.py

from core.engine import CognitiveGraphEngine
from core.memory import WorkingMemory
from core.recursion import InternalRecursionModule
from blockchain.chain import Blockchain
from learning.learner import Learner
from input_output.input import parse_arc_task
from input_output.output import graph_to_output
from core.graph import Node
import sys

def build_graph_from_grid(engine, grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != 0:
                # Assign memory density, emotion, frequency heuristically
                rho = 0.9
                q = val / 9.0
                f = (x + 1) / (len(row) + 1)
                label = f"({x},{y})={val}"
                node = Node(label=label, rho=rho, q=q, f=f)
                engine.graph.add_node(node)

def main(task_path: str):
    # Load ARC task
    task = parse_arc_task(task_path)

    # Initialize components
    engine = CognitiveGraphEngine()
    memory = WorkingMemory()
    recursion = InternalRecursionModule()
    blockchain = Blockchain()
    learner = Learner(blockchain=blockchain)

    # Build symbolic graph from first training input
    first_grid = task['train'][0]['input']
    build_graph_from_grid(engine, first_grid)

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

    # 🔍 Debug: show node labels used in prediction
    print("\n🧩 Graph Node Labels for Grid Prediction")
    for _, wrapper in engine.graph.graph.nodes(data=True):
        node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
        print("Label:", getattr(node, 'label', '???'))

    # Visualize symbolic coherence across graph
    engine.visualize_psi_distribution()
    engine.visualize_graph_layout()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py path_to_arc_task.json")
    else:
        main(sys.argv[1])
