# showmount

> Muestra información sobre sistemas de archivos NFS en Windows Server.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- Mostra todos los sistemas de archivos exportados:

`showmount -e`

- Mostra todos los clientes NFS y sus directorios montados:

`showmount -a`

- Mostra todos los directorios NFS montados:

`showmount -d`

- Mostra todos los sistemas de archivos exportados para un servidor remoto:

`showmount -e {{dirección_del_servidor}}`
