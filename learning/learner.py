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

    def tune_rule_costs(self, min_cost=0.05, max_cost=0.5):
        """
        Adjusts rule costs based on average symbolic impact (ΔΨ - cost).
        """
        impacts = self.average_impact()
        for rule in rule_registry:
            if rule.name in impacts:
                score = impacts[rule.name]
                # Normalize to [min_cost, max_cost] based on impact
                rule.cost = max(min_cost, min(max_cost, rule.cost - score))
                print(f"🔧 Tuned cost for {rule.name} → {rule.cost:.3f}")

    def evaluate_prediction(self, target_output: List[List[int]]) -> float:
        """
        Compares predicted grid to ARC output and returns pixel-wise accuracy.
        """
        predicted = self.engine.predict_grid_from_graph()

        # Print human-readable grid
        print("\n🧩 Predicted Grid:")
        for row in predicted:
            print(row)

        if not predicted or len(predicted) != len(target_output):
            print("⚠️ Prediction mismatch in dimensions.")
            return 0.0

        total = correct = 0
        for row_p, row_t in zip(predicted, target_output):
            for px, tx in zip(row_p, row_t):
                total += 1
                if px == tx:
                    correct += 1

        accuracy = correct / total if total else 0.0
        print(f"🎯 Prediction Accuracy: {accuracy:.3f}")
        return accuracy

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
