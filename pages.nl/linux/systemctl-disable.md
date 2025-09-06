# systemctl disable

> Schakel systemd-services uit.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html#disable%20UNIT%E2%80%A6>.

- Voorkom dat een service automatisch opstart:

`systemctl disable {{eenheid}}`

- Voorkom dat een service automatisch opstart en stop de huidige uitvoering:

`systemctl disable {{eenheid}} --now`
