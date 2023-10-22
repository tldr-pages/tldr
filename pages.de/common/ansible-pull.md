# ansible-pull

> Laden eines Ansible-Playbooks aus einem VCS-Repository und ausführen auf dem lokalen Host.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Laden eines Playbooks aus einem VCS und ausführen des standardmässigen local.yml Playbooks:

`ansible-pull -U {{repository_url}}`

- Laden eines Playbooks aus einem VCS und ausführen eines spezifischen Playbooks:

`ansible-pull -U {{repository_url}} {{playbook}}`

- Laden eines Playbooks aus einem VCS unter angabe eines bestimmten branches und ausführen eines spezifischen Playbooks:

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- Laden eines Playbooks aus einem VCS und ausführen eines spezifischen Playbooks unter angabe einer Hosts-Datei:

`ansible-pull -U {{repository_url}} -i {{hosts_datei}} {{playbook}}`
