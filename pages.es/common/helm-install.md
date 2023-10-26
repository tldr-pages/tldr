# helm install

> Instalar un chart de helm.
> Mas información: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- Instalar un chart de helm:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}}`

- Instalar un chart de helm desde un directorio de chart desempaquetado:

`helm install {{nombre}} {{ruta/a/directorio_de_origen}}`

- Instalar un chart de helm desde una URL:

`helm install {{nombre_del_paquete}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- Instalar un chart de helm y generar un nombre:

`helm install {{nombre_del_repositorio}}/{{nombre_del_chart}} --generate-name`

- Realizar una simulación:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --dry-run`

- Instalar un chart de helm con valores personalizados:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --set {{parámetro1}}={{valor1}},{{parámetr2}}={{valor2}}`

- Instalar un chart de helm pasando un archivo de valores personalizados:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}} --values {{ruta/a/valores.yaml}}`
