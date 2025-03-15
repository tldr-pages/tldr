# reboot

> Herstart het systeem.
> Meer informatie: <https://manned.org/reboot.8>.

- Herstart het systeem:

`reboot`

- Schakel het systeem uit (zelfde als `poweroff`):

`reboot {{[-p|--poweroff]}}`

- Houd het systeem (beëindigt alle processen en zet de CPU uit) (zelfde als `halt`):

`reboot --halt`

- Herstart onmiddellijk zonder contact op te nemen met de systeembeheerder:

`reboot {{[-f|--force]}}`

- Schrijf de wtmp shutdown entry zonder het systeem opnieuw te starten:

`reboot {{[-w|--wtmp-only]}}`
