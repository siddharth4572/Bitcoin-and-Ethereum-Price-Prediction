// frontend/js/script.js
document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const open = parseFloat(document.getElementById('open').value);
    const high = parseFloat(document.getElementById('high').value);
    const low = parseFloat(document.getElementById('low').value);
    const volume = parseFloat(document.getElementById('volume').value);

    const data = [{
        Open: open,
        High: high,
        Low: low,
        Volume: volume
    }];

    // Fetch prediction for BTC
    fetch('/predict/btc', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `Predicted BTC Price: $${data.prediction[0].toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error predicting BTC price.';
    });
});

// Event listener for predicting ETH price
document.getElementById('predict-eth').addEventListener('click', function() {
    const open = parseFloat(document.getElementById('open').value);
    const high = parseFloat(document.getElementById('high').value);
    const low = parseFloat(document.getElementById('low').value);
    const volume = parseFloat(document.getElementById('volume').value);

    const data = [{
        Open: open,
        High: high,
        Low: low,
        Volume: volume
    }];

    // Fetch prediction for ETH
    fetch('/predict/eth', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML += `<br>Predicted ETH Price: $${data.prediction[0].toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML += '<br>Error predicting ETH price.';
    });
});