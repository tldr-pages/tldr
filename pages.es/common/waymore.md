# waymore

> Obtén las URLs de un dominio desde Wayback Machine, Common Crawl, Alien Vault OTX, URLScan y VirusTotal.
> Nota: A menos que se especifique lo contrario, los resultados se escriben en el directorio `results/` donde reside el archivo `config.yml` de waymore (por defecto en `~/.config/waymore/`).
> Más información: <https://github.com/xnl-h4ck3r/waymore>.

- Busca URLs de un dominio (la salida suele estar en `~/.config/waymore/results/`):

`waymore -i {{example.com}}`

- Limita los resultados de la búsqueda para que solo incluyan una lista de URLs de un dominio y almacena los resultados en el archivo especificado:

`waymore -mode U -oU {{ruta/a/example.com-urls.txt}} -i {{example.com}}`

- Imprime solo los cuerpos de contenido de las URLs y almacena los resultados en el directorio especificado:

`waymore -mode R -oR {{ruta/a/example.com-url-responses}} -i {{example.com}}`

- Filtra los resultados especificando intervalos de fechas:

`waymore -from {{YYYYMMDD|YYYMM|YYYY}} -to {{AAAAMMDD|AAAAMMD|AAAAMMD}} -i {{example.com}}`
