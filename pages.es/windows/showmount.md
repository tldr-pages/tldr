# showmount

> Muestra información sobre sistemas de archivos NFS en Windows Server.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- Mostrar todos los sistemas de archivos exportados:

`showmount -e`

- Mostrar todos los clientes NFS y sus directorios montados:

`showmount -a`

- Mostrar todos los directorios NFS montados:

`showmount -d`

- Mostrar todos los sistemas de archivos exportados para un servidor remoto:

`showmount -e {{dirección_del_servidor}}`
