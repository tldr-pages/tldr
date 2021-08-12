# dbus-daemon

> Demonul mesajului D-Bus, permițând mai multor programe să facă schimb de mesaje.
> Mai multe informaţii: <https://www.freedesktop.org/wiki/Software/dbus/>

- Rulați daemonul cu un fișier de configurare:

`dbus-daemon --config-file {{path/to/file}}`

- Rulați daemonul cu configurația standard a magistralei de mesaje per-login-sesiune:

`dbus-daemon --session`

- Rulați daemonul cu configurația standard a magistralei de mesaje sistemwide:

`dbus-daemon --system`

- Setați adresa pentru a asculta și suprascrie valoarea de configurare pentru aceasta:

`dbus-daemon --address {{address}}`

- Ieșiți id-ul procesului la stdout:

`dbus-daemon --print-pid`

- Forțați magistrala de mesaje să scrie în jurnalul de sistem pentru mesaje:

`dbus-daemon --syslog`
