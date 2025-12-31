# dbx

> Interactúa con la plataforma Databricks.
> Nota: esta herramienta ha sido retirada y se recomienda utilizar Databricks Asset Bundles en su lugar.
> Más información: <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>.

- Crea un nuevo proyecto `dbx` en el directorio de trabajo actual:

`dbx configure --profile {{DEFAULT}}`

- Sincroniza archivos locales de la ruta especificada a DBFS y vigila los cambios:

`dbx sync dbfs --source {{ruta/a/directorio}} --dest {{ruta/a/directorio_remoto}}`

- Despliega el flujo de trabajo especificado en el almacenamiento de artefactos:

`dbx deploy {{nombre_del_flujo_de_trabajo}}`

- Inicia el flujo de trabajo especificado después de desplegarlo:

`dbx launch {{nombre_del_flujo_de_trabajo}}`
