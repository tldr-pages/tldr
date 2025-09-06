# ansible-galaxy

> Erstelle und verwalte Ansible Rollen.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installiere eine Rolle:

`ansible-galaxy install {{benutzername}}.{{rollenname}}`

- Entferne eine Rolle:

`ansible-galaxy remove {{benutzername}}.{{rollenname}}`

- Liste installierte Rollen auf:

`ansible-galaxy list`

- Suche nach einer bestimmten Rolle:

`ansible-galaxy search {{rollenname}}`

- Erstelle eine neue Rolle:

`ansible-galaxy init {{rollenname}}`

- Erhalte Informationen über eine Benutzerrolle:

`ansible-galaxy role info {{benutzername}}.{{rollenname}}`

- Erhalte Informationen über eine Kollektion:

`ansible-galaxy collection info {{benutzername}}.{{kollektionsname}}`
