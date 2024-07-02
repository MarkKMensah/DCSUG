import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('path_to_twitter_dataset.csv')

# Preprocess the data (example: extract user interactions)
interactions = df[['user1', 'user2']]  # Assuming 'user1' mentions 'user2'

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for _, row in interactions.iterrows():
    G.add_edge(row['user1'], row['user2'])

# Basic visualization
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_size=50, font_size=10)
plt.show()
