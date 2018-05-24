#!/bin/bash

read -p 'Voulez-vous lancer le prétaitement? [o/n] ' decision
read -p 'Combien de foyer voulez-vous ? ' nb_foyer

if [[ "$decision" = "o" ]]; then
	python pretraitement.py $nb_foyer
fi

echo "Assurez-vous que l'exécutable matlab est bien dans /opt/matlab/R2015b/bin. Sinon changez la variable d'environnement PATH."

export PATH="/opt/matlab/R2015b/bin:$PATH"

matlab -nodisplay -nodesktop -r "run OptiNbProduction"

nbPanneaux=$(head -1 nb_devices.txt)
nbEolienne=$(tail -1 nb_devices.txt)


echo $nbPanneaux
echo $nbEolienne

python traitement.py $nb_foyer $nbPanneaux $nbEolienne



