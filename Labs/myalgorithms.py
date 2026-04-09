import numpy as np
def calculate_pi(n_terms):
  s = 0.
  for k in range(1,n_terms):
    s += 1/(k**2)
  return np.sqrt(6*s)  # don't forget the square root!