function detectText() {
    const content = document.getElementById('textInput').value;

    fetch('/detect', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = "Detection Result: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = "Error occurred during detection.";
    });
}
