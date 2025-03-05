document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    // Convert all values to integers
    for (let key in data) {
        data[key] = parseInt(data[key]);
    }

    // Disable submit button and show loading
    const submitButton = e.target.querySelector('button[type="submit"]');
    const resultDiv = document.getElementById('predictionResult');
    
    submitButton.disabled = true;
    submitButton.innerHTML = 'Predicting...';
    resultDiv.innerHTML = '';

    // Send data to backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            if (result.prediction === 'Lung Cancer') {
                resultDiv.innerHTML = `
                    <div class="alert alert-danger result-positive">
                        <strong>High Risk of Lung Cancer</strong>
                        <p>Please consult a healthcare professional for further evaluation.</p>
                    </div>
                `;
            } else {
                resultDiv.innerHTML = `
                    <div class="alert alert-success result-negative">
                        <strong>Low Risk of Lung Cancer</strong>
                        <p>Continue maintaining a healthy lifestyle.</p>
                    </div>
                `;
            }
        } else {
            resultDiv.innerHTML = `
                <div class="alert alert-warning">
                    ${result.error || 'An unexpected error occurred'}
                </div>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = `
            <div class="alert alert-danger">
                Network error. Please try again later.
            </div>
        `;
    })
    .finally(() => {
        // Re-enable submit button
        submitButton.disabled = false;
        submitButton.innerHTML = 'Predict Lung Cancer Risk';
    });
});