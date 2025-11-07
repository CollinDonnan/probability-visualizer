class geometric_distribution:
    def __init__(self, n, success_rate):
        self.n = n
        self.success_rate = success_rate

    def pmf(self):
        pmf = {}
        for i in range(1, self.n+1):
            pmf[i] = (((1-self.success_rate) ** (i-1)) * self.success_rate)
        return pmf

    def cdf(self):
        cdf = {}
        for i in range(1, self.n + 1):
            cdf[i] = (1-((1-self.success_rate) ** i))
        return cdf

    def mean(self):
        return 1/self.success_rate

    def variance(self):
        return (1-self.success_rate)/(self.success_rate ** 5)
    
    def stddev(self):
        return self.variance() ** .5

    def mgf(self):
        return f"(e^t * {self.success_rate})/(1-e^t(1-{self.success_rate}))"