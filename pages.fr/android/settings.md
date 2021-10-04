# settings

> Récupère les informations du système d'exploitation Android.
> Plus d'informations : <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Affiche une liste des paramètres de l'espace de nom `global` :

`settings list {{global}}`

- Récupère la valeur d'un paramètre :

`settings get {{global}} {{airplane_mode_on}}`

- Assigne une valeur à un paramètre :

`settings put {{system}} {{screen_brightness}} {{42}}`

- Supprime un paramètre :

`settings delete {{secure}} {{screensaver_enabled}}`
