# Référence Absolue Universelle (RAU) - README

## Axiome Fondamental

Le projet de Référence Absolue Universelle (RAU) repose sur l'axiome suivant :

\[ 0 = 0 \]

Cet axiome, d'une simplicité déconcertante, est le fondement de toutes les opérations, validations, et calculs effectués dans ce projet. Il sert de référence absolue et immuable dans l'univers de RAU.

## Objectif du Projet

L'objectif principal du projet est de fournir une structure simple, vérifiable et empiriquement prouvable qui peut être appliquée à des calculs dans diverses dimensions.

## Connexion au Réseau

Pour interagir avec le réseau Ethereum via Metamask ou tout autre matériel compatible, utilisez le bouton ci-dessous.

<button id="connectButton">Connecter au Réseau</button>

<script>
document.getElementById('connectButton').onclick = async function() {
    if (typeof window.ethereum !== 'undefined') {
        // Metamask détecté
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connecté à Metamask');
        } catch (error) {
            console.error('Erreur de connexion à Metamask', error);
        }
    } else if (typeof window.web3 !== 'undefined') {
        // Legacy dApp browsers
        alert('Votre navigateur est configuré pour fonctionner avec une ancienne version de Web3.');
    } else if (/Android|iPhone/i.test(navigator.userAgent)) {
        // Mobile detection
        alert('Veuillez utiliser une application mobile compatible avec Ethereum.');
    } else {
        alert('Metamask n\'est pas installé. Veuillez installer Metamask ou utiliser un appareil compatible.');
    }
};
</script>

## Instructions pour l'Utilisation

1. **Cloner le Repository**

   Clonez le projet à partir de GitHub en utilisant la commande suivante :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repository.git
   cd votre-repository