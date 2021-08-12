# timedatectl

> Controlați ora și data sistemului.
> Mai multe informaţii: <https://manned.org/timedatectl.1>

- Verificați timpul curent de ceas al sistemului:

`timedatectl`

- Setați ora locală a ceasului sistemului direct:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- Lista fusurilor orare disponibile:

`timedatectl list-timezones`

- Setați fusul orar al sistemului:

`timedatectl set-timezone {{timezone}}`

- Activați sincronizarea Protocol Time Network (NTP):

`timedatectl set-ntp on`
