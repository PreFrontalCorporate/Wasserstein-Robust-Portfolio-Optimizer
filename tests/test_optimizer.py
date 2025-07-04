import numpy as np
from utils.optimizer import robust_optimize

def test_optimizer_basic():
    mean = np.array([0.01, 0.02, 0.015])
    cov = np.eye(3) * 0.0001
    weights = robust_optimize(mean, cov, rho=0.1, lambda_reg=0.05, gamma=5.0, cap=0.5)
    assert np.isclose(np.sum(weights), 1), "Weights do not sum to 1"
    assert np.all(weights >= 0), "Negative weights found"
    assert np.all(weights <= 0.5), "Weights exceed cap"

if __name__ == "__main__":
    test_optimizer_basic()
    print("✅ Optimizer basic test passed!")
