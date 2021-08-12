# ansible-pull

> Trageți playbooks ansible dintr-un repo VCS și le execută pentru gazda locală.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>

- Trageți un playbook dintr-un VCS și executați un manual de redare implicit local.yml:

`ansible-pull -U {{repository_url}}`

- Trageți un playbook de la un VCS și executați un anumit playbook:

`ansible-pull -U {{repository_url}} {{playbook}}`

- Trageți un playbook de la un VCS la o anumită ramură și executați un anumit playbook:

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- Trageți un playbook dintr-un VCS, specificați fișierul hosts și executați un anumit playbook:

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`
