# exo compute

> Manage Exoscale Compute resources.
> Some subcommands such as `instance` have their own documentation.
> More information: <https://community.exoscale.com/product/>.

- Quickly create an Exoscale Compute resource (e.g., instance, Security Group, SKS cluster,...):

`exo compute {{resource_type}} create {{resource_name}}`

- List Exoscale Compute instance types:

`exo compute instance-type list`

- Register a new SSH key that can be used to access Compute instances:

`exo compute ssh-key register {{key_name}} {{public_key_file}}`

- Create a Compute instance with an ssh-key deployed on it:

`exo compute instance create {{instance_name}} {{ssh_key_name}}`

- Register a new Compute instance template based on a Snapshot of a Compute instance (useful when you want to quickly create a replica of a Compute instance):

`exo compute instance template register {{template_name}} --from-snapshot {{snapshot_id}}`

- Add a new rule to an existing Security Group:

`exo compute security-group rule add {{security_group_name|id}} --description '{{Allow SSH access}}' --flow {{ingress}} --port {{22}} --network {{0.0.0.0/0}}`

- Manage the services of an existing Network Load Balancer:

`exo compute load-balancer service add {{load_balancer_name|id}} {{service_name}} --port {{service_port}}`
