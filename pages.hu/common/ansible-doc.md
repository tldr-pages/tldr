# ansible-doc

> Az Ansible könyvtárakba telepített modulok információinak megjelenítése. A bővítmények tömör listájának és rövid leírásának megjelenítése. További információ: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Az elérhető műveleti bővítmények (modulok) listázása:

`ansible-doc --list`

- Egy adott típusú elérhető bővítmények listázása:

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} --list`

- Információk megjelenítése egy adott műveleti bővítményről (modulról):

`ansible-doc {{plugin_name}}`

- Információk megjelenítése egy adott típusú beépülő modulról:

`ansible-doc --type {{become|cache|callback|cliconf|connection|...}} {{plugin_name}}`

- A műveleti plugin (modulok) playbook snippetjének megjelenítése:

`ansible-doc --snippet {{plugin_name}}`

- Információk megjelenítése egy akciómodulról (modulról) JSON-ként:

`ansible-doc --json {{plugin_name}}`
