from flask import Flask, render_template, jsonify
from ThereomGrimiore.discreate_distros import bernoulli_distro
import ThereomGrimiore.discreate_distros.integer_distrobution as integer_distrobution
from ThereomGrimiore.discreate_distros.binomial_distro import binomial_distribution
from ThereomGrimiore.discreate_distros.geometric_distro import geometric_distribution
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/<distro>/<float:n>/<int:trials>', methods=['GET', 'POST'])
def stats(distro, n, trials):
    n = round(n,5)

    if distro == "geometric":
        dist = geometric_distribution(trials, n)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    if distro == "binomial":
        dist  = binomial_distribution(trials, n)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    try:
        n_val = float(n)
    except (TypeError, ValueError):
        return jsonify({"error": "invalid numeric value"}), 400
    if distro == "bernoulli":
        dist = bernoulli_distro.bernoulli_distribution(n_val)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cmf": dist.cdf()})
    elif distro == "integer":
        idx = int(trials)
        dist = integer_distrobution.integer_distribution(idx)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "cdf": dist.cdf(), "mgf": dist.mgf()})
    return jsonify({"error": "unknown distribution"}), 404
if __name__ == "__main__":
    app.run(debug=True)