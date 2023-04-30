import networkx as np
import pickle
import random

def node_relabeling(v, l_s, l_s_prime):
    return (v, l_s_prime, l_s)

def node_insertion(v_new, l_s):
    return (v_new, l_s)

def edge_deletion(e, l_s):
    return (e[0], e[1], l_s)

def edge_relabeling(e, l_s, l_s_prime):
    return (e[0], e[1], l_s_prime)

def edge_insertion(e_new, l_s):
    return (e_new[0], e_new[1], l_s)

def generate_gev(G, NR, NID, EI, ER):
    # Step 1: Copy the original graph G to generate G_s
    G_s = G.copy()

    # Step 2-5: Node Relabeling
    for i in range(NR):
        v = random.choice(list(G_s.nodes()))
        l_s, l_s_prime = random.sample(G_s.nodes[v]['label'], 2)
        G_s.nodes[v]['label'] = node_relabeling(v, l_s, l_s_prime)

    # Step 6-8: Node Insertion
    for i in range(NID):
        v_new = max(list(G_s.nodes())) + 1
        l_s = random.choice(G_s.nodes[v_new-1]['label'])
        G_s.add_node(v_new, label=node_insertion(v_new, l_s))

    # Step 9-15: Edge Deletion
    T = random.randint(0, len(G_s.edges()))
    Del_Edge = []
    for i in range(T):
        e = random.choice(list(G_s.edges()))
        Del_Edge.append(e)
        l_s = random.choice(G_s.edges[e]['label'])
        G_s.remove_edge(*e)
        G_s.add_edge(*edge_deletion(e, l_s))

    # Step 16-19: Edge Relabeling
    for i in range(ER):
        e = random.choice(list(G_s.edges()))
        l_s, l_s_prime = random.sample(G_s.edges[e]['label'], 2)
        G_s.edges[e]['label'] = edge_relabeling(e, l_s, l_s_prime)

    # Step 20-22: Edge Insertion
    for i in range(len(G_s.edges()) - T):
        e_new = (max(list(G_s.nodes())) + 1, max(list(G_s.nodes())) + 2)
        l_s = random.choice(G_s.nodes[e_new[0]]['label'])
        while e_new in Del_Edge:
            e_new = (e_new[0] + 1, e_new[1] + 1)
        G_s.add_edge(*e_new, label=edge_insertion(e_new, l_s))

    # Step 23: Return G and G_s with the ground truth GEV
    return (G, G_s)




if __name__ == '__main__':
