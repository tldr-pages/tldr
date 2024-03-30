# gcloud config

> Manage different configurations of `gcloud`.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/config>.

- Define a property (like compute/zone) for the current configuration:

`gcloud config set {{property}} {{value}}`

- Fetch the value of a `gcloud` property:

`gcloud config get {{property}}`

- Display all the properties for the current configuration:

`gcloud config list`

- Create a new configuration with a given name:

`gcloud config configurations create {{configuration_name}}`

- Display a list of all available configurations:

`gcloud config configurations list`

- Switch to an existing configuration with a given name:

`gcloud config configurations activate {{configuration_name}}`
