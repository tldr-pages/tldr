# ansible-pull

> Pull ansible playbooks from a VCS repo and executes them for the local host.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Pull a playbook from a VCS and execute a default local.yml playbook:

`ansible-pull -U {{repository_url}}`

- Pull a playbook from a VCS and execute a specific playbook:

`ansible-pull -U {{repository_url}} {{playbook}}`

- Pull a playbook from a VCS at a specific branch and execute a specific playbook:

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- Pull a playbook from a VCS, specify hosts file and execute a specific playbook:

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`
