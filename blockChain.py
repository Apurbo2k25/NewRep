import hashlib
import time

# Step 1: Define the Block
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # For proof of work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Step 2: Define the Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Proof-of-Work difficulty level

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = len(self.chain)
        new_block = Block(new_index, data, previous_block.hash)
        # Mine the block
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Step 3: Display the Blockchain
def display_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Block {block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Nonce: {block.nonce}")
        print("-" * 40)

# Step 4: Test the Blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block("Transaction 1: Alice pays Bob 10 BTC")
    my_blockchain.add_block("Transaction 2: Bob pays Charlie 5 BTC")
    my_blockchain.add_block("Transaction 3: Charlie pays Dave 2 BTC")
    display_blockchain(my_blockchain)
