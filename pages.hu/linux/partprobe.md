# partprobe

> Értesíti az operációs rendszer kernelét a partíciós tábla változásairól. További információ: <https://manned.org/partprobe>.

- Az operációs rendszer kernelének értesítése a partíciós tábla változásairól:

`sudo partprobe`

- Értesíti a rendszermagot a partíciós tábla változásairól, és megjeleníti az eszközök és partícióik összefoglalóját:

`sudo partprobe --summary`

- Az eszközök és partícióik összefoglalójának megjelenítése, de nem értesíti a rendszermagot:

`sudo partprobe --summary --dry-run`
