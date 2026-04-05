async function getHealthData() {
    const disease = document.getElementById("disease").value;
    const output = document.getElementById("output");

    if (!disease) {
        output.innerHTML = "Please select a disease";
        return;
    }

    const res = await fetch('/get-health-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ disease })
    });

    const data = await res.json();

    output.innerHTML = `
        <h3>Health Details</h3>
        <p><b>Advice:</b> ${data.advice}</p>
        <p><b>Diet:</b> ${data.diet}</p>
        <p><b>Exercise:</b> ${data.exercise}</p>
    `;
}