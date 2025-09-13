# secon

> Krijg de SELinux-beveiligingscontext van een bestand, PID, huidige uitvoeringscontext of een contextspecificatie.
> Zie ook: `semanage`, `runcon`, `chcon`.
> Meer informatie: <https://manned.org/secon>.

- Krijg de beveiligingscontext van de huidige uitvoeringscontext:

`secon`

- Krijg de huidige beveiligingscontext van een proces:

`secon --pid {{1}}`

- Krijg de huidige beveiligingscontext van een bestand, waarbij alle tussenliggende symlinks worden opgelost:

`secon --file {{pad/naar/bestand_of_map}}`

- Krijg de huidige beveiligingscontext van een symlink zelf (d.w.z. niet oplossen):

`secon --link {{pad/naar/symlink}}`

- Parse en leg een contextspecificatie uit:

`secon {{systeem_u:systeem_r:container_t:s0:c899,c900}}`
