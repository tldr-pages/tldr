# ibmcloud api

> Set or view the IBM Cloud API endpoint.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_api>.

- View the current API endpoint:

`ibmcloud api`

- Set the API endpoint to `cloud.ibm.com`:

`ibmcloud api cloud.ibm.com`

- Set a private API endpoint:

`ibmcloud api private.cloud.ibm.com`

- Use a VPC connection for a private endpoint:

`ibmcloud api private.cloud.ibm.com --vpc`

- Bypass SSL validation of HTTP requests:

`ibmcloud api https://cloud.ibm.com --skip-ssl-validation`

- Remove the API endpoint setting:

`ibmcloud api --unset`
