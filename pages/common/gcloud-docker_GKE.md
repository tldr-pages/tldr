# gcloud CLI Docker and Google Kubernetes Engine

> The official CLI tool for Google Cloud Platform.
> More information: <https://cloud.google.com/sdk/docs/cheatsheet#docker>.

Docker & Google Kubernetes Engine (GKE)
Manage containerized applications on Kubernetes.

`gcloud auth configure-docker`: Register the gcloud CLI as a Docker credential helper (https://cloud.google.com/sdk/gcloud/reference/auth/configure-docker)

`gcloud container clusters create`: Create a cluster to run GKE containers (https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)

`gcloud container clusters list`: List clusters for running GKE containers (https://cloud.google.com/sdk/gcloud/reference/container/clusters/list)

`gcloud container clusters get-credentials`: Update kubeconfig to get kubectl to use a GKE cluster (https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)

`gcloud container images list-tags`: List tag and digest metadata for a container image (https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags)
