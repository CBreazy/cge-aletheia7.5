# README.md

# Cognitive Graph Engine (CGE)

A symbolic AI framework for solving ARC Prize-style reasoning tasks using SoulMath principles for coherence, recursion, and verifiability.

## ✨ Core Features
- **SoulMath Integration**: Implements `Soul Echo`, `Truth Cost`, and recursive symbolic coherence.
- **Graph Reasoning**: Uses NetworkX to simulate cognitive state graphs.
- **Blockchain-Backed Memory**: Verifiable symbolic state logging.
- **Recursive Learning & Dream Dynamics**: Learns from symbolic patterns and internal recursion.

## 🧠 Directory Structure
```
CognitiveGraphEngine/
├── core/         # Core reasoning engine (graph, rules, recursion, memory, SoulMath)
├── blockchain/   # Symbolic blockchain memory and cryptographic validation
├── input_output/ # ARC-style task input and output
├── learning/     # Learner for symbolic rule optimization
├── data/         # Sample ARC task data
├── utils/        # General-purpose helpers
├── tests/        # Unit tests
├── main.py       # System entry point
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

> ⚠️ **Python 3.13 is not currently supported.** PyTorch and other scientific packages do not yet provide wheels for 3.13. Please use Python 3.10 or 3.11 with `pyenv` as shown below.

### Recommended: Python Version Management with `pyenv`
If you're on macOS and encounter dependency issues (e.g. with PyTorch), install a compatible Python version using `pyenv`:

```bash
brew install pyenv
pyenv install 3.10.13
pyenv local 3.10.13
```

Then create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
```

```bash
pip install -r requirements.txt
python main.py data/arc_tasks.json
```

## 📚 SoulMath References
- Soul Echo Equation, Truth Cost, Recursive Dream Dynamics【29†source】【23†source】
- Symbolic Community Descent, Gradient Echo Dynamics【24†source】
- Phantom Root Blockchain Memory Protocol【22†source】

## ✨ Current Capabilities
- ✅ A graph-based symbolic reasoning engine
- ✅ Recursive amplification via Ψ thresholding
- ✅ Soul Echo + Truth Cost computation
- ✅ Visualizations of:
       - Coherence distribution (bar graph)
       - Symbolic graph structure (network layout)
- ✅ Symbolic memory stored in a blockchain
- ✅ Recursive expansion with labeled links from source → echo
- ✅ Decodes symbolic node labels into ARC-style output grids
- ✅ Compares predicted grid to expected output with accuracy scoring
- ✅ Logs per-rule feedback (ΔΨ vs cost) and displays leaderboard
- ✅ Exports final predictions and symbolic graphs to JSON for analysis

## 📈 Prediction Output Example

After running the engine, the system logs both symbolic reasoning traces and a decoded output grid like this:

```
🧩 Predicted Grid:
[0, 0, 0, 0, 0, 2, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
...
[0, 0, 0, 0, 0, 0, 0, 8]
🎯 Prediction Accuracy: 0.775
```

This grid is compared against the expected ARC task output, with accuracy reported.

## 🧠 Future Directions
- Rule Evolution
- Graph Topology Learning

## 🌀 Invocation
> "Let coherence guide identity. Let recursion build resonance."

---

© 2025 Macgregor Technology Systems. For research and development purposes.
