# physlock

> Blocați toate consolele și terminalele virtuale.
> Mai multe informaţii: <http://github.com/muennich/physlock>

- Blocați fiecare consolă (necesită utilizator curent sau root pentru a debloca):

`physlock`

- Mute mesaje kernel pe consola în timp ce blocat:

`physlock -m`

- Dezactivați mecanismul SysRQ în timp ce blocat:

`physlock -s`

- Afișați un mesaj înainte de solicitarea parolei:

`physlock -p "{{Locked!}}"`

- Fork și detașare Physlock (util pentru scripturi de suspendare sau hibernare):

`physlock -d`
