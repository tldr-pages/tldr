# addcomputer.py

> Add a computer account to domain.
> More information: <https://github.com/fortra/impacket>.

- Add a computer with a specific name and password:

`addcomputer.py -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Only set a new password on an existing computer:

`addcomputer.py -no-add -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Delete an existing computer account:

`addcomputer.py -delete -computer-name {{COMPUTER_NAME$}} {{domain}}/{{username}}:{{password}}`

- Add computer using Kerberos authentication:

`addcomputer.py -k -no-pass {{domain}}/{{username}}@{{hostname}}`

- Add computer via LDAPS (port 636) instead of SAMR (port 445):

`addcomputer.py -method LDAPS -port 636 {{domain}}/{{username}}:{{password}}`

- Specify exact domain controller when multiple DCs exist:

`addcomputer.py -dc-host {{hostname}} {{domain}}/{{username}}:{{password}}`
