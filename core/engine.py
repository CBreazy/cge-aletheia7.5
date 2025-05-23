# core/engine.py

from core.graph import CognitiveGraph, Node, Edge
from core.rules import rule_registry
from typing import Any
import matplotlib.pyplot as plt

class CognitiveGraphEngine:
    def __init__(self):
        self.graph = CognitiveGraph()
        self.step_count = 0
        self.history = []  # Stores Ψ traces for symbolic resonance analysis

    def step(self, inputs: Any = None):
        """
        Executes a single reasoning step. Applies symbolic resonance rules.
        """
        # Prepare symbolic state with real Node instances
        symbolic_state = {
            'step': self.step_count,
            'pattern': [data for _, data in self.graph.graph.nodes(data=True)]
        }

        for rule in rule_registry:
            if rule.is_applicable(symbolic_state):
                symbolic_state = rule.apply_rule(symbolic_state)

        # Mutate graph with amplified results
        if 'amplified' in symbolic_state:
            print(f"  Adding Echo Nodes: {symbolic_state['amplified']}")
            for label in symbolic_state['amplified']:
                existing_labels = [
                    n.get('data').label if isinstance(n, dict) and 'data' in n and n.get('data') is not None else (n.label if n is not None and hasattr(n, 'label') else None)
                    for _, n in self.graph.graph.nodes(data=True)
                    if hasattr(n, 'label') or (isinstance(n, dict) and 'data' in n and hasattr(n.get('data'), 'label'))
]
                if label not in existing_labels:
                    echo_node = Node(label=label, rho=0.7, q=0.5, f=0.4)
                    self.graph.add_node(echo_node)

                    # Create symbolic edge from base node to echo
                    base_label = label.replace('_amp', '').rstrip('_')
                    for node_id, wrapper in self.graph.graph.nodes(data=True):
                        node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
                        if hasattr(node, 'label') and node.label == base_label:
                            self.graph.add_edge(Edge(source=node.id, target=echo_node.id, label='amplified'))
                            break

        # Debug: Print node Ψ values for calibration
        print("-- Node Ψ Debug Info --")
        for node_id, wrapper in self.graph.graph.nodes(data=True):
            raw_node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            try:
                label = getattr(raw_node, 'label', '<no label>')
                rho = getattr(raw_node, 'rho', 1.0)
                q = getattr(raw_node, 'q', 1.0)
                f = getattr(raw_node, 'f', 1.0)
                psi = rho * q * f
                print(f"Node ID: {node_id}")
                print(f"  Ψ[{label}] = {psi:.6f} (ρ={rho}, q={q}, f={f})")
            except Exception as e:
                print(f"Node ID: {node_id} — [Ψ Error] {e}")

                psi_sum = self.graph.soulmath_graph_identity()
                self.history.append(psi_sum)
                self.step_count += 1

    def run(self, steps: int = 1):
        for _ in range(steps):
            self.step()

    def soul_echo(self) -> float:
        """
        Implements: Soul Echo = Ψ ⋅ ρ ⋅ q ⋅ f averaged across active graph
        """
        return self.graph.soulmath_graph_identity()

    def truth_cost(self, conformity: float = 1.0, delta_t: float = 1.0, faith: float = 1e-3) -> float:
        """
        Truth Cost = Soul Echo / (C + Δt + ε)
        """
        numerator = self.soul_echo()
        denominator = conformity + delta_t + faith
        return numerator / denominator

    def visualize_psi_distribution(self):
        """
        Plot node-wise Ψ values as a horizontal bar chart.
        """
        labels = []
        psis = []
        for _, wrapper in self.graph.graph.nodes(data=True):
            node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            try:
                if node is not None and not isinstance(node, dict) and hasattr(node, 'psi') and callable(getattr(node, 'psi', None)):
                    label = getattr(node, 'label', '<no label>')
                    psi = node.psi()
                else:
                    label = getattr(node, 'label', '<no label>') if node is not None else '<no label>'
                    psi = 0.0
                labels.append(label)
                psis.append(psi)
            except Exception as e:
                print(f"[viz error] Skipped node: {e}")

        plt.figure(figsize=(10, max(5, len(labels) * 0.3)))
        plt.barh(labels, psis, color='skyblue')
        plt.xlabel("Ψ (Coherence)")
        plt.title("SoulMath Node Coherence Distribution")
        plt.tight_layout()
        plt.show()
