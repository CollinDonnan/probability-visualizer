import pytest
from ThereomGrimiore.discreate_distros import bernoulli_distro

def test_valid_initialization():
    b = bernoulli_distro.bernoulli_distribution(0.5)
    assert b.success_rate == 0.5

@pytest.mark.parametrize("invalid_value", [-0.1, 1.1])
def test_invalid_initialization(invalid_value):
    with pytest.raises(ValueError):
        bernoulli_distro.bernoulli_distribution(invalid_value)

def test_pmf():
    b = bernoulli_distro.bernoulli_distribution(0.7)
    expected = {0: 0.3, 1: 0.7}
    actual = b.pmf()

    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])

def test_mean():
    b = bernoulli_distro.bernoulli_distribution(0.4)
    assert b.mean() == 0.4

def test_variance():
    b = bernoulli_distro.bernoulli_distribution(0.4)
    expected = 0.4 * (1 - 0.4)
    assert b.variance() == pytest.approx(expected)

def test_stddev():
    b = bernoulli_distro.bernoulli_distribution(0.4)
    expected = (0.4 * 0.6) ** 0.5
    assert b.stddev() == pytest.approx(expected)

def test_mgf():
    b = bernoulli_distro.bernoulli_distribution(0.5)
    expected_str = "(1 - 0.5) + 0.5 * exp(t)"
    assert b.mgf() == expected_str

def test_cdf():
    b = bernoulli_distro.bernoulli_distribution(0.8)
    expected = {0: 0.2, 1: 1.0}
    actual = b.cdf()
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])

