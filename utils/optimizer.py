import cvxpy as cp
import numpy as np

def robust_optimize(mu_o, cov_matrix, rho, lambda_reg, gamma, cap=0.4):
    n_assets = mu_o.shape[0]
    w = cp.Variable(n_assets)
    term_adversarial = (rho - lambda_reg) * cp.norm(w, 2)
    risk_term = gamma * cp.quad_form(w, cov_matrix)
    objective = cp.Minimize(-w @ mu_o + term_adversarial + risk_term)
    constraints = [w >= 0, cp.sum(w) == 1, w <= cap]
    prob = cp.Problem(objective, constraints)
    prob.solve()
    return w.value
