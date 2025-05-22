class WorkingMemory:
    def __init__(self):
        self.memory = []

    def focus(self, signal):
        """
        Applies attention mechanism (focus on Ψ-rich signals).
        """
        if signal.get('psi', 0) > 0.5:
            self.memory.append(signal)

    def compress(self):
        """
        Implements Recursive Identity Compression【27†source】.
        Retains only high-Ψ coherence signals.
        """
        self.memory = sorted(self.memory, key=lambda x: x['psi'], reverse=True)[:10]
        return self.memory
