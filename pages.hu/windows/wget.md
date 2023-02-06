# wget

> A PowerShellben ez a parancs a `Invoke-WebRequest` aliasza lehet, ha az eredeti `wget` program[(https://www.gnu.org/software/wget](https://www.gnu.org/software/wget)) nincs megfelelően telepítve.

- Ellenőrizze, hogy a `wget` megfelelően telepítve van-e, a verziószámának kinyomtatásával. Ha ez a parancs hibaüzenetet ad ki, akkor a PowerShell ezt a parancsot a `Invoke-WebRequest` parancsra cserélhette:

`curl --version`

- Az eredeti `wget` parancs dokumentációjának megtekintése:

`tldr wget -p common`

- Az eredeti `wget` parancs dokumentációjának megtekintése a `tldr` parancssori kliens régebbi verzióiban:

`tldr wget -o common`

- A PowerShell `Invoke-WebRequest` parancsának dokumentációjának megtekintése:

`tldr invoke-webrequest`
