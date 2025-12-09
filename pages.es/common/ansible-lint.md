# ansible-lint

> Aplica reglas y sigue las mejores prácticas en la automatización de tu contenido.
> Más información: <https://ansible.readthedocs.io/projects/lint/>.

- Analiza un playbook (archivo de tareas) específico y un directorio de roles con Lint:

`ansible-lint {{ruta/al/playbook}} {{ruta/al/directorio_de_roles}}`

- Analiza un playbook mientras se excluyen reglas específicas:

`ansible-lint {{[-x|--exclude-rules]}} {{regla1, regla2,...}} {{ruta/al/archivo_playbook}}`

- Analiza un playbook en modo sin conexión y le da un formato de salida PEP8:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{ruta/al/archivo_playbook}}`

- Analiza un playbook usando un directorio de reglas personalizadas:

`ansible-lint {{[-r|--rules]}} {{ruta/al/directorio_de_reglas_personalizadas}} {{ruta/al/archivo_playbook}}`

- Analiza todo el contenido Ansible de manera recursiva en un directorio dado:

`ansible-lint {{ruta/al/directorio_del_proyecto}}`
