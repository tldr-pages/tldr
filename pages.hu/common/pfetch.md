# pfetch

> Rendszerinformációk megjelenítése. További információ: <https://github.com/dylanaraps/pfetch>.

- Az ASCII art és az alapértelmezett mezők megjelenítése:

`pfetch`

- Csak az ASCII art és a színpaletta mezők megjelenítése:

`PF_INFO="{{ascii palette}}" pfetch`

- Az összes lehetséges mező megjelenítése:

`PF_INFO="{{ascii title os host kernel uptime pkgs memory shell editor wm de palette}}" pfetch`

- Más felhasználónév és hosztnév megjelenítése:

`USER="{{user}}" HOSTNAME="{{hostname}}" pfetch`

- Megjelenítés színek nélkül:

`PF_COLOR={{0}} pfetch`
