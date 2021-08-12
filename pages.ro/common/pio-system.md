# pio system

> Comenzi de sistem diverse pentru PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/system/>

- Instalați finalizarea coajă pentru carcasa curentă (suportă bash, pește, zsh și powershell):

`pio system completion install`

- Dezinstalare completare coajă pentru shell-ul curent:

`pio system completion uninstall`

- Afișează informații PlatForMio la nivel de sistem:

`pio system info`

- Eliminați datele PlatForMio neutilizate:

`pio system prune`

- Eliminați numai datele memorate în cache:

`pio system prune --cache`

- Lista de date neutilizate PlatForMio care ar fi eliminate, dar nu elimina de fapt:

`pio system prune --dry-run`
