# arduino

> Arduino Studio - Environnement de Développement Intégré pour la plateforme Arduino.
> Plus d'informations : <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Construis un croquis :

`arduino --verify {{chemin/vers/croquis.ino}}`

- Construis et téléverse un croquis :

`arduino --upload {{chemin/vers/croquis.ino}}`

- Construis et téléverse un croquis vers un Arduino Nano avec un CPU Atmega328p, connecté sur le port `/dev/ttyACM0` :

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{chemin/vers/croquis.ino}}`

- Configure la préférence `nom` à une valeur `valeur` :

`arduino --pref {{nom}}={{valeur}}`

- Construis un croquis, mets le résultat de ce dernier dans un dossier, et réutilise n'importe quelles versions précédentes dans ce dossier :

`arduino --pref build.path={{chemin/vers/dossier/de/construction}} --verify {{chemin/vers/croquis.ino}}`

- Sauvegarde toutes préférences (modifiées) dans un fichier `preferences.txt` :

`arduino --save-prefs`
