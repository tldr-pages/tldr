# Add-AppxPackage

> Una utilidad de PowerShell para agregar un paquete de aplicación firmado (`.appx`, `.msix`, `.appxbundle` y `.msixbundle`) a una cuenta de usuario.
> Más información: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- Agregar un paquete de aplicación:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}}`

- Agregar un paquete de aplicación con dependencias:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}} -DependencyPath {{ruta\a\dependencias.msix}}`

- Instalar una aplicación utilizando el archivo del instalador de la aplicación:

`Add-AppxPackage -AppInstallerFile {{ruta\al\app.appinstaller}}`

- Agregar un paquete no firmado:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}} -DependencyPath {{ruta\a\dependencias.msix}} -AllowUnsigned`
