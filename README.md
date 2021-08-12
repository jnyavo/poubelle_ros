# poubelle_ros

Ce projet contient un package "projet_poubelle" qui contient un nœud publish_poubelle.py accompagné d'un package "button_gui" qui contient un nœud button_node.py.

Lors de l'exécution, l'état du poubelle est publié dans un topic nommé "/etat_poubelle". <br>
L'état change de "utilisable" à "plein" et vice-versa à chaque fois que le bouton du package "button_gui" est appuyé.<br>
L'identifiant de la poubelle peut être modifié dans publish_poubelle.py en argument sur le constructeur de la classe Publisher (par défaut id:1).

## Pour installer ces packages

copiez-les dans le dossier src de votre espace de travail catkin

```sh
https://github.com/jnyavo/poubelle_ros
cp -r poubelle_ros/projet_poubelle ~/catkin_ws/src
cp -r poubelle_ros/button_gui ~/catkin_ws/src
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
```
## Pour exécuter les deux nœuds
Une fois que le fichier d'installation a été sourcé.

```sh
rosrun button_gui button_node.py
rosrun projet_poubelle publish_poubelle.py
```

## Voir l'état de la poubelle
```sh
rostopic echo /etat_poubelle
```

