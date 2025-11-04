class bernoulli_distribution:
    def __init__(self, success_rate):
        if success_rate < 0 or success_rate > 1:
            raise ValueError("Success rate must be between 0 and 1.")
        self.success_rate = success_rate

    def pmf(self):
        # represents the probability mass function for a Bernoulli distribution
        return {0: 1 - self.success_rate, 1: self.success_rate}

    def mean(self):
        return self.success_rate

    def variance(self):
        return self.success_rate * (1 - self.success_rate)

    def stddev(self):
        return self.variance() ** 0.5

    def mgf(self):
        # Moment Generating Function for Bernoulli distribution
        return f"(1 - {self.success_rate}) + {self.success_rate} * exp(t)"

    def cdf(self):
        return {0: 1 - self.success_rate, 1: 1}
