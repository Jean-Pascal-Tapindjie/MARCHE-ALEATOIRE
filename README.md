# Marche aléatoire 1D et 2D
## Objectif : 
 Le but de cet exercice est de simuler la marche aléatoire d'une particule dans un tube (en une dimension) et hors du tube (en deux dimensions). Cet exercice permet donc de comprendre comment une marche aléatoire peut servir à approximer un mouvement Brownien qui est une modélisation aléatoire de l'évolution d'une particule au cours du temps.
## Langage de programmation:
  Python 
## Interface de programmation :
  Spyder 
## Bibliothèques utilisées :
  ### Matplotlib : 
  Pour la représentation des graphiques
  ### Random : 
  Pour utiliser des valeurs aléatoires 
  ### Numpy : 
  Utiliser pour borner graphiquement la marche aléatoire en 1D  
# Marche aléatoire 1D
  Ici, on suppose la particule dans un tube très fin et se déplace entre chaque pas de temps aléatoirement vers la gauche ou la droite. Pour illustrer cela, j'ai utilisé dans mon code deux fonctions Pile_ou_face() et Position(N). J'ai également utilisé la fonction Position_bornée(N) pour stopper la simulation de la marche aléatoire de la particule entre -30 et 30 ou si l'on atteint un nombre d'itérations maximum (10000). 
  ### Pile_ou_face():
  Cette fonction utilise la bibliothèque Random pour retourne aléatoirement (-1) ou (1) avec P(-1)= P(1) = 1/2. Ici P(-1) (respectivement P(1)) représente la probabilité d'obtenir (-1) (resp. (1)).
  ### Position (N) :
  
