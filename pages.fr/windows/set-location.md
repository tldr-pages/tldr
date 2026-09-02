# Set-Location

> Affiche le dossier de travail actuel ou se déplace vers un autre dossier.
> Remarque : cette commande peut uniquement être utilisée via PowerShell.
> Plus d'informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Va dans le dossier spécifié :

`Set-Location {{chemin\vers\dossier}}`

- Va dans un dossier spécifique sur un autre lecteur :

`Set-Location {{C}}:{{chemin\vers\dossier}}`

- Va dans le dossier spécifié et affiche son emplacement :

`Set-Location {{chemin\vers\dossier}} -PassThru`

- Remonte au dossier parent du dossier actuel :

`Set-Location ..`

- Va dans le dossier personnel de l’utilisateur actuel :

`Set-Location ~`

- Retourne au dossier précédemment sélectionné ou avance vers le suivant :

`Set-Location {{-|+}}`

- Va à la racine du lecteur actuel :

`Set-Location \`
