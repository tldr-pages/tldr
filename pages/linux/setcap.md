# setcap

> Set capabilities of specified file.
> See also: `getcap`.
> More information: <https://manned.org/setcap>.

- Set capability `cap_net_raw` (to use RAW and PACKET sockets) for a given file:

`setcap '{{cap_net_raw}}' {{path/to/file}}`

- Set multiple capabilities on a file (`ep` behind the capability means "effective permitted"):

`setcap '{{cap_dac_read_search,cap_sys_tty_config+ep}}' {{path/to/file}}`

- Remove all capabilities from a file:

`setcap -r {{path/to/file}}`

- Verify that the specified capabilities are currently associated with the specified file:

`setcap -v '{{cap_net_raw}}' {{path/to/file}}`

- The optional `-n root_uid` argument can be used to set the file capability for use only in a user namespace with this root user ID owner:

`setcap -n {{root_uid}} '{{cap_net_admin}}' {{path/to/file}}`
