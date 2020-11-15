# Projet Snowplow

Ce paragraphe décrit un algorithme permettant de construire un chemin dont on espère qu’il sera le plus court.

Il part d’un ensemble de maison où doit se rendre un chasse neige pour construire un parcours optimal. Cet algorithme utilise un chemin hamiltonien. Un chemin hamiltonien d’un graphe est un chemin passant par tous les nœuds de ce graphe.

On suppose qu’il faut déterminer le plus court chemin passant par n maisons. L’algorithme se décompose en quatre étapes :

- Quadrillage des sommets en **NB_ZONES** contenant **HOUSE_PER_ZONE** maisons.

- (_NON EFFECTUÉ POUR L'EXERCICE_)
  Construction d’arbres de poids minimum : grâce au points précédent, on peut ainsi se contenter de construire l’arbre de poids minimal à l’aide des arêtes entre les nœuds de même zone. Le nombre d'arêtes envisagés est majoré par : **HOUSE_PER_ZONE** \* n.

- (_NON EFFECTUÉ POUR L'EXERCICE_)
  Tri des sommets des APM selon un chemin eulérien (dans notre cas, le “graphe” est considéré comme fortement connexe car les points sont liés de façon linéaire, ce point-là ne s’applique donc pas).

  Le “graphe” obtenu par l’algorithme est dans notre cas non orienté. Il est possible de passer d’une maison à une autre puis d’en revenir. Par conséquent, il est possible de construire un chemin qui passe une seule fois par tous les arcs du graphe. Le coût de cet algorithme est en O(n).

  Si possible, création d’un circuit hamiltonien depuis le chemin eulérien en évitant cette fois-ci les nœuds déjà parcourus. Il y aura possibilité de passer par des nœuds n’appartenant pas à l’APM.

  On parcourt les zones en commençant par celle ayant le poids le plus faible. Au passage on ajoute les nœuds que l’on croise en chemin vers la première arêtes de la zone

#### Complexité :

- O(**NB_ZONES** \*nlog(n)) où n est le nombre d’arêtes dans le graphe par **NB_ZONES** (algorithme de Kruskal: détermination des arbres de poids minimal.)

- O(n) Concernant la détermination des chemins eulériens, l’algorithme de Hierholzer

Rayanne Bouslimi & Nathan Douillet
