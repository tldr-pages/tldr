# helm install

> Instalar un chart de helm.
> Más información: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- Instala un chart de helm:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}}`

- Instala un chart de helm desde un directorio de chart desempaquetado:

`helm install {{nombre}} {{ruta/al/directorio_de_origen}}`

- Instala un chart de helm desde una URL:

`helm install {{nombre_del_paquete}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- Instalar un chart de helm y genera un nombre:

`helm install {{nombre_del_repositorio}}/{{nombre_del_chart}} --generate-name`

- Realiza una simulación:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --dry-run`

- Instala un chart de helm con valores personalizados:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --set {{parámetro1}}={{valor1}},{{parámetro2}}={{valor2}}`

- Instala un chart de helm pasando un archivo de valores personalizados:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --values {{ruta/a/valores.yaml}}`
