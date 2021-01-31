# ansible

> Manage groups of computers remotely over SSH.
> Use the `/etc/ansible/hosts` file to add new groups/hosts.
> More information: <https://www.ansible.com/>.

- List hosts belonging to a group:

`ansible {{group}} --list-hosts`

- Ping a group of hosts by invoking the ping module:

`ansible {{group}} -m ping`

- Display facts about a group of hosts by invoking the setup module:

`ansible {{group}} -m setup`

- Execute a command on a group of hosts by invoking command module with arguments:

`ansible {{group}} -m command -a '{{my_command}}'`

- Execute a command with administrative privileges:

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- Execute a command using a custom inventory file:

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`
