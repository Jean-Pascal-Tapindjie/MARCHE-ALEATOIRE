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
  Pour générer des valeurs aléatoires 
  ### Numpy : 
  Utiliser tracer deux droites pour borner graphiquement la marche aléatoire en 1D  
# Marche aléatoire 1D
  Ici, on suppose la particule dans un tube très fin et se déplace entre chaque pas de temps aléatoirement vers la gauche ou la droite. Pour illustrer cela, j'ai utilisé dans mon code deux fonctions Pile_ou_face() et Position(N). J'ai également utilisé la fonction Position_bornee() pour stopper la simulation de la marche aléatoire de la particule si celle si atteint (-30) ou (30) ou si le programme atteint un nombre d'itérations maximum (10000). 
  ### Pile_ou_face():
  Cette fonction utilise la bibliothèque Random pour retourne aléatoirement (-1) ou (1) avec P(-1)= P(1) = 1/2. Ici P(-1) (respectivement P(1)) représente la probabilité d'obtenir (-1) (resp. (1)).
  ### Position (N) :
  Pour cette fonction, j'ai supposé que la particule se trouve a l'origine du repère ( x = 0 ) à l'instant initial. Cette fonction prend donc en argument un entier N et renvoie une liste de positions de la particule à des instants successifs de t(0) à t(N). La formule générale utilisée est x(n+1) = x(n) + Pile_ou_face() avec n un instant quelconque et x(n) la position de la particule à cet instant. 
   #### Illustration graphique: 
  <p align = "center"> <img width="377" height="268" alt="Position 1D" src="https://github.com/user-attachments/assets/7aeef90f-5a41-4c5a-9d61-19e0f3422fe1" />
<img width="371" height="268" alt="Position 1D v2" src="https://github.com/user-attachments/assets/e609ca3c-1eef-48a0-bd27-001c876aac98" /> </p> Pour le graphique de gauche, N = 1000 et pour celui de droite, N = 100.
   
  ### Position_bornee() :
   Cette fonction calcule  et renvoie une liste des positions successives de la particule jusqu'à ce qu'elle atteigne (-30) ou (30) ou bien jusqu'à ce que le nombre d'itérations atteigne 10000. Elle sert donc à arrêter la simulation de la marche aléatoire sous ces deux conditions ci-dessus.
   #### Illustration graphique :
   <p align = "center"> <img width="387" height="268" alt="Position Bornee" src="https://github.com/user-attachments/assets/8181fe59-cbaa-4d9a-9864-7e32937836f8" />
<img width="387" height="268" alt="Position Bornee v2" src="https://github.com/user-attachments/assets/5ae5aaf0-35a3-4a47-b470-412c0a43b605" /> </p> 

### Illustration graphique marche aléatoire bornée et non bornée
<p align = "center"> <img width="387" height="268" alt="Marche 1d" src="https://github.com/user-attachments/assets/ebf1465f-33a0-413f-98d8-1e1fa499b64b" />
<img width="387" height="268" alt="Marche 1d v2" src="https://github.com/user-attachments/assets/d4404b53-69c0-495d-8836-e745aae54239" /> </p> 

# Marche aléatoire 2D 



  
