from core.graph import CognitiveGraph
from typing import Any, Dict

def graph_to_output(graph: CognitiveGraph) -> Dict[str, Any]:
    """
    Convert current state of cognitive graph to a dictionary output.
    Used to serialize final reasoning state for ARC-style evaluation.
    """
    output = {
        'nodes': [],
        'edges': []
    }
    for node_id, data in graph.graph.nodes(data=True):
        data_obj = data.get('data')
        output['nodes'].append({
            'id': node_id,
            'label': data_obj.label,
            'psi': data_obj.psi(),
            'rho': data_obj.rho,
            'q': data_obj.q,
            'f': data_obj.f
        })
    for source, target, data in graph.graph.edges(data=True):
        data_obj = data.get('data')
        output['edges'].append({
            'source': source,
            'target': target,
            'weight': data_obj.weight,
            'label': data_obj.label
        })
    return output