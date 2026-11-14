# rdma

> Manage RDMA (Remote Direct Memory Access) devices and links.
> More information: <https://manned.org/rdma>.

- List all RDMA devices:

`rdma dev show`

- List all RDMA links and their states:

`rdma link show`

- Display RDMA resource usage of all devices:

`rdma resource show`

- Display the RDMA subsystem settings:

`rdma system show`

- Create a software RDMA over Converged Ethernet (RoCE) link on a network interface:

`sudo rdma link add {{rxe0}} type rxe netdev {{eth0}}`

- Delete an RDMA link:

`sudo rdma link delete {{rxe0}}`
