# ibmcloud ks

> Manage Kubernetes and OpenShift clusters in IBM Cloud.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-kubernetes-service-cli>.

- View the details of a cluster:

`ibmcloud ks cluster get {{[-c|--cluster]}} {{cluster_id}}`

- View the rotation status of Cluster Authority certificates for a cluster:

`ibmcloud ks cluster ca status {{[-c|--cluster]}} {{cluster_id}}`

- View worker pools of a cluster:

`ibmcloud ks worker-pool ls {{[-c|--cluster]}} {{cluster_id}}`

- Delete a worker node and replace it with a new one in the same worker pool:

`ibmcloud ks worker replace {{[-c|--cluster]}} {{cluster_id}} {{[-w|--worker]}} {{worker_id}}`

- List all actions available under this command:

`ibmcloud ks help`
