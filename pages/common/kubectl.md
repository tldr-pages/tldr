# kubectl

> Command line interface for running commands against Kubernetes clusters.

- List all pods in all namespaces:

`kubectl get pods --all-namespaces`

- List all pods with more information (such as node name):

`kubectl get pods -o wide`

- List all resources with different types:

`kubectl get all`

- Update specified pod with the label 'unhealthy' and the value 'true':

`kubectl label pods {name} unhealthy=true`

- Show metrics for all nodes:

`kubectl top node`

- Show metrics for all pods in the default namespace:

`kubectl top pod`

- Print the address of the master and cluster services:

`kubectl cluster-info`
