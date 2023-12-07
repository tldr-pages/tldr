# gcloud components install

> Install specific components of the Google Cloud CLI, along with their dependencies.
> Installs components at the current version of the Google Cloud CLI without upgrading the existing installation.
> More information: <https://cloud.google.com/sdk/gcloud/reference/components/install>.

- View available components for installation:

`gcloud components list`

- Install a specific component (installs any dependencies as well):

`gcloud components install {{component_id}}`

- Install multiple specific components:

`gcloud components install {{component_id1}} {{component_id2}}`

- Check the current version of Google Cloud CLI:

`gcloud version`

- Update Google Cloud CLI to the latest version:

`gcloud components update`
