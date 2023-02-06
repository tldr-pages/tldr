# k8sec

> A Kubernetes titkokat kezelő parancssori eszköz. További információ: <https://github.com/dtan4/k8sec>.

- Az összes titok listázása:

`k8sec list`

- Egy adott titok listázása base64-kódolt karakterláncként:

`k8sec list {{secret_name}} --base64`

- Egy titok értékének beállítása:

`k8sec set {{secret_name}} {{key=value}}`

- Egy base64-kódolt érték beállítása:

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- Egy titok beállításának feloldása:

`k8sec unset {{secret_name}}`

- Titkok betöltése fájlból:

`k8sec load -f {{path/to/file}} {{secret_name}}`

- Titkok fájlba való kiürítése:

`k8sec dump -f {{path/to/file}} {{secret_name}}`
