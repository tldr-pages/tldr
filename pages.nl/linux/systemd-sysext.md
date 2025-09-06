# systemd-sysext

> Activeer or deactiveer systeem extensie images.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- Toon geïnstalleerde extensie images:

`systemd-sysext list`

- Voeg systeem extensie images samen in `/usr/` en `/opt/`:

`systemd-sysext merge`

- Toon de huidige status van het samenvoegen:

`systemd-sysext status`

- Draai het samenvoegen van alle huidig geïnstalleerde systeem extensie images terug in `/usr/` en `/opt/`:

`systemd-sysext unmerge`

- Ververs de systeem extensie images (een combinatie van `unmerge` and `merge`):

`systemd-sysext refresh`
