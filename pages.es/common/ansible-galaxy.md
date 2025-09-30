# ansible-galaxy

> Realiza varias operaciones de Ansible Role y algunas relacionadas a Collection.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Enumera roles instalados o colecciones:

`ansible-galaxy {{role|collection}} list`

- Busca un rol con varios niveles de verbosidad (`-v` debe ser específicado al final):

`ansible-galaxy role search {{keyword}} -v{{vvvvv}}`

- Instala o elimina roles:

`ansible-galaxy role {{install|remove}} {{rol_nombre1 rol_nombre2 ...}}`

- Crea un nuevo rol:

`ansible-galaxy role init {{rol_nombre}}`

- Obtiene información acerca de un rol:

`ansible-galaxy role info {{rol_nombre}}`

- Instala o elimina colecciones:

`ansible-galaxy collection {{install|remove}} {{colección_nombre1 colección_nombre2 ...}}`

- Despliega más información (ayuda) acerca de roles o colecciones:

`ansible-galaxy {{role|collection}} {{[-h|--help]}}`
