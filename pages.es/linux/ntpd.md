# ntpd

> El daemon oficial de NTP (Network Time Protocol) para sincronizar el reloj del sistema con servidores de tiempo remotos o relojes de referencia locales.
> Más información: <https://manned.org/ntpd>.

- Inicia el daemon:

`sudo ntpd`

- Sincroniza la hora del sistema con servidores remotos una sola vez (sale después de sincronizar):

`sudo ntpd --quit`

- Sincroniza una sola vez permitiendo "grandes" ajustes:

`sudo ntpd --panicgate --quit`
