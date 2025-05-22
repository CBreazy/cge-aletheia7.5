from blockchain.block import Block
from typing import List, Dict, Any

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_data = {"message": "Genesis Block", "soul_echo": 0.0, "truth_cost": 0.0}
        genesis_block = Block(index=0, previous_hash="0", data=genesis_data)
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]) -> Block:
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            previous_hash=last_block.hash,
            data=data
        )
        self.chain.append(new_block)
        return new_block

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def to_dict(self) -> List[Dict[str, Any]]:
        return [block.to_dict() for block in self.chain]
