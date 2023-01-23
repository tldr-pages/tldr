# black

> Python automatikus kódformázó. További információ: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Egy fájl vagy egy teljes könyvtár automatikus formázása:

`black {{path/to/file_or_directory}}`

- A karakterláncként átadott kód formázása:

`black -c "{{code}}"`

- Kimeneti, hogy egy fájl vagy egy könyvtár változtatásokat eszközölne-e rajtuk, ha formázni kellene őket:

`black --check {{path/to/file_or_directory}}`

- Kimenet, hogy egy fájlon vagy könyvtáron milyen változtatásokat hajtanának végre anélkül, hogy azokat végrehajtanák (száraz futtatás):

`black --diff {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár automatikus formázása, kizárólag hibaüzenetek kibocsátása a `stderr` címre:

`black --quiet {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár automatikus formázása anélkül, hogy az egyszerű idézőjeleket kettős idézőjelekkel helyettesítené (adoptálási segédprogram, kerülje a használatát új projekteknél):

`black --skip-string-normalization {{path/to/file_or_directory}}`
