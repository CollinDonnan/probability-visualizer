from flask import Flask, render_template, jsonify
from ThereomGrimiore.discreate_distros import bernoulli_distro
import ThereomGrimiore.discreate_distros.integer_distrobution as integer_distrobution
# from ThereomGrimiore.discreate_distros.binomial_distro import BinomialDistro

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/<distro>/<float:n>', methods=['GET', 'POST'])
@app.route('/<distro>/<n>', methods=['GET', 'POST'])
def stats(distro, n):
    # accept numeric strings like ".5" by parsing here
    print(distro, n)
    try:
        n_val = float(n)
    except (TypeError, ValueError):
        return jsonify({"error": "invalid numeric value"}), 400

    if distro == "bernoulli":
        dist = bernoulli_distro.bernoulli_distribution(n_val)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "mgf": dist.mgf(), "cdf": dist.cdf()})
    elif distro == "integer":
        # allow integer strings or floats that represent integers
        try:
            idx = int(float(n))
        except (TypeError, ValueError):
            return jsonify({"error": "invalid integer value"}), 400
        dist = integer_distrobution.integer_distribution(idx)
        return jsonify({"pmf": dist.pmf(), "mean": dist.mean(), "variance": dist.variance(), "stddev": dist.stddev(), "cdf": dist.cdf()})
    return jsonify({"error": "unknown distribution"}), 404
if __name__ == "__main__":
    app.run(debug=True)