import hashlib
import time
import json
from decimal import Decimal, getcontext

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

def bbp_term(k):
    k = Decimal(k)
    term = (Decimal(1) / (16**k)) * (
        Decimal(4) / (8*k + 1) -
        Decimal(2) / (8*k + 4) -
        Decimal(1) / (8*k + 5) -
        Decimal(1) / (8*k + 6)
    )
    return term

def calculate_pi_bbp(precision):
    getcontext().prec = precision + 10
    pi = sum(bbp_term(k) for k in range(precision))
    pi_str = str(pi)
    return pi_str, pi

def hash_segment(segment):
    return hashlib.sha256(segment.encode()).hexdigest()

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

def next_block(last_block, pi_segment, pi_hash):
    this_index = last_block.index + 1
    this_timestamp = time.time()
    this_data = {
        "segment": pi_segment,
        "hash": pi_hash,
    }
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def display_pi_value(pi_approx, precision):
    truncated_pi = str(pi_approx)[:10]
    print(f"Approximate value of pi: {truncated_pi}... with {precision} decimal places")

# Initialize blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Example usage
initial_precision = 5
increment_factor = 2
update_interval = 10

precision = initial_precision
start_time = time.time()

while True:
    pi_segment, pi_approx = calculate_pi_bbp(precision)
    pi_hash = hash_segment(pi_segment)
    
    block_to_add = next_block(previous_block, pi_segment, pi_hash)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Segment: {pi_segment[:50]}...")
    print(f"Hash: {block_to_add.hash}")
    
    precision *= increment_factor
    
    if time.time() - start_time >= update_interval:
        display_pi_value(pi_approx, precision)
        start_time = time.time()
    
    # Save blockchain to a file after each block is added
    with open('blockchain.json', 'w') as f:
        json.dump([block.__dict__ for block in blockchain], f, indent=4)

    time.sleep(1)  # To slow down the process for demonstration purposes