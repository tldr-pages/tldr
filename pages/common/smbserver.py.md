# smbserver.py

> A Python-based SMB server for hosting shares (requires root for port 445).
> More information: <https://github.com/fortra/impacket>.

- Set up a basic SMB share:

`smbserver.py {{sharename}} {{path/to/share}}`

- Set up a share with a custom comment:

`smbserver.py -comment {{my_share}} {{sharename}} {{path/to/share}}`

- Set up a share with username and password authentication:

`smbserver.py -username {{username}} -password {{password}} {{sharename}} {{path/to/share}}`

- Set up a share with NTLM hash authentication:

`smbserver.py -hashes {{LMHASH}}:{{NTHASH}} {{sharename}} {{path/to/share}}`

- Set up a share on a specific interface:

`smbserver.py {{[-ip|--interface-address]}} {{interface_ip_address}} {{sharename}} {{path/to/share}}`

- Set up a share on a non-standard SMB port:

`smbserver.py -port {{port}} {{sharename}} {{path/to/share}}`

- Set up a share with SMB2 support:

`smbserver.py -smb2support {{sharename}} {{path/to/share}}`

- Set up a share and log commands to an output file:

`smbserver.py -outputfile {{path/to/output_file}} {{sharename}} {{path/to/share}}`
