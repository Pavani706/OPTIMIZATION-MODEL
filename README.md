# OPTIMIZATION-MODEL

🚚 Delivery Route Optimization using Linear Programming 📌 Project Description This project demonstrates how to solve a real-world logistics problem using linear programming with the PuLP library in Python. The goal is to minimize delivery costs while meeting customer demand across cities and staying within truck capacity limits.

📦 Problem Statement A logistics company delivers packages to multiple cities using a limited number of trucks. Each truck has a maximum capacity, and each city has a fixed demand for packages. The company wants to determine the optimal number of packages each truck should deliver to each city to minimize total delivery cost.

✅ Features Linear programming model using PuLP

Customizable demand, truck capacities, and distances

Optimal cost calculation

Distribution plan output for each truck

📂 Project Structure bash Copy Edit Optimization/ ├── optimal.py # Main Python script with PuLP optimization code ├── README.md # Project description and setup instructions 📌 Requirements Python 3.x

PuLP 💻 Installation Install the required Python package using pip:

bash Copy Edit pip install pulp 🚀 How to Run Navigate to the project folder and run the script:

bash Copy Edit cd D:\Optimization python optimal.py 📈 Output Example text Copy Edit Status: Optimal Total Cost: 18200.0

Package Distribution Plan: Truck T1 → City A: 100 packages Truck T1 → City B: 50 packages Truck T2 → City C: 120 packages Truck T2 → City B: 30 packages
