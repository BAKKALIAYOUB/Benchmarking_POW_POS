# Proof of Stake vs Proof of Work

This project demonstrates and compares the two popular blockchain consensus mechanisms: **Proof of Stake (PoS)** and **Proof of Work (PoW)**. The implementation is done in Python, showcasing how each mechanism processes transactions and creates blocks.

## Overview

- **Proof of Work (PoW)**: Miners solve a computational puzzle to create a new block. This method requires significant computational power and energy.
- **Proof of Stake (PoS)**: Validators are chosen to create new blocks based on their stake (amount of cryptocurrency they hold). This approach is more energy-efficient and faster than PoW.

## Features

- Implementation of both PoS and PoW consensus mechanisms.
- Measurement of execution time for block creation in both methods.
- Random selection of validators based on stake for PoS.
- Iterative mining process for PoW to find a valid hash.

## Output Example

With Difficulty of 5 we have the following result:

```
Proof of Stake:
Selected Validator: Validator3
Block Hash: ebbcc1f78384bd46c432933a79a52c831d59148523ddd172ae2d7c669d350f5b
Execution Time: 0.000073 seconds
Block mined: 0000007a3f3ff8054fa4478cf8b7b845988eb9f8a8cc4007bd6251bb7184ed9e

Proof of Work:
Block Hash: ebbcc1f78384bd46c432933a79a52c831d59148523ddd172ae2d7c669d350f5b
Execution Time: 7.918883 seconds

Comparison:
Proof of Stake is faster by 7.918810 seconds.
```
