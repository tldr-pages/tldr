# fping

> Un ping mai puternic, care poate ping mai multe gazde.
> Mai multe informaţii: <https://fping.org>

- Lista gazdelor vii dintr-o subrețea generată de la o netmask:

`fping -a -g 192.168.1.0/24`

- Lista gazdelor vii dintr-o subrețea generată dintr-un interval IP:

`fping -a -g 192.168.1.1 192.168.1.254`

- Lista gazdelor inaccesibile într-o subrețea generată de la o netmask:

`fping -u -g 192.168.1.0/24`
