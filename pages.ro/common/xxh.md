# xxh

> Adu-ți carcasa cu toate personalizările prin sesiuni SSH.
> Notă: xxh nu instalează nimic în directoarele de sistem de pe mașina țintă; eliminarea `~/.xxh` va șterge toate urmele xxh pe mașina țintă.
> Mai multe informaţii: <https://github.com/xxh/xxh>

- Conectați-vă la o gazdă și executați shell-ul curent:

`xxh "{{host}}"`

- Instalați carcasa curentă în mașina țintă fără a solicita:

`xxh "{{host}}" ++install`

- Rulați carcasa specificată pe mașina țintă:

`xxh "{{host}}" ++shell {{xonsh|zsh|fish|bash|osquery}}`

- Utilizați un director de configurare xxh specific pe mașina țintă:

`xxh "{{host}}" ++host-xxh-home {{~/.xxh}}`

- Utilizați fișierul de configurare specificat pe mașina gazdă:

`xxh "{{host}}" ++xxh-config {{~/.config/xxh/config.xxhc}}`

- Specificați o parolă de utilizat pentru conexiunea SSH:

`xxh "{{host}}" ++password "{{password}}"`

- Instalați un pachet xxh pe mașina țintă:

`xxh "{{host}}" ++install-xxh-packages {{package}}`

- Setați o variabilă de mediu pentru procesul de coajă pe mașina țintă:

`xxh "{{host}}" ++env {{name}}={{value}}`
