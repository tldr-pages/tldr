# kube-capacity

> A simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster.
> It attempts to combine the best parts of the output from kubectl top and kubectl describe into an easy to use CLI focused on cluster resources.

- Output a list of nodes with the total CPU and Memory resource reqeusts and limits:

`kube-capacity`

- Include pods:

`kube-capacity -p`

- Include utilization:

`kube-capacity -u`
