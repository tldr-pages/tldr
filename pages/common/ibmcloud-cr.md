# ibmcloud cr

> Manage IBM Cloud Container Registry content and configuration.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-containerregcli>.

- Set target region for IBM Cloud Container Registry:

`ibmcloud cr region-set`

- List images available:

`ibmcloud cr {{[images|image-list]}}`

- Inspect an image data:

`ibmcloud cr image-inspect {{image}}`

- Run vulnerability assessment on an image:

`ibmcloud cr {{[va|vulnerability-assessment]}} {{image}}`

- Log the local Docker or Podman client in to IBM Cloud Container Registry:

`ibmcloud cr login`

- List all actions available under this command:

`ibmcloud cr help`
