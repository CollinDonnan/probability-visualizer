enter = document.getElementById("enter");
distros = document.getElementById("distros");
output = document.getElementById("output");

enter.addEventListener("click", () => {
    let distro = distros.value.toLowerCase();
    let n = 1; // Example value, you can modify this as needed

    fetch(`/${distro}/${n}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        output.innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});