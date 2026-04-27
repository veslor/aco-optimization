# 🐜 Ant Colony Optimization for Wireless Sensor Networks

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
  <img src="https://img.shields.io/badge/Focus-Optimization-orange">
  <img src="https://img.shields.io/badge/Domain-WSN-purple">
</p>

<p align="center">
  <b>🚀 Swarm Intelligence • Energy Optimization • Interactive Simulation</b>
</p>

---

## 📌 Overview

This project implements and compares **energy-efficient clustering techniques** in Wireless Sensor Networks (WSN) using:

* 🔹 LEACH (Low Energy Adaptive Clustering Hierarchy)
* 🔹 SEP (Stable Election Protocol)
* 🔹 Ant Colony Optimization (ACO)
* 🔹 Bat Algorithm (BAT)

💡 The goal is to **optimize cluster head selection**, minimize energy consumption, and **extend network lifetime**.

---

## 🧠 Key Idea

Traditional protocols like LEACH and SEP rely on probabilistic selection.

👉 This project enhances them using:

* **ACO → intelligent pheromone-based optimization**
* **BAT → adaptive global search mechanism**

⚡ Result: **Improved energy efficiency & longer network survival**

---

## 🖥️ Live Simulation UI

An interactive simulation built using **Streamlit**.

### ▶️ Run locally:

```bash id="1o0kqg"
streamlit run app.py
```

### ✨ Features:

* Real-time node visualization
* Cluster head highlighting
* Dynamic simulation updates
* Interactive parameter control

---

## 📊 Results & Visualization

### 🔹 LEACH vs SEP

![LEACH vs SEP](images/leach_vs_sep_analysis.png)

---

### 🔹 LEACH-ACO vs LEACH-BAT

![LEACH ACO vs BAT](images/leach_aco_vs_bat.png)

---

### 🔹 SEP-ACO vs SEP-BAT

![SEP ACO vs BAT](images/sep_aco_vs_bat.png)

---

## 📈 Key Insights

* ✅ ACO significantly improves cluster head selection
* ✅ BAT algorithm ensures stable optimization
* ✅ SEP performs better in heterogeneous environments
* ✅ Hybrid techniques extend network lifetime

---

## ⚙️ Tech Stack

* 🐍 Python
* 📊 NumPy
* 📉 Matplotlib
* 🌐 Streamlit
* 📓 Jupyter Notebook

---

## ▶️ How to Run

```bash id="p2md1q"
pip install -r requirements.txt
jupyter notebook
streamlit run app.py
```

---

## 📁 Project Structure

```bash id="u3y62g"
aco-optimization/
│
├── ACO.ipynb
├── app.py
├── README.md
├── requirements.txt
└── images/
    ├── leach_vs_sep_analysis.png
    ├── leach_aco_vs_bat.png
    ├── sep_aco_vs_bat.png
```

---

## 🚀 Future Scope

* 🔹 Real-time animated ACO paths
* 🔹 Deploy Streamlit app online
* 🔹 Hybrid ACO + BAT optimization
* 🔹 Large-scale WSN simulation

---

## 👨‍💻 Author

**Nisant Kumar Pradhan**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
