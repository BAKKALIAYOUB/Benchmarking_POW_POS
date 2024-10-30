import time 
from PoS import Validator, BlockPoS, select_validator
from PoW import BlockPoW



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
    print(f"Block Hash: {block_pos.get_hash()}")
    print(f"Execution Time: {time_pos:.6f} seconds")

    # Measure execution time for Proof of Work
    difficulty = 5  # Set the difficulty
    block_pow = BlockPoW(data, previous_hash)

    start_time_pow = time.time()
    mined_hash = block_pow.mine_block(difficulty)
    end_time_pow = time.time()
    time_pow = end_time_pow - start_time_pow

    print("\nProof of Work:")
    print(f"Block Hash: {block_pos.get_hash()}")
    print(f"Execution Time: {time_pow:.6f} seconds")

    # Compare execution times
    print("\nComparison:")
    if time_pow > time_pos:
        print(f"Proof of Stake is faster by {time_pow - time_pos:.6f} seconds.")
    else:
        print(f"Proof of Work is faster by {time_pos - time_pow:.6f} seconds.")