# gcloud CLI Personalization

> Make the gcloud CLI your own; personalize your configuration with properties.
> More information: <https://cloud.google.com/sdk/docs/cheatsheet#personalization>.

- Define a property (like compute/zone) for the current configuration:

`gcloud config set`

- Fetch the value of a gcloud CLI property:

`gcloud config get`

- Display all the properties for the current configuration:

`gcloud config list`

- Create a new named configuration:

`gcloud config configurations create`

- Display a list of all available configurations:

`gcloud config configurations list`

- Switch to an existing named configuration:

`gcloud config configurations activate`
