# core/rules.py

from typing import Callable, Dict, List, Any

class Rule:
    def __init__(self, name: str, condition: Callable[[Dict], bool], apply: Callable[[Dict], Dict], cost: float):
        self.name = name
        self.condition = condition
        self.apply = apply
        self.cost = cost

    def is_applicable(self, state: Dict) -> bool:
        return self.condition(state)

    def apply_rule(self, state: Dict) -> Dict:
        print(f"[Rule Applied] {self.name}")
        updated = self.apply(state)
        if 'amplified' in updated:
            print(f"  Amplified Nodes: {updated['amplified']}")
        return updated

# Example symbolic pattern operation rules (initial set)
def basic_condition(state: Dict) -> bool:
    return 'pattern' in state and len(state['pattern']) > 0

def basic_apply(state: Dict) -> Dict:
    pattern = state.get('pattern', [])
    state['pattern_mirrored'] = pattern[::-1]
    return state

basic_rule = Rule(
    name="Mirror Pattern",
    condition=basic_condition,
    apply=basic_apply,
    cost=0.1
)

# Advanced rule: amplify nodes with symbolic coherence (Ψ) above a threshold

def psi_threshold_condition(state: Dict) -> bool:
    return 'pattern' in state and len(state['pattern']) > 0

def psi_threshold_apply(state: Dict) -> Dict:
    amplified = []
    for wrapper in state['pattern']:
        node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
        if hasattr(node, 'psi') and callable(node.psi):
            psi_value = node.psi()
            if isinstance(psi_value, (int, float)) and psi_value > 0.001:
                amplified.append(f"{node.label}_amp")
    state['amplified'] = amplified
    return state

psi_amplifier_rule = Rule(
    name="PsiThresholdAmplifier",
    condition=psi_threshold_condition,
    apply=psi_threshold_apply,
    cost=0.2
)

# ΨDeltaAmplifier: amplify only if Ψ increased from previous step
psi_memory = {}

def psi_delta_condition(state: Dict) -> bool:
    return 'pattern' in state and len(state['pattern']) > 0

def psi_delta_apply(state: Dict) -> Dict:
    amplified = []
    for wrapper in state['pattern']:
        node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
        if hasattr(node, 'psi') and callable(node.psi):
            current_psi = node.psi()
            last_psi = psi_memory.get(node.id, 0)
            if current_psi > last_psi:
                amplified.append(f"{node.label}_amp")
            psi_memory[node.id] = current_psi
    state['amplified'] = amplified
    return state

psi_delta_rule = Rule(
    name="PsiDeltaAmplifier",
    condition=psi_delta_condition,
    apply=psi_delta_apply,
    cost=0.3
)

# ΨDecayPruner: remove nodes with Ψ below a threshold

def psi_decay_condition(state: Dict) -> bool:
    return 'graph' in state and hasattr(state['graph'], 'graph')

def psi_decay_apply(state: Dict) -> Dict:
    graph = state['graph'].graph
    low_psi_nodes = []
    for node_id, wrapper in graph.nodes(data=True):
        node = wrapper.get('data') if isinstance(wrapper, dict) and 'data' in wrapper else wrapper
        if hasattr(node, 'psi') and callable(node.psi):
            if node.psi() < 0.01:
                low_psi_nodes.append(node_id)

    graph.remove_nodes_from(low_psi_nodes)
    if low_psi_nodes:
        print(f"  Pruned Nodes: {low_psi_nodes}")
    return state

psi_prune_rule = Rule(
    name="PsiDecayPruner",
    condition=psi_decay_condition,
    apply=psi_decay_apply,
    cost=0.1
)

# Topology-Aware Rule: Fan-Out Detector

def fanout_condition(state: Dict) -> bool:
    return 'graph' in state and hasattr(state['graph'], 'graph')

def fanout_apply(state: Dict) -> Dict:
    G = state['graph'].graph
    fanouts = {}
    for node_id in G.nodes():
        out_degree = G.out_degree(node_id)
        if out_degree > 0:
            fanouts[node_id] = out_degree
    if fanouts:
        print("  Fan-Outs:", fanouts)
    return state

fanout_rule = Rule(
    name="SymbolicFanoutTracker",
    condition=fanout_condition,
    apply=fanout_apply,
    cost=0.05
)

# Rule Registry
rule_registry: List[Rule] = [
    fanout_rule,
    psi_prune_rule,
    psi_delta_rule,
    basic_rule,
    psi_amplifier_rule,
]
