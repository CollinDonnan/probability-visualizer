
from math import isclose
import ThereomGrimiore.discreate_distros.integer_distrobution as integer_distrobution

dist  = integer_distrobution.integer_distribution(10)

def test_pmf():
    pmf = dist.pmf()
    # All probabilities should sum to 1
    assert isclose(sum(pmf.values()), 1.0)
    # Each key should be an integer from 0 to k-1
    assert list(pmf.keys()) == list(range(dist.k))
    # Each probability should be 1/k
    assert all(isclose(v, 1/dist.k) for v in pmf.values())

def test_cdf():
    cdf = dist.cdf()
    # Last value should be 1.0
    assert isclose(list(cdf.values())[-1], 1.0)
    # CDF should be non-decreasing
    vals = list(cdf.values())
    assert all(vals[i] <= vals[i+1] for i in range(len(vals)-1))

def test_mean():
    assert isclose(dist.mean(), (dist.k - 1) / 2)

def test_variance():
    expected_var = (dist.k**2 - 1) / 12
    assert isclose(dist.variance(), expected_var)

def test_stddev():
    expected_std = ((dist.k**2 - 1) / 12) ** 0.5
    assert isclose(dist.stddev(), expected_std)
