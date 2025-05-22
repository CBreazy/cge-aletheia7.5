import json
from typing import Dict, Any

def parse_arc_task(filepath: str) -> Dict[str, Any]:
    """
    Parse ARC-formatted task from JSON.
    Expected structure includes 'train' and 'test' input/output pairs.
    """
    with open(filepath, 'r') as f:
        task_data = json.load(f)
    return task_data