import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title("🐜 ACO-based WSN Simulation")

# ---------------- UI CONTROLS ----------------
num_nodes = st.slider("Number of Nodes", 20, 200, 100)
rounds = st.slider("Simulation Rounds", 10, 500, 100)

run = st.button("Run Simulation")

# ---------------- CONSTANTS ----------------
FIELD_SIZE = 100
P = 0.1

# ---------------- NODE ----------------
class Node:
    def __init__(self, i):
        self.id = i
        self.x = np.random.uniform(0, FIELD_SIZE)
        self.y = np.random.uniform(0, FIELD_SIZE)
        self.energy = np.random.uniform(0.3, 1.0)
        self.dead = False

# ---------------- SIMULATION ----------------
def simulate():
    nodes = [Node(i) for i in range(num_nodes)]
    history = []

    for r in range(rounds):
        alive = [n for n in nodes if not n.dead]

        if not alive:
            break

        # select cluster heads randomly
        ch_count = max(1, int(P * len(alive)))
        chs = random.sample(alive, ch_count)

        # simulate energy drop
        for n in alive:
            n.energy -= np.random.uniform(0.001, 0.01)
            if n.energy <= 0:
                n.dead = True

        history.append((nodes.copy(), chs))

    return history

# ---------------- VISUALIZATION ----------------
def plot_round(nodes, chs, round_no):
    fig, ax = plt.subplots()

    for n in nodes:
        if n.dead:
            ax.plot(n.x, n.y, 'rx')
        elif n in chs:
            ax.plot(n.x, n.y, 'go', markersize=8)
        else:
            ax.plot(n.x, n.y, 'bo', markersize=4)

    ax.set_title(f"Round {round_no}")
    ax.set_xlim(0, FIELD_SIZE)
    ax.set_ylim(0, FIELD_SIZE)

    return fig

# ---------------- RUN ----------------
if run:
    st.write("Running simulation...")
    history = simulate()

    placeholder = st.empty()

    for i, (nodes, chs) in enumerate(history):
        fig = plot_round(nodes, chs, i+1)
        placeholder.pyplot(fig)
