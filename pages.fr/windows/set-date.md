# Set-Date

> Modifie l’heure système de l’ordinateur pour l’heure spécifié.
> Remarque : cette commande peut uniquement être utilisée via PowerShell.
> Plus d'informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- Ajoute trois jours à la date système :

`Set-Date -Date (Get-Date).AddDays({{3}})`

- Recule l’horloge système de 10 minutes :

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- Ajoute 90 minutes à l’horloge système :

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`
