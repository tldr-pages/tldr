# ansible-pull

> Pull ansible playbooks from a VCS repo and executes them for the local host.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Pull playbook from a VCS and execute default local.yml playbook:

`ansible-pull -U {{repository_url}}`

- Pull playbook from a VCS and execute a specific playbook:

`ansible-pull -U {{repository_url}} {{playbook}}`

- Pull playbook from a VCS at specific branch and execute a specific playbook:

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- Pull playbook from a VCS, specify hosts file and execute a specific playbook:

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`
