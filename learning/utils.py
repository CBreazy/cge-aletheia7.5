from typing import List

def moving_average(data: List[float], window_size: int = 3) -> List[float]:
    """
    Compute moving average over a time-series (used for coherence trend analysis).
    """
    if len(data) < window_size:
        return data
    return [sum(data[i:i+window_size])/window_size for i in range(len(data) - window_size + 1)]