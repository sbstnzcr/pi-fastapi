import math
import random
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def get_pi():
    return {"pi": math.pi}


@app.get("/leibniz")
async def get_pi_leibniz(n: int = Query(default=1000)):
    pi_estimate = 0
    sign = 1

    for i in range(n):
        pi_estimate += sign / (2 * i + 1)
        sign *= -1

    return {"pi": pi_estimate * 4}


@app.get("/monte_carlo")
async def get_pi_monte_carlo(n: int = Query(default=1000)):
    inside_circle = 0

    for _ in range(n):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        origin_dist = rand_x**2 + rand_y**2

        if origin_dist <= 1:
            inside_circle += 1

    return {"pi": 4 * inside_circle / n}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
