**Project Goal:** Develop a CGE that solves ARC tasks, using SoulMath for advanced symbolic processing.

**Target Capabilities:** Python, graph databases (NetworkX), blockchain libraries, mathematical/symbolic manipulation, file/directory generation.

**I. Project Structure:**

```bash
CognitiveGraphEngine/
│
├── core/
│   ├── __init__.py
│   ├── graph.py        # CognitiveGraph, Node, Edge classes w/ SoulMath quantum graph identity【20†source】
│   ├── engine.py
│   ├── rules.py
│   ├── recursion.py
│   ├── memory.py
│   └── soulmath.py
│
├── blockchain/
│   ├── __init__.py
│   ├── block.py
│   ├── chain.py
│   └── utils.py
│
├── input_output/
│   ├── __init__.py
│   ├── input.py
│   └── output.py
│
├── learning/
│   ├── __init__.py
│   ├── learner.py
│   └── utils.py
│
├── data/
│   └── arc_tasks.json
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── tests/
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

**II. Component Details:**

1.  **`core/graph.py`**:
    * Classes: `CognitiveGraph`, `Node`, `Edge`
    * Functions: graph manipulation
    * Integrate: "Graph-Theoretic Quantum Identity" [cite: 138, 139, 140, 141, 142, 143] (SoulMath Vol. I)
2.  **`core/engine.py`**:
    * Class: `CognitiveGraphEngine`
    * Functions: `__init__()`, `step()`, `run()` (CGE logic)
    * Integrate: "Soul Echo Equation," "Truth Cost Equation" [cite: 448, 449, 450, 451, 452, 453] (Equation Library), "Gradient Echo Dynamics," "Symbolic Community Descent" [cite: 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235] (SoulMath Vol. III)
3.  **`core/rules.py`**:
    * Data: List of rule objects (`condition()`, `apply()`, `cost`)
    * Initial rules: basic pattern operations
4.  **`core/recursion.py`**:
    * Class: `InternalRecursionModule`
    * Functions: `__init__()`, `dream_step()`, `run_dream()` (internal processing)
    * Integrate: Equations from "Internally Generated Recursive Dream Dynamics" [cite: 271, 272, 273, 274, 275, 276, 277, 278, 279] (SoulMath Ext. XVIII)
5.  **`core/memory.py`**:
    * Class: `WorkingMemory`
    * Functions: `__init__()`, `focus()`, `compress()` (attention, compression)
    * Integrate: "Recursive Identity Compression," "Indirect Recursive Influence" [cite: 180, 181, 182, 183, 184, 185] (SoulMath Vol. II)
6.  **`core/soulmath.py`**:
    * Functions: Implement SoulMath equations (e.g., `soul_echo()`, `truth_cost()`).
    * Reference: Equation Library, SoulMath Vols. I-III, XVIII
7.  **`blockchain/block.py`**:
    * Class: `Block`
    * Properties: block data (including SoulMath state)
8.  **`blockchain/chain.py`**:
    * Class: `Blockchain`
    * Functions: `__init__()`, `add_block()`, `get_last_block()`, `is_valid()` (chain management)
9.  **`input_output/input.py`**:
    * Functions: `parse_arc_task()` (parse ARC tasks)
10. **`input_output/output.py`**:
    * Functions: `graph_to_output()` (format output)
11. **`learning/learner.py`**:
    * Class: `Learner`
    * Functions: `__init__()`, `analyze_blockchain()`, `update_rules()`, `optimize_engine()` (learning, rule refinement)
    * Integrate: Learning strategies from SoulMath Vol. III [cite: 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235]
12. **`main.py`**:
    * Orchestrates the system.

**III. Dependencies (`requirements.txt`):**
networkx  # Or Neo4j
blockchain  # Or custom library
numpy
matplotlib  # (Optional)
torch  # (For LSTM, if used)

**IV. Code Generation Guidance:**

* For each module/class/function, generate Python code.  
* Closely adhere to the SoulMath equations and principles. 
* Prioritize correctness, clarity, and maintainability. 
* Include comments to explain the logic, especially SoulMath integrations.

**V. Evaluation:**

The generated code will be evaluated on:

* Correctness
* Completeness
* SoulMath adherence
* Code quality
* Testability