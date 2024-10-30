import hashlib
import datetime
import random
from ex2 import BlockPoW
import time
class Validator:
    def __init__(self, address, stake=0):
        self.address = address
        self.stake = stake

    def add_stake(self, amount):
        self.stake += amount

class BlockPoS:
    def __init__(self, data: str, previous_hash: str, validator: Validator):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.validator = validator.address
        self.hash = self.calcul_hash()
        
    def calcul_hash(self) -> str:
        return hashlib.sha256(
            str(self.data).encode("utf-8") +
            str(self.previous_hash).encode("utf-8") +
            str(self.timestamp).encode("utf-8") +
            str(self.validator).encode("utf-8")
        ).hexdigest()

def select_validator(validators):
    total_stake = sum(v.stake for v in validators)
    if total_stake == 0:
        raise ValueError("Total stake must be greater than zero.")
    
    # Probability-based selection weighted by stake
    weights = [v.stake / total_stake for v in validators]
    selected_validator = random.choices(validators, weights=weights, k=1)[0]
    return selected_validator

if __name__ == "__main__":
    # Set up the validators for Proof of Stake
    validators = [Validator("Validator1", 10),
                  Validator("Validator2", 20),
                  Validator("Validator3", 30)]

    # Test data and previous hash
    data = "This is a block of data."
    previous_hash = "0" * 64  # Example previous hash

    # Measure execution time for Proof of Stake
    start_time_pos = time.time()
    selected_validator = select_validator(validators)
    block_pos = BlockPoS(data, previous_hash, selected_validator)
    end_time_pos = time.time()
    time_pos = end_time_pos - start_time_pos

    print("Proof of Stake:")
    print(f"Selected Validator: {selected_validator.address}")
    print(f"Block Hash: {block_pos.hash}")
    print(f"Execution Time: {time_pos:.6f} seconds")

    # Measure execution time for Proof of Work
    difficulty = 3  # Set the difficulty
    block_pow = BlockPoW(data, previous_hash)

    start_time_pow = time.time()
    mined_hash = block_pow.mine_block(difficulty)
    end_time_pow = time.time()
    time_pow = end_time_pow - start_time_pow

    print("\nProof of Work:")
    print(f"Block Hash: {mined_hash}")
    print(f"Execution Time: {time_pow:.6f} seconds")

    # Compare execution times
    print("\nComparison:")
    if time_pow > time_pos:
        print(f"Proof of Stake is faster by {time_pow - time_pos:.6f} seconds.")
    else:
        print(f"Proof of Work is faster by {time_pos - time_pow:.6f} seconds.")