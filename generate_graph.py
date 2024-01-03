import networkx as nx
import matplotlib.pyplot as plt
import json
import numpy as np
from netgraph import Graph
from pathlib import Path

# Read the JSON data
path_process = "./my_conf/process_3.json"

def create_graph(path_process):
    filename = Path(path_process).name.split('.')[0]

    with open(path_process) as f:
        data = json.load(f)

    edges = []

    # Add edges based on the JSON data
    for source in data["tasks"]:
        sum = 0
        for transition in source["transitions"]:
            # (source, target, weight)
            edges.append((source["id"], transition["id"], transition["probability"]))
            sum += transition["probability"]
        # assert that either all probabilities sum up to 1 or 0 (for the last task)
        assert sum == 1 or sum == 0, "Probabilities for transitions from task {} do not sum up to 1 or 0".format(source["id"])

    edge_labels = {(s, t): prob for (s, t, prob) in edges}
    # edge_width = {(s, t) : 4 * np.abs(prob) for (s, t, prob) in edges}

    # Node descriptions
    node_labels = {task["id"]: f"Task {task['id']}\nD: {task['duration']}\nD_SD: {task['duration_SD']}" for task in data["tasks"]}
    cmap = 'RdGy'

    # # Plot the graph using netgraph
    fig, ax = plt.subplots()
    Graph(edges, edge_labels=edge_labels, 
        edge_label_position=0.3, arrows=True, ax=ax, 
        node_labels=node_labels, edge_cmap=cmap, 
        font_size=40, edge_layout='curved', node_size=6, node_color='skyblue',
        edge_weight=6.0)
    print("Graph saved to: " + "./images/" + filename + ".png")
    plt.savefig("./images/" + filename + ".png", dpi=300, bbox_inches='tight')
    

# for every file that starts with name process
for path in Path("./conf/").glob("process*.json"):
    print(path)
    create_graph(path)