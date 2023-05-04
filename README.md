# Estimating Pi API

This is a simple API that provides three different endpoints for estimating the value of pi using different methods. The endpoints are:

- `/`: Returns the value of pi from the `math` library in Python.
- `/leibniz`: Returns an estimate of pi using the Leibniz formula.
- `/monte_carlo`: Returns an estimate of pi using a Monte Carlo simulation.

## Usage

To use this API, you can send GET requests to the appropriate endpoint. For example, to get the value of pi from the `math` library, you can send a GET request to `/`:

```
GET /
```

This will return the value of pi as a string in the response body.

To get an estimate of pi using the Leibniz formula, you can send a GET request to `/leibniz` with an optional parameter `n` to specify the number of terms to use in the formula. For example, to estimate pi using the Leibniz formula with 100 terms, you can send a GET request to `/leibniz?n=100`:

```
GET /leibniz?n=100
```

This will return the estimated value of pi as a string in the response body.

To get an estimate of pi using a Monte Carlo simulation, you can send a GET request to `/monte_carlo` with an optional parameter `n` to specify the number of points to use in the simulation. For example, to estimate pi using a Monte Carlo simulation with 10000 points, you can send a GET request to `/monte_carlo?n=10000`:

```
GET /monte_carlo?n=10000
```

This will return the estimated value of pi as a string in the response body.

## Installation

To install and run this API, you can follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in the root directory of the project.
3. Start the API by running `python app.py` in the root directory of the project.
4. Send GET requests to the appropriate endpoints as described above.

Note that this is just a simple example and you may want to add more functionality or error handling depending on your specific use case.