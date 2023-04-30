import random
import networkx as nx


def generate_gev(G):
    # Step 1
    Gs = G.copy()

    # Step 2: Node Relabeling
    for i in range(G.number_of_nodes()):
        # Step 3
        node = random.choice(list(Gs.nodes()))
        label = Gs.nodes[node]['label']
        candidate_labels = [l for l in Gs.nodes[node]['candidate_labels'] if l != label]
        if len(candidate_labels) == 0:
            continue
        new_label = random.choice(candidate_labels)
        Gs.nodes[node]['label'] = new_label

    # Step 6: Node Insertion
    num_nodes = G.number_of_nodes()
    for i in range(G.number_of_nodes()):
        new_node = num_nodes + i
        node = random.choice(list(Gs.nodes()))
        label = Gs.nodes[node]['label']
        Gs.add_node(new_node, label=label)
        Gs.add_edge(node, new_node)

    # Step 11: Edge Deletion
    num_edges = G.number_of_edges()
    to_delete = random.randint(0, num_edges)
    for i in range(to_delete):
        edge = random.choice(list(Gs.edges()))
        Gs.remove_edge(*edge)

    # Step 16: Edge Relabeling
    for i in range(G.number_of_edges()):
        edge = random.choice(list(Gs.edges()))
        label = Gs.edges[edge]['label']
        candidate_labels = [l for l in Gs.edges[edge]['candidate_labels'] if l != label]
        if len(candidate_labels) == 0:
            continue
        new_label = random.choice(candidate_labels)
        Gs.edges[edge]['label'] = new_label

    # Step 21: Edge Insertion
    to_insert = G.number_of_edges() - to_delete
    for i in range(to_insert):
        new_edge = (random.choice(list(Gs.nodes())), random.choice(list(Gs.nodes())))
        if new_edge in Gs.edges():
            continue
        label = random.choice(list(G.edges[new_edge]['candidate_labels']))
        Gs.add_edge(*new_edge, label=label)

    # return the graph pair and GEV
    return (G, Gs), None
