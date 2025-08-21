# kubectl autoscale

> Creates an autoscaler to intelligently scale pod count based on kubernetes cluster demands.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale>.

- Usage:

`kubectl autoscale (-f FILENAME | TYPE NAME | TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu-percent=CPU]`

- Auto scale a deployment with no target CPU utilization specified:

`kubectl autoscale deployment foo --min={{number}} --max={{number}}`

- Auto scale a replication controller with target CPU utilization:

`kubectl autoscale rc foo --max={{number}} --cpu-percent={{number}}`
