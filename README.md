<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
    <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
</head>
<body>
    <h1>MetaMask Integration Test</h1>
    <button id="connectButton">Connect MetaMask</button>
    <p id="accountInfo"></p>

    <script>
        document.getElementById('connectButton').addEventListener('click', async function() {
            if (typeof window.ethereum !== 'undefined') {
                try {
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await ethereum.request({ method: 'eth_accounts' });
                    document.getElementById('accountInfo').innerText = 'Connected account: ' + accounts[0];
                } catch (error) {
                    console.error('Error connecting to MetaMask:', error);
                    document.getElementById('accountInfo').innerText = 'Error connecting to MetaMask.';
                }
            } else {
                alert('MetaMask not detected. Please install MetaMask.');
                window.location.href = 'https://metamask.io/download.html'; // Redirect to MetaMask download
            }
        });
    </script>
</body>
</html>