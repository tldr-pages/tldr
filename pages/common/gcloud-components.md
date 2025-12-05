# gcloud components

> Manage Google Cloud CLI components.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/components>.

- View available components for installation:

`gcloud components list`

- Install one or more components (installs any dependencies as well):

`gcloud components install {{component_id1 component_id2 ...}}`

- Update all components to the latest version:

`gcloud components update`

- Update all components to a specific version:

`gcloud components update --version={{1.2.3}}`

- Update components without confirmation (useful for automation scripts):

`gcloud components update --quiet`
