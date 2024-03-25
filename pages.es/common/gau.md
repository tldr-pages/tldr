# gau

> Obtén todas las URLs: obtén las URLs conocidas de Open Threat Exchange de AlienVault, Wayback Machine y Common Crawl para cualquier dominio.
> Más información: <https://github.com/lc/gau>.

- Obtén todas las URLs de un dominio de Open Threat Exchange de AlienVault, Wayback Machine, Common Crawl y URLScan:

`gau {{ejemplo.com}}`

- Obtén URLs de varios dominios:

`gau {{dominio1 dominio2 ...}}`

- Obtén todas las URLs de varios dominios en un archivo de entrada, ejecutando varios subprocesos:

`gau --threads {{4}} < {{ruta/a/dominios.txt}}}`

- Escribe los resultados en un archivo:

`gau {{ejemplo.com}} --o {{ruta/a/urls_encontradas.txt}}`

- Busca las URLs de un solo proveedor específico:

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{ejemplo.com}}`

- Busca las URLs de varios proveedores:

`gau --providers {{wayback,otx,...}} {{ejemplo.com}}`

- Busca las URLs dentro de un intervalo de fechas específico:

`gau --from {{AAAAMM}} --to {{YYYYMM}} {{ejemplo.com}}`
