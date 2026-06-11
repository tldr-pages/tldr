# mirrord

> Run code locally as if it were a pod in a Kubernetes cluster.
> Skip the build-push-deploy cycle when shipping features or fixing bugs against real services.
> More information: <https://metalbear.com/mirrord/docs/getting-started/quick-start#cli>.

- Run a local binary connected to a remote pod:

`mirrord exec {{[-t|--target]}} pod/{{pod_name}} -- {{command}} {{argument1 argument2 ...}}`

- Target a deployment in a specific namespace:

`mirrord exec {{[-t|--target]}} deployment/{{deployment_name}} {{[-n|--target-namespace]}} {{namespace}} -- {{command}}`

- Run with a configuration file:

`mirrord exec {{[-f|--config-file]}} {{path/to/mirrord.json}} -- {{command}}`

- Forward a local port to a host reachable from inside the cluster:

`mirrord port-forward {{[-t|--target]}} pod/{{pod_name}} --port-mapping {{local_port}}:{{remote_port}}`

- Print incoming TCP traffic from specific ports on a remote target:

`mirrord dump {{[-t|--target]}} pod/{{pod_name}} {{[-p|--ports]}} {{8080}}`

- Launch the interactive configuration wizard:

`mirrord wizard`

- Diagnose mirrord setup and cluster connectivity:

`mirrord diagnose`
