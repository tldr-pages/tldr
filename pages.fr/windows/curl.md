# curl

> Dans PowerShell, cette commande peut être un alias de `Invoke-WebRequest` lorsque le programme original `curl` (<https://curl.se>) n'est pas correctement installé.
> Plus d'informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Affiche la documentation de la commande `curl` originale :

`tldr curl -p common`

- Affiche la documentation de la commande PowerShell `Invoke-WebRequest` :

`tldr invoke-webrequest`

- Vérifie si `curl` est correctement installé en affichant son numéro de version. Si cette commande renvoie une erreur, PowerShell a peut-être remplacé cette commande par `Invoke-WebRequest` :

`curl --version`
