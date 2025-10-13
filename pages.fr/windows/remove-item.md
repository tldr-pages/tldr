# Remove-Item

> Supprime des fichier, des dossiers, ainsi que des clés et sous-clés de registre.
> Cette commande ne peut être exécutée que via PowerShell.
> Plus d'informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Supprime des fichiers ou des clés de registre spécifiques (sans sous-clés) :

`Remove-Item {{chemin\vers\fichier_ou_clé1 , chemin\vers\fichier_ou_clé2 ...}}`

- Supprime des fichiers cachés ou en lecture seule :

`Remove-Item -Force {{chemin\vers\fichier1 , chemin\vers\fichier2 ...}}`

- Supprime des fichiers ou des clés de registre spécifiques en demandant une confirmation interactive avant chaque suppression :

`Remove-Item -Confirm {{chemin\vers\fichier_ou_clé1 , chemin\vers\fichier_ou_clé2 ...}}`

- Supprime des fichiers et répertoires spécifiques de manière récursive (Windows 10 version 1909 ou ultérieure) :

`Remove-Item -Recurse {{chemin\vers\fichier_ou_répertoire1 , chemin\vers\fichier_ou_répertoire2 ...}}`

- Supprime des clés de registre Windows spécifiques et toutes leurs sous-clés :

`Remove-Item -Recurse {{chemin\vers\clé1 , chemin\vers\clé2 ...}}`

- Effectue un test du processus de suppression :

`Remove-Item -WhatIf {{chemin\vers\fichier1 , chemin\vers\fichier2 ...}}`
