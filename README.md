# SupplyGuard AI

An educational prototype for supply-chain crisis prevention and recovery. It combines:
- Route planning using Dijkstra's shortest-path algorithm
- Inventory stock-cover estimation
- Alternative warehouse stock discovery
- Explainable rule-based recovery recommendations
- An interactive crisis simulator

> Important: This project uses simulated data and illustrative route values. It is not intended for real logistics, medical, or operational decisions.

## Run locally

Python 3.10+ recommended.

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy from GitHub

1. Create a GitHub repository named `supplyguard-ai`.
2. Upload all files and the `data/` folder from this project.
3. Open https://share.streamlit.io/
4. Sign in with GitHub and choose **Create app**.
5. Select your repository, branch `main`, and main file `app.py`.
6. Deploy.

## Project structure

```text
supplyguard-ai/
├── app.py
├── route_optimizer.py
├── inventory.py
├── recovery_engine.py
├── requirements.txt
├── README.md
└── data/
    └── sample_shipments.csv
```

## What is implemented?

- A Dijkstra route optimizer that respects blocked roads
- Inventory stock-cover calculations
- Suggestions for alternative stock sources
- A recovery recommendation engine that reacts to simulated disruptions
- A Streamlit dashboard for the demo

## Suggested next steps

1. Add CSV upload and input validation.
2. Add a visual road graph or map.
3. Use real, documented datasets to train and evaluate a delivery-delay model.
4. Compare recovery plans with a measurable cost/time/stockout scoring function.
5. Add tests and a database if the project grows.
