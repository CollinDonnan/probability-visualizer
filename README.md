[image]({ 	https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white})
# 📊 Probability Visualizer

A full-stack Flask web app that calculates and visualizes common probability distributions.  
It computes key statistical properties — mean, variance, standard deviation, and the moment-generating function (MGF) — while interactively plotting each distribution’s PMF and CDF using Chart.js. This project to is deployed at http://my-env.eba-ufcxb3ib.us-east-2.elasticbeanstalk.com/

---

## ⚙️ Tech Stack

- **Deploymnet:** AWS Elastic Beanstalk
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Templates:** Jinja2  
- **Math Engine:** Custom Python functions (no external stats libraries)  
- **CI:** GitHub Actions, `uv`, `ty`, `ruff`

---

## 🧩 How It Works

1. Choose a distribution  
2. Enter the required parameters  
3. Click **Generate**  
4. The app:
   - Computes the mean, variance, standard deviation, and MGF  
   - Displays the PMF and CDF interactively

---

## 🧮 Supported Distributions

Currently, the app supports **Bernoulli**, **Binomial**, **Geometric**, and **Integer** distributions.  
More distributions are planned in future releases.

---

## 🚀 Installation

### Requirements
- Python **3.12+**  
- Pip **25.2+**

### Setup
```bash
git clone https://github.com/CollinDonnan/stats-distro.git
cd stats-distro
pip install uv
uv sync
python3 app.py
