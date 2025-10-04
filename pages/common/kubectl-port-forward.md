# kubectl port-forward

> Forward one or more local ports to a pod.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/>.

- Forward local ports 5000 and 6000 to the pod ports 5000 and 6000:

`kubectl port-forward pod/{{pod_name}} 5000 6000`

- Forward a random local port to the pod port 5000:

`kubectl port-forward pod/{{pod_name}} :5000`

- Forward local ports 5000 and 6000 to the deployment ports 5000 and 6000:

`kubectl port-forward deployment/{{deployment_name}} 5000 6000`

- Forward local port 8443 to the service port named https:

`kubectl port-forward service/{{service_name}} 8443:https`

- Forward port 8888 on all addresses to the pod port 5000:

`kubectl port-forward --address 0.0.0.0 pod/{{pod_name}} 8888:5000`

- Forward port 8888 on localhost and selected IP to the pod port 5000:

`kubectl port-forward --address localhost,10.19.21.23 pod/{{pod_name}} 8888:5000`
