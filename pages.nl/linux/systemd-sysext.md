# systemd-sysext

> Activeer of deactiveer systeemextensie-images.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/systemd-sysext.html>.

- Toon geïnstalleerde extensie-images:

`systemd-sysext list`

- Voeg systeemextensie-images samen in `/usr/` en `/opt/`:

`systemd-sysext merge`

- Toon de huidige status van het samenvoegen:

`systemd-sysext`

- Draai het samenvoegen van alle huidig geïnstalleerde systeemextensie-images terug in `/usr/` en `/opt/`:

`systemd-sysext unmerge`

- Ververs de systeemextensie-images (een combinatie van `unmerge` en `merge`):

`systemd-sysext refresh`
