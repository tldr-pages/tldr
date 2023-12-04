# gcloud

> The official CLI tool for Google Cloud Platform.
> Some subcommands such as `gcloud iam` have their own usage documentation.
> More information: <https://cloud.google.com/sdk/gcloud>.

- List all properties in one's active configuration:

`gcloud config list`

- Login to Google account:

`gcloud auth login`

- Set the active project:

`gcloud config set project {{project_name}}`

- SSH into a virtual machine instance:

`gcloud compute ssh {{user}}@{{instance}}`

- Display all Google Compute Engine instances in a project (Instances from all zones are listed by default):

`gcloud compute instances list`

- Update a kubeconfig file with the appropriate credentials to point `kubectl` to a specific cluster in Google Kubernetes Engine (GKE):

`gcloud container clusters get-credentials {{cluster_name}}`

- Update all `gcloud` components:

`gcloud components update`

- Display help for a given command:

`gcloud help {{command}}`
