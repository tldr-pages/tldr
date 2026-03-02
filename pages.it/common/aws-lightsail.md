# aws lightsail

> Gestisce le risorse Amazon Lightsail.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/lightsail/>.

- Elenca tutti i server virtuali privati, o istanze:

`aws lightsail get-instances`

- Elenca tutti i bundle (piani istanza):

`aws lightsail list-bundles`

- Elenca tutte le immagini istanza disponibili, o blueprint:

`aws lightsail list-blueprints`

- Crea un'istanza:

`aws lightsail create-instances --instance-names {{nome}} --availability-zone {{regione}} --bundle-id {{nano_2_0}} --blueprint-id {{id_blueprint}}`

- Stampa lo stato di un'istanza specifica:

`aws lightsail get-instance-state --instance-name {{nome}}`

- Ferma un'istanza specifica:

`aws lightsail stop-instance --instance-name {{nome}}`

- Elimina un'istanza specifica:

`aws lightsail delete-instance --instance-name {{nome}}`
