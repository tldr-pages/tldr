# ansible-doc

> Display information on modules installed in Ansible libraries.
> It displays a terse listing of plugins and their short descriptions.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- List available action plugins (modules):

`ansible-doc -l`

- List available plugins from specific type:

`ansible-doc -t {{plugin_type}} -l`

- Show information of action plugin (module):

`ansible-pull {{plugin_name}}`

- Show information of a plugin from a specific type:

`ansible-doc -t {{plugin_type}} {{plugin_name}}`

- Show playbook snippet for action plugin (modules):

`ansible-pull -s {{plugin_name}}`

- Show information of action plugin (module) in JSON format:

`ansible-pull -j {{plugin_name}}`
