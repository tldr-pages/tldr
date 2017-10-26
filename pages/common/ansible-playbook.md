# ansible-playbook

> Execute tasks defined in playbook on remote machines over SSH.

- Run tasks in playbook:

`ansible-playbook {{playbook}}`

- Run tasks in playbook with custom host inventory:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- Run tasks in playbook with extra variables defined via the command line:

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- Run tasks in playbook with extra variables defined on a json file:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`
