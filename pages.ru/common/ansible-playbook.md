# ansible-playbook

> Выполнять задачи, определённые в playbook, на удалённых машинах по SSH.
> Больше информации: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html>.

- Запустить задачи из playbook:

`ansible-playbook {{playbook}}`

- Запустить задачи из playbook с пользовательским инвентарём хостов:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{файл_инвентаря}}`

- Запустить задачи из playbook с дополнительными переменными, определёнными в командной строке:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{переменная1}}={{значение1}} {{переменная2}}={{значение2}}"`

- Запустить задачи из playbook с дополнительными переменными, определёнными в JSON-файле:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{переменные.json}}"`

- Запустить задачи из playbook для указанных тегов:

`ansible-playbook {{playbook}} {{[-t|--tags]}} {{тег1,тег2}}`

- Запустить задачи из playbook, начиная с определённой задачи:

`ansible-playbook {{playbook}} --start-at {{имя_задачи}}`

- Симулировать выполнение задач из playbook без внесения изменений:

`ansible-playbook {{playbook}} {{[-C|--check]}} {{[-D|--diff]}}`
