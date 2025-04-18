# ansible-lint

> Apply rules and follow best practices with your automation content.
> More information: <https://ansible.readthedocs.io/projects/lint/>.

- Lint a specific playbook and a role directory:

`ansible-lint {{path/to/playbook_file}} {{path/to/role_directory}}`

- Lint a playbook while excluding specific rules:

`ansible-lint {{--exclude-rules|-x}} {{rule1}},{{rule2}} {{path/to/playbook_file}}`

- Lint a playbook in offline mode and format output as PEP8 with:

`ansible-lint {{--offline|-o}} {{--parseable|-p}} {{path/to/playbook_file}}`

- Lint a playbook using a custom rule directory:

`ansible-lint {{--rules|-r}} {{path/to/custom_rules_directory}} {{path/to/playbook_file}}`

- Lint all Ansible content recursively in a given directory:

`ansible-lint {{path/to/project_directory}}`
