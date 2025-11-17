# cephadm

> Deploy and manage a Ceph cluster using containers.
> Part of the Ceph orchestrator framework.
> More information: <https://docs.ceph.com/en/latest/man/8/cephadm/>.

- Bootstrap a new Ceph cluster on the current host:

`sudo cephadm bootstrap --mon-ip {{monitor_ip}}`

- Add a new host to the cluster:

`sudo cephadm add-host {{hostname}} {{ip_address}}`

- Deploy a specific service (e.g., mgr, mon, osd):

`sudo cephadm deploy {{service_type}} --name {{service_name}}`

- Check the status of cluster services:

`cephadm shell -- ceph {{[-s|--status]}}`

- Enter a shell environment inside the Ceph container:

`sudo cephadm shell`

- Remove a service from the cluster:

`cephadm rm-service {{service_type}} --name {{service_name}}`
