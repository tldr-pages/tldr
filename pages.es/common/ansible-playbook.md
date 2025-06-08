# ansible-playbook

> Ejecuta tareas definidas en un playbook (archivo de tareas) en máquinas remotas sobre SSH.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Corre tareas en el playbook dado:

`ansible-playbook {{playbook}}`

- Corre tareas en el playbook dado con inventario de host personalizado:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{inventory_file}}`

- Corre tareas en el playbook dado con variables extra definidas con la línea de comandos:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{variable1}}={{valor1}} {{variable2}}={{valor2}}"`

- Corre tareas en el playbook dado con variables extra definidas en un archivo JSON:

`ansible-playbook {{playbook}} {{[-e|extra-vars]}} "@{{variables.json}}"`

- Corre tareas en el playbook dado con tags específicos:

`ansible-playbook {{playbook}} {{[-t|--tags]}} {{tag1,tag2}}`

- Ejecuta tareas en el playbook dado empezando por una tarea determinada:

`ansible-playbook {{playbook}} --start-at {{nombre_tarea}}`

- Ejecuta tareas en el playbook dado sin realizar ningún cambio (dry-run):

`ansible-playbook {{playbook}} {{[-C|--check]}} {{[-D|--diff]}}`
