#!/bin/bash
# Suppression des fichiers de compilations

echo "Suppression des fichier compilation .pyc de git et du terminal"
find . -name "*.pyc" -exec git rm -f "{}" \;
find . -name "*.pyc" -exec rm -f "{}" \;
echo "Suppression des fichier compilation .m~ de git et du terminal"
find . -name "*.m~" -exec git rm -f "{}" \;
find . -name "*.m~" -exec rm -f "{}" \;



