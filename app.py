import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(layout="wide")

st.title("🚀 Multi-Algorithm WSN Simulator")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Controls")

num_nodes = st.sidebar.slider("Nodes", 20, 200, 100)
rounds = st.sidebar.slider("Rounds", 50, 500, 200)

algo = st.sidebar.selectbox("Algorithm", [
    "LEACH", "SEP", "ACO", "BAT",
    "ACO-LEACH", "ACO-SEP",
    "BAT-LEACH", "BAT-SEP"
])

speed = st.sidebar.slider("Speed", 0.01, 0.2, 0.05)

FIELD_SIZE = 100
P = 0.1
m = 0.2
alpha = 1.0

# ---------------- SESSION ----------------
if "run" not in st.session_state:
    st.session_state.run = False

if "nodes" not in st.session_state:
    st.session_state.nodes = []

# ---------------- BUTTONS ----------------
col1, col2, col3 = st.columns(3)

if col1.button("▶️ Start"):
    st.session_state.run = True

if col2.button("⏸ Pause"):
    st.session_state.run = False

if col3.button("🔄 Reset"):
    st.session_state.nodes = []
    st.session_state.run = False

# ---------------- NODE ----------------
class Node:
    def __init__(self, i, advanced=False):
        self.id = i
        self.x = np.random.uniform(0, FIELD_SIZE)
        self.y = np.random.uniform(0, FIELD_SIZE)
        self.energy = np.random.uniform(0.5, 1.0)
        if advanced:
            self.energy *= (1 + alpha)
        self.dead = False

# ---------------- INIT ----------------
def init_nodes():
    nodes = []
    adv_ids = set(random.sample(range(num_nodes), int(m*num_nodes)))

    for i in range(num_nodes):
        nodes.append(Node(i, i in adv_ids))

    return nodes

# ---------------- SELECTION METHODS ----------------
def leach(nodes):
    alive = [n for n in nodes if not n.dead]
    count = max(1, int(P * len(alive)))
    return random.sample(alive, count)

def sep(nodes):
    alive = [n for n in nodes if not n.dead]
    probs = [n.energy for n in alive]
    probs = np.array(probs) / np.sum(probs)
    count = max(1, int(P * len(alive)))
    idx = np.random.choice(len(alive), count, replace=False, p=probs)
    return [alive[i] for i in idx]

def aco(nodes):
    alive = [n for n in nodes if not n.dead]
    scores = np.array([n.energy/(np.sqrt(n.x**2+n.y**2)+1) for n in alive])
    probs = scores / np.sum(scores)
    count = max(1, int(P * len(alive)))
    idx = np.random.choice(len(alive), count, replace=False, p=probs)
    return [alive[i] for i in idx]

def bat(nodes):
    alive = [n for n in nodes if not n.dead]
    sorted_nodes = sorted(alive, key=lambda n: n.energy, reverse=True)
    count = max(1, int(P * len(alive)))
    return sorted_nodes[:count]

# ---------------- ALGO MAPPER ----------------
def select_CH(nodes):
    if algo == "LEACH":
        return leach(nodes)

    if algo == "SEP":
        return sep(nodes)

    if algo == "ACO":
        return aco(nodes)

    if algo == "BAT":
        return bat(nodes)

    if algo == "ACO-LEACH":
        return aco(leach(nodes))

    if algo == "ACO-SEP":
        return aco(sep(nodes))

    if algo == "BAT-LEACH":
        return bat(leach(nodes))

    if algo == "BAT-SEP":
        return bat(sep(nodes))

# ---------------- STEP ----------------
def step(nodes):
    chs = select_CH(nodes)

    for n in nodes:
        if not n.dead:
            n.energy -= np.random.uniform(0.003, 0.01)
            if n.energy <= 0:
                n.dead = True

    return chs

# ---------------- PLOT ----------------
def plot_network(nodes, chs, r):
    fig, ax = plt.subplots(figsize=(6,6))

    for n in nodes:
        if n.dead:
            ax.scatter(n.x, n.y, c='red', s=10)
        elif n in chs:
            ax.scatter(n.x, n.y, c='green', s=50, marker='D')
        else:
            ax.scatter(n.x, n.y, c='blue', s=10)

    ax.set_title(f"{algo} - Round {r}")
    ax.set_xlim(0, FIELD_SIZE)
    ax.set_ylim(0, FIELD_SIZE)

    return fig

# ---------------- STATS ----------------
def plot_stats(dead, energy):
    fig, ax = plt.subplots(1,2, figsize=(10,4))

    ax[0].plot(dead)
    ax[0].set_title("Dead Nodes")

    ax[1].plot(energy)
    ax[1].set_title("Avg Energy")

    return fig

# ---------------- MAIN ----------------
if not st.session_state.nodes:
    st.session_state.nodes = init_nodes()

nodes = st.session_state.nodes

plot_area = st.empty()
stats_area = st.empty()

dead_hist = []
energy_hist = []

if st.session_state.run:
    for r in range(rounds):

        chs = step(nodes)

        dead = len([n for n in nodes if n.dead])
        energy = np.mean([n.energy for n in nodes if not n.dead]) if nodes else 0

        dead_hist.append(dead)
        energy_hist.append(energy)

        fig1 = plot_network(nodes, chs, r)
        plot_area.pyplot(fig1)

        fig2 = plot_stats(dead_hist, energy_hist)
        stats_area.pyplot(fig2)

        time.sleep(speed)

        if not st.session_state.run:
            break