# cephadm

> Deploy and manage a Ceph cluster using containers.
> Part of the Ceph orchestrator framework.
> More information: <https://docs.ceph.com/en/latest/cephadm/>.

- Bootstrap a new Ceph cluster on the current host:
`cephadm bootstrap --mon-ip {{monitor_ip}}`

- Add a new host to the cluster:
`cephadm add-host {{hostname}} {{ip_address}}`

- Deploy a specific service (e.g., mgr, mon, osd):
`cephadm deploy {{service_type}} --name {{service_name}}`

- Check the status of cluster services:
`cephadm shell -- ceph -s`

- Enter a shell environment inside the Ceph container:
`cephadm shell`

- Remove a service from the cluster:
`cephadm rm-service {{service_type}} --name {{service_name}}`

