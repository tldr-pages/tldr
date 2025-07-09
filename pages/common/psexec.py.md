# psexec.py

> Execute commands on a remote Windows machine using `RemComSvc`, providing PsExec-like functionality.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Spawn an interactive shell on a remote target:

`psexec.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Execute a specific command on a remote target:

`psexec.py {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Copy the filename for later execution, arguments are passed in the command:

`psexec.py -c {{filename}} {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Execute a command from a specific path on a remote target:

`psexec.py -path {{path}} {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Authenticate using pass-the-hash authentication instead of a password:

`psexec.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Use Kerberos authentication for the target:

`psexec.py -k -no-pass {{domain}}/{{username}}@{{target}}`

- Specify the IP address of the domain controller:

`psexec.py -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`
