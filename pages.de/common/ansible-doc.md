# ansible-doc

> Anzeigen von Informationen über die in den Ansible-Bibliotheken installierten Module.
> Anzeigen einer knappen Auflistung von Plugins und deren Kurzbeschreibungen.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Auflisten der verfügbaren Aktions-Plugin (Module):

`ansible-doc --list`

- Auflisten der verfügbare Plugins eines bestimmten Typs:

`ansible-doc --type {{plugin_typ}} --list`

- Anzeigen von Informationen über ein bestimmtes Aktions-Plugin (Module):

`ansible-doc {{plugin_name}}`

- Anzeigen von Informationen über ein Plugin mit einem betimmten Typ:

`ansible-doc --type {{plugin_typ}} {{plugin_name}}`

- Anzeigen des Playbookausschnittes für ein Actions-Plugin (Module):

`ansible-doc --snippet {{plugin_name}}`

- Anzeigen von Informationen über ein Aktions-Plugin (Module) als JSON:

`ansible-doc --json {{plugin_name}}`
