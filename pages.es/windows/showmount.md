# showmount

> Muestra información sobre sistemas de archivos NFS en Windows Server.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- Muestra todos los sistemas de archivos exportados:

`showmount -e`

- Muestra todos los clientes NFS y sus directorios montados:

`showmount -a`

- Muestra todos los directorios NFS montados:

`showmount -d`

- Muestra todos los sistemas de archivos exportados para un servidor remoto:

`showmount -e {{dirección_del_servidor}}`
