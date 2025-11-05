class integer_distribution:
    def __init__(self, k):
        self.k = k

    def pmf(self):
        pmf = {}
        for i in range(self.k):
            pmf.update({i: 1 / self.k})
        return pmf

    def cmf(self):
        cdf = {}
        cumulative = 0
        for i in range(self.k):
            cumulative += 1 / self.k
            cdf.update({i: cumulative})
        return cdf
    
    def mgf(self):
        return f"(e^t(1-e^t{self.k}))/({self.k}(1-e^t)))"
    

    def mean(self):
        return (self.k - 1) / 2

    def variance(self):
        return (self.k**2 - 1) / 12

    def stddev(self):
        return self.variance() ** 0.5
