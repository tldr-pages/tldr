# ansible-doc

> Muestra información sobre los módulos instalados en las bibliotecas de Ansible.
> Muestra una concisa lista de complementos y sus breves descripciones.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Lista de complementos disponibles acorde a su acción (módulos):

`ansible-doc --list`

- Lista de complementos disponibles dado un tipo específico:

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} --list`

- Muestra información sobre un complemento acorde a su acción específica (módulo):

`ansible-doc {{nombre_complemento}}`

- Muestra información acerca de un complemento dado un tipo específico:

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} {{nombre_complemento}}`

- Muestra fragmentos de las acciones respecto al tipo de complemento y su especificidad de tipo de acción (módulos):

`ansible-doc --snippet {{nombre_complemento}}`

- Muestra información de acuerdo al complemento dada su especificidad de acción (módulo) como JSON:

`ansible-doc --json {{nombre_complemento}}`
