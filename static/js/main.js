document.addEventListener('DOMContentLoaded', () => {
    const enter = document.getElementById("enter");
    const distros = document.getElementById("distros");
    const trialsEl = document.getElementById("trials");
    const probEl = document.getElementById("success_rate");

    const mean = document.getElementById("mean");
    const variance = document.getElementById("variance");
    const standard_deviation = document.getElementById("standard_deviation");
    const moment_generating_function = document.getElementById("moment_generating_function");
    const pmfCanvas = document.getElementById("pmf");
    const cmfCanvas = document.getElementById("cmf");

    let pmfChart = null;
    let cmfChart = null;

    enter.addEventListener("click", (e) => {
        e.preventDefault();

        const distro = (distros.value || 'integer').toString().trim().toLowerCase();
        // ensure probEl exists and parse as float with fallback 0.0
        console.log(probEl);
        const n = (probEl && typeof probEl.value !== 'undefined') ? (parseFloat((probEl.value || '').toString().trim()) || 0.0) : 0.0;
        const trials = parseInt((trialsEl.value || '').toString().trim(), 10) || 0;

        const url = `/${distro}/${n}/${trials}`;

        fetch(url, {
            method: 'GET',
            headers: { 'Accept': 'application/json' },
        })
        .then(response => response.json())
        .then(data => {
            displayData(data);
        });
    });

    function displayData(data) {
        mean.innerText = `Mean: ${data.mean}`;
        variance.innerText = `Variance: ${data.variance}`;
        standard_deviation.innerText = `Standard Deviation: ${data.stddev}`;
        moment_generating_function.innerText = `Moment Generating Function: ${data.mgf}`;
        displayCharts(data.pmf, data.cmf);
    }

    function displayCharts(pmf, cmf){
      const pmfCtx = pmfCanvas.getContext('2d');
      const cmfCtx = cmfCanvas.getContext('2d');

      const normalize = (obj) => {
        if (Array.isArray(obj)) {
          return { labels: obj.map((_, i) => String(i)), values: obj.map(v => Number(v)) };
        }
        const keys = Object.keys(obj).sort((a,b)=>Number(a)-Number(b));
        return { labels: keys.map(k => String(k)), values: keys.map(k => Number(obj[k])) };
      };

      const pmfData = normalize(pmf);
      const cmfData = normalize(cmf);
if (pmfChart) { pmfChart.destroy(); pmfChart = null; }
if (cmfChart) { cmfChart.destroy(); cmfChart = null; }

// only create charts if Chart.js is loaded and canvas contexts are available
if (typeof Chart !== 'undefined' && pmfCtx) {
  pmfChart = new Chart(pmfCtx, {
    type: 'bar',
    data: {
      labels: pmfData.labels,
      datasets: [{ label: 'PMF', data: pmfData.values, borderColor: 'blue', backgroundColor: 'rgba(0,0,0,0)', borderWidth: 2, tension: 0.2 }]
    },
    options: { plugins: { title: { display: true, text: 'Probability Mass Function' } }, scales: { x: { title:{display:true,text:'Trials'} }, y:{ beginAtZero:true, title:{display:true,text:'Probability'} } } }
  });
}

if (typeof Chart !== 'undefined' && cmfCtx) {
  cmfChart = new Chart(cmfCtx, {
    type: 'bar',
    data: {
      labels: cmfData.labels,
      datasets: [{ label: 'CMF', data: cmfData.values, borderColor: 'green', backgroundColor: 'rgba(0,0,0,0)', borderWidth: 2, tension: 0.2 }]
    },
    options: { plugins: { title: { display: true, text: 'Cumulative Mass Function' } }, scales: { x: { title:{display:true,text:'Trials'} }, y:{ beginAtZero:true, title:{display:true,text:'Cumulative Probability'} } } }
  });
}

    }
});
    
