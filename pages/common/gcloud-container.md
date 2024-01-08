# gcloud container

> Manage containerized applications on Kubernetes and clusters.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/container>.

- Register `gcloud` as a Docker credential helper:

`gcloud auth configure-docker`

- Create a cluster to run GKE containers:

`gcloud container clusters create {{cluster_name}}`

- List clusters for running GKE containers:

`gcloud container clusters list`

- Update kubeconfig to get `kubectl` to use a GKE cluster:

`gcloud container clusters get-credentials {{cluster_name}}`

- List tag and digest metadata for a container image:

`gcloud container images list-tags {{image}}`
