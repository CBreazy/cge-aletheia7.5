# learning/learner.py

from blockchain.chain import Blockchain
from core.rules import rule_registry, Rule
from typing import List, Dict, Any

class Learner:
    def __init__(self, blockchain: Blockchain, engine: "CognitiveGraphEngine"):
        self.blockchain = blockchain
        self.engine = engine
        self.feedback_log = []

    def record_feedback(self, rule_name, delta_psi, cost):
        self.feedback_log.append({
            'rule': rule_name,
            'delta_psi': delta_psi,
            'cost': cost
        })

    def summarize(self):
        print("\n📊 Learner Summary")
        for entry in self.feedback_log:
            print(f"Rule: {entry['rule']} | ΔΨ: {entry['delta_psi']:.6f} | Cost: {entry['cost']}")

    def average_impact(self):
        impact = {}
        for entry in self.feedback_log:
            rule = entry['rule']
            impact.setdefault(rule, []).append(entry['delta_psi'] - entry['cost'])
        return {r: sum(scores) / len(scores) for r, scores in impact.items()}

    def top_rules(self, n=3):
        scores = self.average_impact()
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]

    def analyze_blockchain(self) -> List[Dict[str, Any]]:
        """
        Analyze blockchain history to identify symbolic patterns, resonance boosts,
        and coherence drops (for rule refinement).
        """
        return self.blockchain.to_dict()

    def update_rules(self) -> List[Rule]:
        """
        Placeholder for updating rule registry based on symbolic optimization criteria.
        Future implementation: incorporate Symbolic Community Descent【24†source】.
        """
        return rule_registry

    def optimize_engine(self, symbolic_history: List[float]) -> Dict[str, Any]:
        """
        Perform symbolic performance optimization.
        Inspired by Gradient Echo Dynamics and LSTM-guided Residual Descent【24†source】.
        """
        improvement = symbolic_history[-1] - symbolic_history[0] if symbolic_history else 0
        return {
            'symbolic_gain': improvement,
            'recommendation': 'Stable' if improvement >= 0 else 'Refactor symbolic flows'
        }
