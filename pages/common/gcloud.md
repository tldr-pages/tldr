# gcloud

> The official CLI tool for Google Cloud Platform. 
> You can use this tool to perform common platform tasks.

- List all properties in your active configuration. Including: current authorized account, current project, and the default region and zone, if set:

`gcloud config list`

- Set the active project:

`gcloud config set project {{project_name}}`

- SSH into a virtual machine instance:

`gcloud compute ssh {{user}}@{{instance}} `

- Display all Google Compute Engine instances in a project. Instances from all zones are listed by default.

`gcloud compute instances list`

- Update a kubeconfig file with the appropriate credentials to point kubectl to a specific cluster in Google Kubernetes Engine:

`gcloud container clusters get-credentials {{cluster_name}}`

- Update all gcloud CLI components:

`gcloud components update`

- Show help:

`gcloud help {{command}}`
