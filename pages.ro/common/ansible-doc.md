# ansible-doc

> Afișați informații despre modulele instalate în bibliotecile Ansible.
> Afișează o listă detaliată a pluginurilor și descrierile lor scurte.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>

- Lista pluginurilor de acțiune disponibile (module):

`ansible-doc --list`

- Lista pluginurilor disponibile de un anumit tip:

`ansible-doc --type {{plugin_type}} --list`

- Afișați informații despre un anumit plugin de acțiune (modul):

`ansible-doc {{plugin_name}}`

- Afișați informații despre un plugin cu un anumit tip:

`ansible-doc --type {{plugin_type}} {{plugin_name}}`

- Arată fragmentul playbook pentru plugin-ul de acțiune (module):

`ansible-doc --snippet {{plugin_name}}`

- Afișează informații despre un plugin de acțiune (modul) ca JSON:

`ansible-doc --json {{plugin_name}}`
