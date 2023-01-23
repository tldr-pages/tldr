# showmount

> A Windows Server NFS fájlrendszereire vonatkozó információk megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- Az összes exportált fájlrendszer megjelenítése:

`showmount -e`

- Az összes NFS-ügyfél és az általuk csatlakoztatott könyvtárak megjelenítése:

`showmount -a`

- Az összes NFS-csatlakoztatott könyvtár megjelenítése:

`showmount -d`

- Egy távoli kiszolgáló összes exportált fájlrendszerének megjelenítése:

`showmount -e {{server_address}}`
