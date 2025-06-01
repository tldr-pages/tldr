# winget

> Administrador de paquetes de Windows.
> Más información: <https://learn.microsoft.com/windows/package-manager/winget>.

- Instalar un paquete:
  
`winget install {{paquete}}`

- Eliminar un paquete (Nota: `remove` también se puede usar en lugar de `uninstall`):
  
`winget uninstall {{paquete}}`

- Mostrar información sobre un paquete:
  
`winget show {{paquete}}`

- Buscar un paquete:
  
`winget search {{paquete}}`

- Actualizar todos los paquetes a las versiones más recientes:
  
`winget upgrade --all`

- Listar todos los paquetes instalados que se pueden gestionar con `winget`:
  
`winget list --source winget`

- Importar paquetes desde un archivo o exportar paquetes instalados a un archivo:
  
`winget {{importar|exportar}} {{--importar-archivo|--salida}} {{ruta/al/archivo}}`

- Validar manifiestos antes de enviar un PR al repositorio winget-pkgs:
  
`winget validate {{ruta/al/manifiesto}}`
