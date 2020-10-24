# ansible-pull

> pulls ansible playbooks from a VCS repo and executes them for the local host
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- pulls playbook from a VCS and execute default local.yml playbook:

`ansible-pull -U {{repository}}`

- pulls playbook from a VCS and execute a specific playbook:

`ansible-pull -U {{repository}} {{playbook}}`

- pulls playbook from a VCS at specific branch and execute a specific playbook:

`ansible-pull -U {{repository}} -C {{branch}} {{playbook}}`

- pulls playbook from a VCS, specify hosts file and execute a specific playbook:

`ansible-pull -U {{repository}} -i {{hosts_file}} {{playbook}}`
