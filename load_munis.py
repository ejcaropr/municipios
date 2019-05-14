import pandas as pd
from muni_adj import muni_adj
from graphviz import Graph

def generate_edges(muni_adj):
    edges = [(m1,m2) for m1 in muni_adj for m2 in muni_adj[m1] if m1<m2]
    return edges

def gen_csv(name='muni_edges.csv'):
    edge_frame = pd.DataFrame(generate_edges(muni_adj))
    edge_frame.to_csv(name)

def gen_dot(name='municipios.dot'):
    dot = Graph(comment='municipios', engine='sfdp')
    dot.graph_attr.update({'overlap':'false',
                           'splines':'true'})
    for muni in muni_adj:
        dot.node(muni)
    for edge in generate_edges(muni_adj):
        dot.edge(*edge)
    return dot
