# Add-AppxPackage

> Una utilidad de PowerShell para agregar un paquete de aplicación firmado (`.appx`, `.msix`, `.appxbundle` y `.msixbundle`) a una cuenta de usuario.
> Más información: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- Agrega un paquete de aplicación:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}}`

- Agrega un paquete de aplicación con dependencias:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}} -DependencyPath {{ruta\a\dependencias.msix}}`

- Instala una aplicación utilizando el archivo del instalador de la aplicación:

`Add-AppxPackage -AppInstallerFile {{ruta\al\app.appinstaller}}`

- Agrega un paquete no firmado:

`Add-AppxPackage -Path {{ruta\al\paquete.msix}} -DependencyPath {{ruta\a\dependencias.msix}} -AllowUnsigned`
