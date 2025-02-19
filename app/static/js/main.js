function process(operation) {
    const key = document.getElementById('key').value;
    const text = document.getElementById('text').value;

    if (!key || !text) {
        showError('Please enter both key and text');
        return;
    }

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: operation,
            key: key,
            text: text
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displayMatrix(data.matrix);
            displayResult(data.result);
        } else {
            showError(data.error);
        }
    })
    .catch(error => {
        showError('An error occurred. Please try again.');
    });
}

function displayMatrix(matrix) {
    const container = document.getElementById('matrix');
    container.innerHTML = '';
    
    matrix.forEach(row => {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'matrix-row';
        
        row.forEach(cell => {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'matrix-cell';
            cellDiv.textContent = cell;
            rowDiv.appendChild(cellDiv);
        });
        
        container.appendChild(rowDiv);
    });
}

function displayResult(result) {
    const container = document.getElementById('result');
    container.innerHTML = result;
}

function showError(message) {
    const resultContainer = document.getElementById('result');
    resultContainer.innerHTML = `<div class="error-message">${message}</div>`;
}

function resetForm() {
    document.getElementById('key').value = '';
    document.getElementById('text').value = '';
    document.getElementById('matrix').innerHTML = '';
    document.getElementById('result').innerHTML = '';
} 