import hashlib
import datetime as date
import networkx as nx
import matplotlib.pyplot as plt
import json

class Block:
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_string = json.dumps(self.transaction, sort_keys=True)
        block_string = str(self.index) + str(self.timestamp) + transaction_string + self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), {"sender": "SYSTEM", "receiver": "SYSTEM", "amount": 0}, "0")

    def add_transaction(self, sender, receiver, amount):
        last_block = self.chain[-1]
        
        transaction_data = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        
        new_block = Block(index=last_block.index + 1,
                          timestamp=date.datetime.now(),
                          transaction=transaction_data,
                          previous_hash=last_block.hash)
        
        self.chain.append(new_block)

    def print_chain_logs(self):
        print("\n" + "="*50)
        print("BLOCKCHAIN TRANSACTION LEDGER")
        print("="*50 + "\n")

        for block in self.chain:
            t = block.transaction
            print(f" [BLOCK {block.index}] Generated: {block.timestamp}")
            print(f" --------------------------------------------------")
            print(f"  > SENDER   : {t['sender']}")
            print(f"  > RECEIVER : {t['receiver']}")
            print(f"  > AMOUNT   : {t['amount']} Coin")
            print(f"  > PREV HASH: {block.previous_hash[:15]}...") 
            print(f"  > CURR HASH: {block.hash[:15]}...")
            print(f" --------------------------------------------------\n")

def visualize_chain(blockchain):
    G = nx.DiGraph()
    labels = {}
    node_colors = []
    
    print(">> Initializing Graph Theory Model...")
    print(">> Rendering Visualization Window...")
    
    for block in blockchain.chain:
        node_id = f"Block {block.index}"
        G.add_node(node_id)
        
        t = block.transaction
        if block.index == 0:
            summary = "GENESIS"
        else:
            summary = f"{t['sender']}\n↓\n{t['receiver']}\n({t['amount']} BTC)"
            
        label_text = f"ID: {block.index}\n{summary}\nHash: {block.hash[:4]}.."
        labels[node_id] = label_text
        
        if block.index == 0:
            node_colors.append('#FFD700')
        else:
            node_colors.append('#90EE90') 
        
        if block.index > 0:
            prev_id = f"Block {block.index - 1}"
            G.add_edge(prev_id, node_id)

    plt.figure(figsize=(10, 5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=6000, node_color=node_colors, node_shape="s", edgecolors='black')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels, font_size=9)
    plt.title("Blockchain Transaction Graph", fontsize=14)
    plt.axis('off')
    plt.show()

my_chain = Blockchain()

my_chain.add_transaction("Alice", "Bob", 50)
my_chain.add_transaction("Bob", "Charlie", 10)
my_chain.add_transaction("Charlie", "Starbucks", 0.005)
my_chain.add_transaction("Miner_01", "Wallet_A", 12.5)

my_chain.print_chain_logs()

visualize_chain(my_chain)