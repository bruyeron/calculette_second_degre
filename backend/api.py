from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, StrictInt
from solution import solution_sec_degree

app = FastAPI(title="Resolution de l'equation du second degree")

# Autorise ReactJS (port 5173 ou 3000) à appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class EquationInput(BaseModel):
    a: StrictInt
    b: StrictInt
    c: StrictInt


@app.post("/api/resoudre")
def solve_endpoint(data: EquationInput):
    try:
        return solution_sec_degree(data.a, data.b, data.c)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err)) from err