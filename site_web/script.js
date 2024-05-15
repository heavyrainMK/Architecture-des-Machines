document.addEventListener("DOMContentLoaded", function() {
    var boutonChangerCouleur = document.createElement("button"); // Création d'un bouton pour changer la couleur
    boutonChangerCouleur.textContent = "Changer la couleur"; // Texte du bouton
    boutonChangerCouleur.classList.add("btn", "btn-primary"); // Ajout des classes Bootstrap pour le style
    boutonChangerCouleur.style.backgroundColor = "#2c3e50"; // Couleur de fond du bouton
    boutonChangerCouleur.style.color = "white"; // Couleur du texte

    boutonChangerCouleur.onclick = function() {
        var couleurAleatoire = getCouleurAleatoire(); // Fonction pour obtenir une couleur aléatoire
        document.body.style.backgroundColor = couleurAleatoire; // Changement de la couleur de fond du body
    };

    // Ajout du bouton "Changer la couleur" au body
    document.body.appendChild(boutonChangerCouleur);

    // Style pour positionner le bouton "Changer la couleur" dans le coin supérieur gauche
    boutonChangerCouleur.style.position = "absolute";
    boutonChangerCouleur.style.top = "10px";
    boutonChangerCouleur.style.left = "10px";

    // Bouton pour rétablir la couleur de fond par défaut
    var boutonRetablirDefaut = document.createElement("button");
    boutonRetablirDefaut.textContent = "Couleur par défaut";
    boutonRetablirDefaut.classList.add("btn", "btn-secondary", "ml-2"); // Ajout des classes Bootstrap pour le style

    boutonRetablirDefaut.onclick = function() {
        document.body.style.backgroundColor = ""; // Rétablir la couleur de fond par défaut
    };

    // Ajout du bouton "Couleur par défaut" au body
    document.body.appendChild(boutonRetablirDefaut);

    // Style pour positionner le bouton "Couleur par défaut" dans le coin supérieur droit
    boutonRetablirDefaut.style.position = "absolute";
    boutonRetablirDefaut.style.top = "10px";
    boutonRetablirDefaut.style.right = "10px";
});

// Fonction pour obtenir une couleur aléatoire
function getCouleurAleatoire() {
    var lettres = "0123456789ABCDEF";
    var couleur = "#";
    for (var i = 0; i < 6; i++) {
        couleur += lettres[Math.floor(Math.random() * 16)];
    }
    return couleur;
}
