# Wasserstein-Robust Portfolio Optimizer

A Flask-based API for solving portfolio optimization problems using Wasserstein Distributionally Robust Optimization (DRO) with mean and covariance perturbations.

## Features

* Robust mean and covariance penalties
* Diversification constraints
* CVXPY-based optimization
* Docker-ready

## Usage

### Local

```bash
pip install -r requirements.txt
python app.py
```

### Docker

```bash
docker build -t wasserstein-optimizer .
docker run -p 5000:5000 wasserstein-optimizer
```

### Example Request

```bash
curl -X POST http://localhost:5000/optimize \
-H "Content-Type: application/json" \
-d @examples/sample_request.json
```

## Example JSON (examples/sample\_request.json)

```json
{
  "mean": [0.01, 0.02, 0.015, 0.017, 0.018],
  "cov": [[0.0001, 0, 0, 0, 0],
          [0, 0.0001, 0, 0, 0],
          [0, 0, 0.0001, 0, 0],
          [0, 0, 0, 0.0001, 0],
          [0, 0, 0, 0, 0.0001]],
  "rho": 0.1,
  "lambda_reg": 0.05,
  "gamma": 5.0,
  "cap": 0.4
}
```

## Authors

* PreFrontal Corporate
