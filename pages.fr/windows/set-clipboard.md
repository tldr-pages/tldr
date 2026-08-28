# Set-Clipboard

> Commande PowerShell permettant de placer du contenu dans le presse-papiers.
> Remarque : `scb` peut être utilisé comme alias pour `Set-Clipboard`.
> Plus d’informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-clipboard>.

- Copie du texte dans le presse-papiers :

`Set-Clipboard -Value "{{texte}}"`

- Copie plusieurs textes dans le presse-papiers, séparés par une nouvelle ligne :

`Set-Clipboard -Value @("{{texte 1}}", "{{texte 2}}", "{{texte 3}}")`

- Copie des fichiers ou des dossiers dans le presse-papiers :

`Set-Clipboard -Path "{{chemin\vers\fichiers_ou_dossiers}}"`

- Copie plusieurs fichiers :

`Set-Clipboard -Path "{{chemin\vers\fichier1}}","{{chemin\vers\fichier2}}","{{chemin\vers\fichier3}}"`

- Efface le presse-papiers :

`Set-Clipboard ""`
