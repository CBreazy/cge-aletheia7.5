import hashlib
import json
import time
from typing import Any, Dict, Optional

class Block:
    def __init__(self, index: int, previous_hash: str, data: Dict[str, Any], timestamp: Optional[float] = None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data  # SoulMath state snapshot
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        SoulMath-integrated hash using SHA-256 over essential symbolic fields【22†source】【29†source】
        """
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
