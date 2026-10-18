# Marche aléatoire 1D/2D
## Objectif 
 Le but de ce projet est de simuler des marches aléatoires en une et deux dimensions à l'aide de Python. En une dimension, la particule se déplace sur une droite ; en deux dimensions, elle se déplace dans un plan. Ce projet constitue une première approche des processus stochastiques et permet d'introduire le lien entre les marches aléatoires discrètes et le mouvement brownien.
## Langage de programmation
  Python 
## Interface de programmation 
  Spyder 
## Bibliothèques utilisées 
  ### Matplotlib 
  Pour la représentation des graphiques
  ### Random 
  Pour générer des valeurs aléatoires 
  ### NumPy 
  Utilisée pour générer les données numériques afin de tracer les droites représentant les bornes de la marche aléatoire en 1D.  
# Marche aléatoire 1D
  Ici, on suppose la particule dans un tube très fin et se déplace à chaque pas de temps aléatoirement vers la gauche ou la droite. Pour illustrer cela, j'ai utilisé dans mon code deux fonctions Pile_ou_face() et Position(N). J'ai également utilisé la fonction Position_bornee() pour stopper la simulation de la marche aléatoire de la particule si celle-ci atteint (-30) ou (30) ou si le programme atteint un nombre d'itérations maximum (10000). 
  ### Pile_ou_face()
  Cette fonction utilise la fonction Random.uniform() du module Random pour retourner aléatoirement (-1) ou (1) avec P(-1)= P(1) = 1/2. Ici P(-1) (respectivement P(1)) représente la probabilité d'obtenir (-1) (resp. (1)).
  
  ### Position(N) 
  Pour cette fonction, j'ai supposé que la particule se trouve a l'origine du repère (x = 0) à l'instant initial. Cette fonction prend donc en argument un entier N et renvoie une liste de positions de la particule à des instants successifs de t(0) à t(N). La formule générale utilisée est x(n+1) = x(n) + Pile_ou_face() avec n un instant quelconque et x(n) la position de la particule à cet instant. 
   #### Illustration graphique
  <p align = "center"> <img width="377" height="268" alt="Position 1D" src="https://github.com/user-attachments/assets/7aeef90f-5a41-4c5a-9d61-19e0f3422fe1" />
<img width="371" height="268" alt="Position 1D v2" src="https://github.com/user-attachments/assets/e609ca3c-1eef-48a0-bd27-001c876aac98" /> </p> Pour le graphique de gauche, N = 1000 et pour celui de droite, N = 100.
   
  ### Position_bornee() 
   Cette fonction calcule  et renvoie une liste des positions successives de la particule. La simulation s'arrête lorsque la position atteint (-30) ou (30) ou lorsque le nombre maximal d'itérations est atteint (10000). Les bornes constituent ici des seuils d'arrêt de la simulation.
   #### Illustration graphique 
   <p align = "center"> <img width="387" height="268" alt="Position Bornee" src="https://github.com/user-attachments/assets/8181fe59-cbaa-4d9a-9864-7e32937836f8" />
<img width="387" height="268" alt="Position Bornee v2" src="https://github.com/user-attachments/assets/5ae5aaf0-35a3-4a47-b470-412c0a43b605" /> </p> 

### Illustration graphique marche aléatoire bornée et non bornée
<p align = "center"> <img width="387" height="268" alt="Marche 1d" src="https://github.com/user-attachments/assets/ebf1465f-33a0-413f-98d8-1e1fa499b64b" />
<img width="387" height="268" alt="Marche 1d v2" src="https://github.com/user-attachments/assets/d4404b53-69c0-495d-8836-e745aae54239" /> </p> 

# Marche aléatoire 2D 
 Ici, la particule est sortie du tube très fin et peut maintenant se déplacer dans quatre directions : la gauche, la droite, en haut et en bas. Pour illustrer cela, j'ai utilisé dans mon code deux fonctions boussole() et Position_2D(N). 
 ### boussole() 
 Cette fonction utilise la fonction Random.uniform() pour retourner aléatoirement un couple de valeur parmi les couples (0,1); (0,-1); (1,0); (-1,0) avec pour chaque couple une probabilité de 1/4. Ces couples représentent les quatre directions que peut prendre la particule.
 ### Position_2D(N) 
 On suppose que la particule se trouve à l'origine du repère, de coordonnées (0,0), à l'instant initial. Cette fonction prend en argument un entier N et retourne deux listes X pour les abscisses et Y pour les ordonnées. Ces deux listes représentent les positions (coordonnées) de la particule (X(i); Y(i)) à l'instant t(i) avec i compris entre 0 et N. 
 ### Illustration graphique 
 <p align = "center"> <img width="450" height="300" alt="Position 2D" src="https://github.com/user-attachments/assets/cdba7e67-868f-460d-a525-1bdef6567a38" />
<img width="450" height="300" alt="Position 2D v2" src="https://github.com/user-attachments/assets/b31d0768-938b-4fe2-b2f9-0df1d9a1204d" /> </p> 
Pour le graphe de gauche, N = 10000 et pour celui de droite, N =  1000

## Remarque 
 Le mouvement brownien est un processus stochastique à trajectoires continues qui modélise des évolutions aléatoires. En physique, il peut notamment représenter le mouvement irrégulier d'une particule microscopique en suspension dans un fluide, soumis aux interactions avec les molécules environnantes.

Le programme présenté ici simule des marches aléatoires discrètes : la position évolue par étapes successives. Ces simulations illustrent le caractère aléatoire des trajectoires, mais elles ne constituent pas, à elles seules, une approximation explicite du mouvement brownien.

Une telle approximation peut être construite en redimensionnant convenablement le temps et les positions de la marche aléatoire, puis en étudiant le comportement obtenu lorsque le nombre d'étapes augmente.

# Conclusion

 Ce projet m'a permis d'étudier et de simuler des marches aléatoires en une et deux dimensions à l'aide du langage de programmation Python, notamment avec les bibliothèques NumPy et Matplotlib.

Les simulations montrent comment une succession de déplacements aléatoires élémentaires peut produire une trajectoire complexe, même lorsque les règles de déplacement sont simples. En une dimension, la position évolue à chaque étape de (+1) ou de (-1), tandis qu'en deux dimensions, le déplacement s'effectue aléatoirement dans l'une des quatre directions cardinales.

Ce travail m'a également permis d'explorer une marche aléatoire avec des limites, qui s'arrête lorsque la position atteint une borne définie. Cette simulation illustre comment des contraintes peuvent être intégrées à un modèle probabiliste.

Enfin, ce projet constitue une première approche de la modélisation stochastique et ouvre la voie à l'étude du mouvement brownien, qui peut être obtenu comme limite continue appropriée de marches aléatoires convenablement redimensionnées.

Il m'a permis de renforcer mes compétences en programmation Python, en visualisation de données et en simulation numérique, tout en mettant en évidence le lien entre probabilités, algorithmes et phénomènes aléatoires.


  
