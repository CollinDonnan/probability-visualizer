document.addEventListener('DOMContentLoaded', () => {
  enter = document.getElementById("enter");
 distros = document.getElementById("distros");
 trialsEl = document.getElementById("trials");
 probEl = document.getElementById("success_rate");
 mean = document.getElementById("mean");
 variance = document.getElementById("variance");
 stddev = document.getElementById("standard_deviation");
 mgf = document.getElementById("moment_generating_function");
  const pmfCanvas = document.getElementById("pmf");
  const cdfCanvas = document.getElementById("cmf");

  let pmfChart = null;
  let cdfChart = null;


const distributionInputs = document.getElementById('distributionInputs');

function updateInputs() {
  const selectedValue = distros.value;

  if (selectedValue === "Integer") {
    distributionInputs.innerHTML = `
      <label for="trials">Trials (n):</label>
      <input id="trials" type="number" min="1" max="100" step="1" placeholder="Number of trials" value="1" />
    `;
  } else if (selectedValue === "Bernoulli") {
    distributionInputs.innerHTML = `
      <label for="success_rate">Success rate (p):</label>
      <input id="success_rate" type="number" min="0" max="1" step="0.01" placeholder="Success probability (0–1)" value="0.5" />
    `;
  } else if(selectedValue === "Geometric"){
        distributionInputs.innerHTML = `
      <label for="trials">Trials (n):</label>
      <input id="trials" type="number" min="1" max="100" step="1" placeholder="Number of trials" value="1" />
            <label for="success_rate">Success rate (p):</label>
      <input id="success_rate" type="number" min="0" max="1" step="0.01" placeholder="Success probability (0–1)" value="0.5" />
    `;

  } else if(selectedValue === "Binomial"){
            distributionInputs.innerHTML = `
      <label for="trials">Trials (n):</label>
      <input id="trials" type="number" min="1" max="100" step="1" placeholder="Number of trials" value="1" />
            <label for="success_rate">Success rate (p):</label>
      <input id="success_rate" type="number" min="0" max="1" step="0.01" placeholder="Success probability (0–1)" value="0.5" />
    `;
  }
   else {
    distributionInputs.innerHTML = ''; // for other distributions
  }
   trialsEl = document.getElementById("trials");
 probEl = document.getElementById("success_rate");
   enter = document.getElementById("enter");
 console.log(trials)
 console.log(probEl)
}

// Initial load
updateInputs();

// Update inputs when selection changes
distros.addEventListener('change', updateInputs);

  enter.addEventListener("click", async (e) => {
    e.preventDefault();

    const distro = distros.value.toLowerCase();
    p = parseFloat(probEl.value);
    const trials = parseInt(trialsEl.value);
    if (p == 1){
        //will be fixed on backend
        p = 1.000001
    }

    const response = await fetch(`/${distro}/${p}/${trials}`);
    const data = await response.json();

    mean.textContent = `Mean: ${data.mean}`;
    variance.textContent = `Variance: ${data.variance}`;
    stddev.textContent = `Standard Deviation: ${data.stddev}`;
    mgf.textContent = `Moment Generating Function: ${data.mgf}`;

    drawCharts(data.pmf, data.cdf);
  });

  function drawCharts(pmf, cdf) {
    const pmfCtx = pmfCanvas.getContext('2d');
    const cdfCtx = cdfCanvas.getContext('2d');

    const normalize = obj => {
      const keys = Object.keys(obj).sort((a,b)=>a-b);
      return { labels: keys, values: keys.map(k => obj[k]) };
    };

    const pmfData = normalize(pmf);
    const cdfData = normalize(cdf);

    if (pmfChart) pmfChart.destroy();
    if (cdfChart) cdfChart.destroy();

    pmfChart = new Chart(pmfCtx, {
      type: 'bar',
      data: {
        labels: pmfData.labels,
        datasets: [{ label: 'PMF', data: pmfData.values, borderColor: 'blue', borderWidth: 2 }]
      },
      options: { scales: { y: { beginAtZero: true } } }
    });

    cdfChart = new Chart(cdfCtx, {
      type: 'bar',
      data: {
        labels: cdfData.labels,
        datasets: [{ label: 'CDF', data: cdfData.values, borderColor: 'green', borderWidth: 2 }]
      },
      options: { scales: { y: { beginAtZero: true } } }
    });
  }
});
