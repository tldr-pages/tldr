# ansible-doc

> Display information on modules installed in Ansible libraries.
> Display a terse listing of plugins and their short descriptions.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- List available action plugins (modules):

`ansible-doc --list`

- List available plugins of a specific type:

`ansible-doc --type {{plugin_type}} --list`

- Show information about a specific action plugin (module):

`ansible-doc {{plugin_name}}`

- Show information about a plugin with a specific type:

`ansible-doc --type {{plugin_type}} {{plugin_name}}`

- Show the playbook snippet for action plugin (modules):

`ansible-doc --snippet {{plugin_name}}`

- Show information about an action plugin (module) as JSON:

`ansible-doc --json {{plugin_name}}`
