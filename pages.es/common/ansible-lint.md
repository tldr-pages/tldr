# ansible-lint

> Aplica reglas y sigue las mejores prácticas en la automatización de tu contenido.
> Más información: <https://ansible.readthedocs.io/projects/lint/>.

- Analizar un playbook (archivo de tareas) específico y un directorio de roles con Lint:

`ansible-lint {{ruta/al/playbook}} {{ruta/al/directorio_de_roles}}`

- Analizar un playbook mientras se excluyen reglas específicas:

`ansible-lint {{[-x|--exclude-rules]}} {{regla1, regla2,...}} {ruta/al/archivo_playbook}`

- Analizar un playbook en modo sin conexión y darle como formato de salida PEP8:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{ruta/al/archivo_playbook}}`

- Analizar un playboo usando un directorio de reglas personalizadas:

`ansible-lint {{[-r|--rules]}} {{ruta/al/directorio_de_reglas_personalizadas}} {{ruta/al/archivo_playbook}}`

- Analizar todo el contenido Ansible de manerea recursiva en un directorio dado:

`ansible-lint {{ruta/al/directorio_del_proyecto}}`
