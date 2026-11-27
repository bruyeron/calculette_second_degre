import pytest
from solution import solution_sec_degree


def test_deux_solutions_reelles():
    """Teste le cas où le discriminant delta est strictement positif (delta > 0)."""
    resultat = solution_sec_degree(1, -3, 2)
    assert resultat["delta"] == 1
    assert resultat["status"] == "Delta positif"
    assert sorted(resultat["roots"]) == [1.0, 2.0]


def test_une_solution_reelle():
    """Teste le cas où le discriminant delta est nul (delta == 0)."""
    resultat = solution_sec_degree(1, -2, 1)
    assert resultat["delta"] == 0
    assert resultat["status"] == "Delta egale a zero"
    assert resultat["roots"] == [1.0]


def test_aucune_solution_reelle():
    """Teste le cas où le discriminant delta est strictement négatif (delta < 0)."""
    resultat = solution_sec_degree(1, 1, 1)
    assert resultat["delta"] == -3
    assert resultat["status"] == "Delta negative"
    assert resultat["roots"] == []


def test_coefficient_a_nul():
    """Vérifie qu'une erreur ValueError est levée si a = 0."""
    with pytest.raises(ValueError):
        solution_sec_degree(0, 2, 3)