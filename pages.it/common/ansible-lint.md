# ansible-lint

> Applica regole e segui le best practice con i tuoi contenuti di automazione.
> Maggiori informazioni: <https://ansible.readthedocs.io/projects/lint/>.

- Lint un playbook specifico e una directory di ruoli:

`ansible-lint {{percorso/del/file_playbook}} {{percorso/della/role_directory}}`

- Lint un playbook escludendo regole specifiche:

`ansible-lint {{[-x|--exclude-rules]}} {{regola1,regola2,...}} {{percorso/del/file_playbook}}`

- Lint un playbook in modalità offline e formatta l'output come PEP8:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{percorso/del/file_playbook}}`

- Lint un playbook utilizzando una directory di regole personalizzate:

`ansible-lint {{[-r|--rules]}} {{percorso/della/custom_rules_directory}} {{percorso/del/file_playbook}}`

- Lint ricorsivamente tutto il contenuto Ansible in una directory specificata:

`ansible-lint {{percorso/della/project_directory}}`
