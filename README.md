# CSPC - Computer Science for Physics and Chemistry
**PW1_Lab A**


# Project Structure
- `PW1/Lab A/decay.py`: Radioactive decay simulation using NumPy and probabilities.
- `PW1/Lab A/test_decay.py`: Automated unit tests using Pytest.
- `PW1/Lab A/speed.py`: Performance benchmark comparing pure Python loops vs NumPy vectorized calculations.
- `PW1/Lab A/environment.yml`: Conda environment specification (`cspc`).

# Comparison
Running `speed.py` with N = 1,000,000 operations yielded:
- **Python loop**: ~0.08 s
- **NumPy vectorization**: ~0.002 s
NumPy demonstrates significant execution speedup due to optimized C-level contiguous memory operations.

# Run
1. Activate environment:
   ```bash
   conda activate cspc


## PW1 Lab B
The observed data shows an exponential decay of radioactive counts over time.
Comparing the scatter plot of observed data with the theoretical curve $N(t) = N_0 e^{-\lambda t}$ shows that the experimental observations closely match the analytical decay law.
The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` and `plot.py`, ensuring the plot is automatically rebuilt whenever input data or code changes.