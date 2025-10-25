# ibmcloud api

> IBM Cloud-API-Endpunkt festlegen oder anzeigen.
> Weitere Informationen: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_api>.

- Gib den aktuellen API-Endpunkt aus:

`ibmcloud api`

- Lege den aktuellen API-Endpunkt als cloud.ibm.com fest:

`ibmcloud api cloud.ibm.com`

- Setze den privaten Endpunkt:

`ibmcloud api private.cloud.ibm.com`

- Benutze eine VPC-Verbindung für einen privaten API-Endpunkt:

`ibmcloud api private.cloud.ibm.com --vpc`

- Umgehe SSL Validierung für HTTPS Anfragen:

`ibmcloud api https://cloud.ibm.com --skip-ssl-validation`

- Entferne den aktuellen API-Endpunkt:

`ibmcloud api --unset`
