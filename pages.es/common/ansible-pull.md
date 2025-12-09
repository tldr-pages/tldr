# ansible-pull

> Extrae playbooks ansible de un repositorio VCS y los ejecuta para el host local.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Extrae un playbook de un VCS y ejecuta local.yml del playbook por defecto:

`ansible-pull {{[-U|--url]}} {{url_repositorio}}`

- Extrae un playbook de un VCS y ejecuta un playbook específico:

`ansible-pull {{[-U|--url]}} {{url_repositorio}} {{playbook}}`

- Extrae un playbook de un VCS en una rama determinada y ejecuta un playbook específico:

`ansible-pull {{[-U|--url]}} {{url_repositorio}} {{[-C|--checkout]}} {{rama}} {{playbook}}`

- Extrae un playbook de un VCS, en tanto especificando un archivo hosts y ejecuta un playbook específico:

`ansible-pull {{[-U|--url]}} {{url_repositorio}} {{[-i|--inventory]}} {{archivo_hosts}} {{playbook}}`
