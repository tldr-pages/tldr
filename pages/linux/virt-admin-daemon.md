# virt-admin daemon

> The following commands work with `virt-admin` to monitor the daemons state and change its internal configuaration.
> More information: <https://manned.org/virt-admin.1#head4>.

- List all managable servers contained within the daemon the client is currently connected to:

`virt-admin server-list`

- Return the currently defined set of logging filters:

`virt-admin daemon-log-filters`

- Define a new set of logging filters as strings deliminated by a space:

`virt-admin daemon-log-filters --filters "4:util.object`

- Return the currently defined set of logging outputs:

`virt-admin daemon-log-outputs`

- Define a new set of logging outputs as strings deliminated by a space:

`virt-admin daemon-log-outputs --outputs "4:file:<absolute_path_to_file>"`

- Set the daemon timeout:

`virt-admin daemon-timeout --timeout 10`

- Disable daemon timeout:

`virt-admin daemon-timeout --timeout 0`
