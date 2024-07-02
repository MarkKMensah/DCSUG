import pytest
import networkx as nx
import pandas as pd

# Sample data for testing
sample_data = {
    'user1': ['A', 'A', 'B', 'C', 'D', 'E'],
    'user2': ['B', 'C', 'D', 'A', 'B', 'A']
}

# Convert sample data to DataFrame
df = pd.DataFrame(sample_data)

# Test function to check graph creation
def test_graph_creation():
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['user1'], row['user2'])
    
    assert len(G.nodes) == 5, "Graph should have 5 nodes"
    assert len(G.edges) == 6, "Graph should have 6 edges"

# Test function to check adjacency list representation
def test_adjacency_list():
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['user1'], row['user2'])

    adj_list = nx.to_dict_of_dicts(G)
    
    assert 'A' in adj_list, "Node A should be in the adjacency list"
    assert 'B' in adj_list['A'], "Node A should be connected to Node B"
    assert 'C' in adj_list['A'], "Node A should be connected to Node C"

# Test function to check adjacency matrix representation
def test_adjacency_matrix():
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['user1'], row['user2'])

    adj_matrix = nx.to_numpy_matrix(G)
    
    assert adj_matrix.shape == (5, 5), "Adjacency matrix should be 5x5"

# Test function to check degree centrality
def test_degree_centrality():
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['user1'], row['user2'])

    degree_centrality = nx.degree_centrality(G)
    
    assert degree_centrality['A'] == 0.5, "Degree centrality of node A should be 0.5"
    assert degree_centrality['B'] == 0.25, "Degree centrality of node B should be 0.25"

# Test function to check visualization
def test_visualization():
    import matplotlib.pyplot as plt
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['user1'], row['user2'])

    plt.figure()
    nx.draw(G, with_labels=True)
    plt.savefig("test_graph.png")
    
    # Check if the file is created
    import os
    assert os.path.exists("test_graph.png"), "Graph visualization should be saved as test_graph.png"

if __name__ == "__main__":
    pytest.main([__file__])
