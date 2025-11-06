import math

class binomial_distribution:
    def __init__(self, trials, success_rate):
        self.n = int(trials)
        self.p = float(success_rate)
        self.pf = {}  # cache for pmf

    def mean(self):
        return self.n * self.p

    def variance(self):
        return self.n * self.p * (1 - self.p)
    
    def stddev(self):
        return self.variance() ** 0.5

    def mgf(self):
        return f"(1 - {self.p} + {self.p} * e^t)^{self.n}"


    def pmf(self):
        self.pf = {}
        for x in range(self.n + 1):
            prob = math.comb(self.n, x) * (self.p ** x) * ((1 - self.p) ** (self.n - x))
            self.pf[x] = prob
        return self.pf

    def cdf(self):
        if not self.pf:
            self.pmf()
        cmf = {}
        acc = 0
        for i in sorted(self.pf.keys()):
            acc += self.pf[i]
            cmf[i] = acc
        return cmf
