# core/engine.py

from core.graph import CognitiveGraph, Node, Edge
from core.rules import rule_registry
from typing import Any
import matplotlib.pyplot as plt

import networkx as nx
import re

import json
import os

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

        feedback_log = []
        baseline_psi = self.graph.soulmath_graph_identity()

        for rule in rule_registry:
            if rule.is_applicable(symbolic_state):
                symbolic_state = rule.apply_rule(symbolic_state)
                new_psi = self.graph.soulmath_graph_identity()
                delta_psi = new_psi - baseline_psi
                feedback_log.append({
                    'rule': rule.name,
                    'delta_psi': delta_psi,
                    'cost': rule.cost
                })
                baseline_psi = new_psi

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
                print("-- Rule Feedback Log --")
        for entry in feedback_log:
            print(f"[Feedback] {entry['rule']} → ΔΨ: {entry['delta_psi']:.6f} | cost: {entry['cost']}")

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

    def predict_grid_from_graph(self):
        """
        Synthesize a 2D grid prediction from symbolic node labels in the graph.
        Assumes node labels are in the format: (x,y)=val
        """
        coords = []
        values = []
        for _, wrapper in self.graph.graph.nodes(data=True):
            node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            label = getattr(node, 'label', '')
            print("Checking label:", label)
            match = re.match(r"^\((\d+),(\d+)\)=([\d.]+)$", label)
            if match:
                print(f"  ↳ MATCHED → x={match.group(1)}, y={match.group(2)}, val={match.group(3)}")

            if match:
                x, y = int(match.group(1)), int(match.group(2))
                val = float(match.group(3))
                coords.append((x, y))
                values.append(val)

        if not coords:
            return []

        max_x = max(x for x, _ in coords) + 1
        max_y = max(y for _, y in coords) + 1
        grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

        for (x, y), val in zip(coords, values):
            grid[y][x] = val

        return grid


    def export_graph_snapshot(self, path: str):
        """
        Export the cognitive graph to a JSON file with full node and edge data.
        """
        nodes = []
        edges = []
        for node_id, wrapper in self.graph.graph.nodes(data=True):
            node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            nodes.append({
                'id': node.id,
                'label': node.label,
                'rho': node.rho,
                'q': node.q,
                'f': node.f,
                'psi': node.psi()
            })
        for u, v, wrapper in self.graph.graph.edges(data=True):
            edge = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            edges.append({
                'source': u,
                'target': v,
                'label': edge.label,
                'weight': edge.weight
            })
        snapshot = {'nodes': nodes, 'edges': edges}
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(snapshot, f, indent=2)
        print(f"✅ Graph snapshot exported to {path}")

    def visualize_graph_layout(self):
        """
        Visualize the full symbolic graph with nodes and edges using networkx spring layout.
        Echo nodes are colored differently.
        """
        G = self.graph.graph
        pos = nx.spring_layout(G)
        node_colors = []
        node_labels = {}

        for node_id, wrapper in G.nodes(data=True):
            node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
            label = getattr(node, 'label', '<?>')
            node_labels[node_id] = label
            if '_amp' in label:
                node_colors.append('orange')
            else:
                node_colors.append('lightblue')

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors, node_size=700, font_size=8, edge_color='gray')
        plt.title("Symbolic Graph Layout")
        plt.tight_layout()
        plt.show()
