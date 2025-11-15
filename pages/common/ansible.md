# ansible

> Manage groups of computers remotely over SSH. (use the `/etc/ansible/hosts` file to add new groups/hosts).
> Some subcommands such as `galaxy` have their own usage documentation.
> More information: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- List hosts belonging to a group:

`ansible {{group}} --list-hosts`

- Ping a group of hosts by invoking the ping module:

`ansible {{group}} {{[-m|--module-name]}} ping`

- Display facts about a group of hosts by invoking the setup module:

`ansible {{group}} {{[-m|--module-name]}} setup`

- Execute a command on a group of hosts by invoking command module with arguments:

`ansible {{group}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- Execute a command with administrative privileges:

`ansible {{group}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- Execute a command using a custom inventory file:

`ansible {{group}} {{[-i|--inventory]}} {{inventory_file}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{my_command}}'`

- List the groups in an inventory:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
