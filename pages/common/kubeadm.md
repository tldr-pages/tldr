# kubeadm

> Command-line interface for creating and managing Kubernetes clusters.
> More information: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Create a Kubernetes master node:

`kubeadm init`

- Bootstrap a Kubernetes worker node and join it to a cluster:

`kubeadm join --token {{token}}`

- Create a new bootstrap token with a TTL of 12 hours:

`kubeadm token create --ttl {{12h0m0s}}`

- Check if the Kubernetes cluster is upgradeable and which versions are available:

`kubeadm upgrade plan`

- Upgrade Kubernetes cluster to a specified version:

`kubeadm upgrade apply {{version}}`

- View the kubeadm ConfigMap containing the cluster's configuration:

`kubeadm config view`

- Revert changes made to the host by 'kubeadm init' or 'kubeadm join':

`kubeadm reset`
