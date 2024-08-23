<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Game</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.6.1/web3.min.js"></script>
</head>
<body>
    <h1>Crypto Game</h1>
    <button id="connectButton">Connect MetaMask</button>
    <button id="playButton" disabled>Play Game</button>
    <p id="accountInfo"></p>

    <script>
        document.getElementById('connectButton').addEventListener('click', async function() {
            if (typeof window.ethereum !== 'undefined') {
                try {
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await ethereum.request({ method: 'eth_accounts' });
                    document.getElementById('accountInfo').innerText = 'Connected account: ' + accounts[0];
                    document.getElementById('playButton').disabled = false;
                } catch (error) {
                    console.error('Error connecting to MetaMask:', error);
                    document.getElementById('accountInfo').innerText = 'Error connecting to MetaMask.';
                }
            } else {
                alert('MetaMask not detected. Please install MetaMask.');
                window.location.href = 'https://metamask.io/download.html'; // Redirect to MetaMask download
            }
        });

        document.getElementById('playButton').addEventListener('click', async function() {
            // Example function to interact with a smart contract
            if (typeof window.ethereum !== 'undefined') {
                const web3 = new Web3(window.ethereum);
                const contractAddress = '0xYourContractAddress';
                const contractABI = [/* Your Contract ABI */];
                const contract = new web3.eth.Contract(contractABI, contractAddress);
                try {
                    // Call a function from the smart contract
                    const result = await contract.methods.yourFunction().call();
                    console.log(result);
                } catch (error) {
                    console.error('Error interacting with smart contract:', error);
                }
            }
        });
    </script>
</body>
</html>