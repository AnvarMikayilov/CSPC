"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?


from decay import simulate_decay

def test_decay_initial_atoms():
    atoms_left = simulate_decay(N0=1000, half_life=10.0, time_steps=[0.0])
    assert atoms_left[0] == 1000

def test_decay_half_life():
    atoms_left = simulate_decay(N0=10000, half_life=10.0, time_steps=[10.0])
    assert 4500 <= atoms_left[0] <= 5500