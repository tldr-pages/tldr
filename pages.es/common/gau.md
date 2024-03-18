# gau

> Obtiene todas las URLs: trae las URLs conocidas de Open Threat Exchange de AlienVault, de Wayback Machine y de Common Crawl para cualquier dominio.
> Más información: <https://github.com/lc/gau>.

- Obtiene todas las URL de un dominio de Open Threat Exchange de AlienVault, de Wayback Machine, de Common Crawl y de URLScan:

`gau {{ejemplo.com}}`

- Trae URLs de varios dominios:

`gau {{dominio1 dominio2 ...}}`

- Trae todas las URLs de varios dominios desde un archivo de entrada, ejecutando varios subprocesos:

`gau --threads {{4}} < {{ruta/a/dominios.txt}}}`

- Escribe los resultados de salida en un archivo:

`gau {{ejemplo.com}} --o {{ruta/a/urls_encontradas.txt}}`

- Busca las URLs de un solo proveedor específico:

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{ejemplo.com}}`

- Busca las URL de varios proveedores:

`gau --providers {{wayback,otx,...}} {{ejemplo.com}}`

- Busca las URLs dentro de un intervalo de fechas específico:

`gau --from {{AAAAMM}} --to {{YYYYMM}} {{ejemplo.com}}`
