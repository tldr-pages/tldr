# arduino-builder

> Un outil en ligne de commande pour compiler des croquis arduino.
> AVERTISSEMENT DE DÉPRÉCIATION: Cet outil a été retiré au profit de `arduino`.
> Plus d'informations : <https://github.com/arduino/arduino-builder>.

- Construis un croquis :

`arduino-builder -compile {{chemin/vers/croquis.ino}}`

- Spécifie the niveau de débogage (1 à 10, 5 par défaut) :

`arduino-builder -debug-level {{niveau}}`

- Spécifie un dossier de construction :

`arduino-builder -build-path {{chemin/vers/dossier/de/construction}}`

- Utilise un fichier d'option de construction, au lieu de spécifier `--hardware`, `--tools`, etc. Manuellement à chaque fois :

`arduino-builder -build-options-file {{chemin/vers/construction.options.json}}`

- Active le mode verbeux :

`arduino-builder -verbose {{true}}`
