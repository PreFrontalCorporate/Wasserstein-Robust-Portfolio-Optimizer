# wasserstein_app/app.py

from flask import Blueprint, request, jsonify
import numpy as np
from utils.optimizer import robust_optimize

# 🔥 Create blueprint
wasserstein_bp = Blueprint("wasserstein", __name__)

@wasserstein_bp.route("/optimize", methods=["POST"])
def optimize_portfolio():
    data = request.json

    mu = np.array(data.get("mean", []))
    cov = np.array(data.get("cov", []))
    rho = data.get("rho", 0.1)
    lambda_reg = data.get("lambda_reg", 0.05)
    gamma = data.get("gamma", 5.0)
    cap = data.get("cap", 0.4)

    if mu.size == 0 or cov.size == 0:
        return jsonify({"error": "Mean vector and covariance matrix must be provided."}), 400

    weights = robust_optimize(mu, cov, rho, lambda_reg, gamma, cap)
    return jsonify({"optimized_weights": weights.tolist()})

@wasserstein_bp.route("/example", methods=["GET"])
def example():
    n_assets = 5
    mean = np.random.rand(n_assets) * 0.05
    vol = np.array([0.15, 0.18, 0.12, 0.10, 0.20])
    cov = np.diag((vol / np.sqrt(252))**2)

    weights = robust_optimize(mean, cov, rho=0.1, lambda_reg=0.05, gamma=5.0, cap=0.4)
    return jsonify({
        "mean": mean.tolist(),
        "cov": cov.tolist(),
        "optimized_weights": weights.tolist()
    })
