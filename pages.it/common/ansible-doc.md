# ansible-doc

> Visualizza informazioni sui moduli installati nelle librerie Ansible.
> Visualizza un elenco conciso dei plugin e delle loro brevi descrizioni.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Elenca i plugin di azione disponibili (moduli):

`ansible-doc {{[-l|--list]}}`

- Elenca i plugin disponibili di un tipo specifico:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{[-l|--list]}}`

- Mostra informazioni su uno specifico plugin di azione (modulo):

`ansible-doc {{plugin_name}}`

- Mostra informazioni su un plugin con un tipo specifico:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{plugin_name}}`

- Mostra lo snippet del playbook per il plugin di azione (moduli):

`ansible-doc {{[-s|--snippet]}} {{plugin_name}}`

- Mostra informazioni su un plugin di azione (modulo) come JSON:

`ansible-doc {{[-j|--json]}} {{plugin_name}}`
