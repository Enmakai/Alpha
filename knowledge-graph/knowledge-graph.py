# /Applications/anaconda3/envs/alpha0.1/bin/python "/Users/yogesh-11389/MachineLearning/Private/Repository/Alpha/knowledge-graph/knowledge-graph.py" 

import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes (stocks, sectors)
G.add_node("Technology", type="Sector")
G.add_node("AAPL", type="Stock")
G.add_node("MSFT", type="Stock")
G.add_node("Finance", type="Sector")
G.add_node("JPM", type="Stock")
G.add_node("Gold", type="Commodity")

# Add edges (relationships)
G.add_edge("Technology", "AAPL")
G.add_edge("Technology", "MSFT")
G.add_edge("Finance", "JPM")
G.add_edge("JPM", "Gold", relation="hedge")

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=12)
plt.title("Sample Financial Knowledge Graph")
plt.show()
