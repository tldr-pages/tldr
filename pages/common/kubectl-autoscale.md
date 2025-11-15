# kubectl autoscale

> Create an autoscaler to intelligently scale pod count based on kubernetes cluster demands.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale>.

- Auto scale a deployment with no target CPU utilization specified:

`kubectl autoscale {{[deploy|deployment]}} {{deployment_name}} --min {{min_replicas}} --max {{max_replicas}}`

- Auto scale a deployment with target CPU utilization:

`kubectl autoscale {{[deploy|deployment]}} {{deployment_name}} --max {{max_replicas}} --cpu-percent {{target_cpu}}`
