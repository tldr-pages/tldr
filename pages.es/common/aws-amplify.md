# aws amplify

> Plataforma de desarrollo para crear aplicaciones móviles y web seguras y escalables.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

- Crea una nueva aplicación Amplify:

`aws amplify create-app --name {{nombre_de_la_app}} --description {{descripción}} --repository {{url_repositorio}} --platform {{plataforma}} --environment-variables {{variables_de_entorno}} --tags {{etiquetas}}`

- Elimina una aplicación Amplify existente:

`aws amplify delete-app --app-id {{id_aplicación}}`

- Obtiene detalles de una aplicación Amplify determinada:

`aws amplify get-app --app-id {{id_aplicación}}`

- Lista todas las aplicaciones de Amplify:

`aws amplify list-apps`

- Actualiza la configuración de una aplicación Amplify:

`aws amplify update-app --app-id {{id_aplicación}} --name {{nuevo_nombre}} --description {{nueva_descripción}} --repository {{nuevo_url_repositorio}} --environment-variables {{variables_nuevo_entorno}} --tags {{nuevas_etiquetas}}`

- Añade un nuevo entorno backend a una aplicación Amplify:

`aws amplify create-backend-environment --app-id {{id_aplicación}} --environment-name {{nombre_del_entorno}} --deployment-artifacts {{artefactos}}`

- Elimina un entorno backend de una aplicación Amplify:

`aws amplify delete-backend-environment --app-id {{id_aplicación}} --environment-name {{nombre_del_entorno}}`

- Lista todos los entornos backend de una aplicación Amplify:

`aws amplify list-backend-environments --app-id {{id_aplicación}}`
