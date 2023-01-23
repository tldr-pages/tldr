# curl

> A PowerShellben ez a parancs a `Invoke-WebRequest` aliasza lehet, ha az eredeti `curl` program[(https://curl.se](https://curl.se)) nincs megfelelően telepítve.

- Ellenőrizze, hogy a `curl` megfelelően telepítve van-e, a verziószámának kinyomtatásával. Ha ez a parancs hibaüzenetet ad ki, akkor a PowerShell ezt a parancsot a `Invoke-WebRequest` parancsra cserélhette:

`curl --version`

- Az eredeti `curl` parancs dokumentációjának megtekintése:

`tldr curl -p common`

- Az eredeti `curl` parancs dokumentációjának megtekintése a `tldr` parancssori kliens régebbi verzióiban:

`tldr curl -o common`

- A PowerShell `Invoke-WebRequest` parancsának dokumentációjának megtekintése:

`tldr invoke-webrequest`
