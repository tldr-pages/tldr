# ansible-playbook

> Executați activitățile definite în playbook pe mașinile la distanță prin SSH.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>

- Rulați sarcini în playbook:

`ansible-playbook {{playbook}}`

- Rulați sarcini în playbook cu inventar personalizat gazdă:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- Rulați sarcini în playbook cu variabile suplimentare definite prin linia de comandă:

`ansible-playbook {{playbook}} -e "{{variable1}}={{value1}} {{variable2}}={{value2}}"`

- Rulați sarcini în playbook cu variabile suplimentare definite într-un fișier json:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- Rulați sarcini în playbook pentru etichetele date:

`ansible-playbook {{playbook}} --tags {{tag1,tag2}}`

- Executați sarcini într-un manual de redare începând de la o anumită sarcină:

`ansible-playbook {{playbook}} --start-at {{task_name}}`
