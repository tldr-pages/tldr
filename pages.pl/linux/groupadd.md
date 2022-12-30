# groupadd

> Dodaje grupę użytkowników do systemu.
> Zobacz też `groups`, `groupdel`, `groupmod`.
> Więcej informacji: <https://manned.org/groupadd>.

- Utwórz nową grupę:

`sudo groupadd {{nazwa_grupy}}`

- Utwórz nową grupę systemową:

`sudo groupadd --system {{nazwa_grupy}}`

- Utwórz nową grupę z określonym `id_grupy`:

`sudo groupadd --gid {{id_grupy}} {{nazwa_grupy}}`
