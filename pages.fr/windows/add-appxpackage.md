# Add-AppxPackage

> Un utilitaire PowerShell pour ajouter un paquet d'applications signé (`.appx`, `.msix`, `.appxbundle`, `.appxbundle` et `.msixbundle`) à un compte utilisateur.
> Plus d'informations : <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- Ajoute un paquet d'application :

`Add-AppxPackage -Path {{chemin\vers\paquet.msix}}`

- Ajoute un paquet d'application avec ses dependences :

`Add-AppxPackage -Path {{chemin\vers\paquet.msix}} -DependencyPath {{chemin\vers\dependences.msix}}`

- Installe une application en utilisant le fichier d'installation de l'application :

`Add-AppxPackage -AppInstallerFile {{chemin\vers\application.appinstaller}}`

- Ajoute un paquet non signé :

`Add-AppxPackage -Path {{chemin\vers\paquet.msix}} -DependencyPath {{chemin\vers\dependences.msix}} -AllowUnsigned`
