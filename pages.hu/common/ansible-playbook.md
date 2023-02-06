# ansible-playbook

> A playbookban meghatározott feladatok végrehajtása távoli gépeken SSH-n keresztül. További információ: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- A playbookban szereplő feladatok futtatása:

`ansible-playbook {{playbook}}`

- Feladatok futtatása playbookban egyéni állomásleltárral:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- Feladatok futtatása playbookban a parancssoron keresztül definiált extra változókkal:

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- Feladatok futtatása playbookban JSON fájlban definiált extra változókkal:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- Feladatok futtatása playbookban a megadott címkékhez:

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- Feladatok futtatása a playbookban egy adott feladattól kezdve:

`ansible-playbook {{playbook}} --start-at {{task_name}}`
