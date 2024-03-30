# sshare

> List the shares of associations to a cluster.
> More information: <https://slurm.schedmd.com/sshare.html>.

- List Slurm share information:

`sshare`

- Control the output format:

`sshare --{{parsable|parsable2|json|yaml}}`

- Control the fields to display:

`sshare --format={{format_string}}`

- Display information for the specified users only:

`sshare --users={{user_id_1,user_id_2,...}}`
