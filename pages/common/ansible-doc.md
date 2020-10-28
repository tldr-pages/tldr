# ansible-doc

> Display information on modules installed in Ansible libraries.
> Displays a terse listing of plugins and their short descriptions.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- List available action plugins (modules):

`ansible-doc --list`

- List available plugins of a specific type:

`ansible-doc --type {{plugin_type}} --list`

- Show information of action plugin (module):

`ansible-doc {{plugin_name}}`

- Show information of a plugin from a specific type:

`ansible-doc --type {{plugin_type}} {{plugin_name}}`

- Show playbook snippet for action plugin (modules):

`ansible-doc --snippet {{plugin_name}}`

- Show information of action plugin (module) in JSON format:

`ansible-doc --json {{plugin_name}}`
