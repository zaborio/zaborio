# Référence Absolue Universelle (RAU) - README

## Axiome Fondamental

Le projet de Référence Absolue Universelle (RAU) repose sur l'axiome suivant :

\[ 0 = 0 \]

Cet axiome, d'une simplicité déconcertante, est le fondement de toutes les opérations, validations, et calculs effectués dans ce projet. Il sert de référence absolue et immuable dans l'univers de RAU.

## Objectif du Projet

L'objectif principal du projet est de fournir une structure simple, vérifiable et empiriquement prouvable qui peut être appliquée à des calculs dans diverses dimensions, en commençant par le calcul de Pi dans la dimension 1.

## Connexion au Réseau

Pour interagir avec le réseau Ethereum via Metamask, utilisez le bouton ci-dessous.

<button id="connectButton">Connecter au Réseau</button>

<script>
document.getElementById('connectButton').onclick = async function() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connecté à Metamask');
        } catch (error) {
            console.error('Erreur de connexion à Metamask', error);
        }
    } else {
        alert('Metamask n\'est pas installé. Veuillez installer Metamask et réessayer.');
    }
};
</script>

## Instructions pour l'Utilisation

1. **Cloner le Repository**

   Clonez le projet à partir de GitHub en utilisant la commande suivante :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repository.git
   cd votre-repository