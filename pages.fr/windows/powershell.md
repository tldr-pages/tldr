# powershell

> Interface en ligne de commande et langage de script spécialement conçu pour l'administration système.
> Plus d'informations : <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Démarre une session Windows PowerShell dans une fenêtre d'invite de commande :

`powershell`

- Charge un fichier de console PowerShell spécifique :

`powershell -PSConsoleFile {{chemin/vers/fichier}}`

- Démarre une session avec une version spécifiée de PowerShell :

`powershell -Version {{version}}`

- Empêche l’interface système de se fermer après avoir exécuté les commandes de démarrage :

`powershell -NoExit`

- Décrive le format des données envoyées à PowerShell :

`powershell -InputFormat {{Texte|XML}}`

- Détermine comment la sortie de PowerShell est formatée :

`powershell -OutputFormat {{Texte|XML}}`

- Affiche l'aide :

`powershell -Help`
