# Set-Service

> Démarre, arrête et suspend un service, et modifie ses propriétés.
> Remarque : cette commande peut uniquement être utilisée via PowerShell.
> Plus d’informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-service>.

- Modifie un nom d’affichage :

`Set-Service -Name {{nom_hôte}} -DisplayName "{{nom}}"`

- Modifie le type de démarrage des services :

`Set-Service -Name {{nom_service}} -StartupType {{Automatic}}`

- Modifie la description d’un service :

`Set-Service -Name {{nom_service}} -Description "{{description}}"`
