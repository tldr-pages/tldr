# fluxctl

> Command-line tool for Flux v1.
> More information: <https://fluxcd.io/legacy/flux/references/fluxctl>.

- List workloads currently running in the cluster on specific namespace:

`fluxctl --k8s-fwd-ns={{namespace}} list-workloads`

- Show deployed and available images:

`fluxctl list-images`

- Synchronize the cluster with the Git repository:

`fluxctl sync`

- Turn on automatic deployment for a workload:

`fluxctl automate`
