# kubectl autoscale

> Builds an autoscaler to intelligently scale pod count based on kubernetes cluster demands.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale>.

- Usage:

`kubectl autoscale (-f FILENAME | TYPE NAME | TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu-percent=CPU]`

- No target CPU utilization specified:

`kubectl autoscale deployment foo --min=2 --max=10`

- Auto scale a replication controller with target CPU utilization at 80%:

`kubectl autoscale rc foo --max=5 --cpu-percent=80`
