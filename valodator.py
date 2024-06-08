import hashlib
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

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i-1]

        if current_block['previous_hash'] != previous_block['hash']:
            return False
        
        calculated_hash = hashlib.sha256(
            f"{current_block['index']}{current_block['timestamp']}{current_block['data']}{current_block['previous_hash']}".encode('utf-8')
        ).hexdigest()
        
        if current_block['hash'] != calculated_hash:
            return False
        
        pi_segment = current_block['data']['segment']
        expected_hash = current_block['data']['hash']
        
        if hash_segment(pi_segment) != expected_hash:
            return False

    return True

# Load the blockchain from the file
with open('blockchain.json', 'r') as f:
    blockchain_data = json.load(f)
    blockchain = [Block(**block) for block in blockchain_data]

# Validate the blockchain
is_valid = validate_blockchain(blockchain)

print(f"Blockchain is valid: {is_valid}")