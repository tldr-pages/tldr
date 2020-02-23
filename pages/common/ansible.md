# ansible install and configure

> Ansible installation can be found here.
> [docs.ansible]<https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>.

# ansible install

> The following commands are examples of required steps to ensure ansible is installed properly
> Ansible may require a separate user account with sudo privs on each node to run system commands

```sh
[user@server1] sudo yum install python python-pip python-devel openssl git ansible
[user@server1] sudo adduser ansible
[user@server1] sudo passwd ansible
```

# add user ansible to wheel

```sh
[user@server1] sudo visudo - %wheel nopasswd
[user@server1] su - ansible
[ansible@server1] ssh-keygen
[ansible@server1] ssh-copy-id localhost
```

## Add user ansible nodes

```sh
[ansible@server1] ssh-copy-id <nodes>
[ansible@server1] vim /etc/ansible/ansible.cfg
sudo_users root

[ansible@server1] vim /etc/ansible/hosts
localhost
```

## Ansible Options

```sh
-v    --verbose
-i    --inventory=Path              # hosts file
      --private-key=Priv_key_file
-m    --module-name
-M directory                        # loads module directory
-a arguments                        # to pass to module
-k    --ask-pass                    # ssh password
-K    --ask-sudo-pass
-o    --one-line
-s    --sudo
-u    --remote_user=
-U    --sudo-user
-c    --connection=                 # ssh or local
-l    --limit subset
-l~REGEX                            # limits hosts with regex pattern
```

## ansible group

> Manage groups of computers remotely over SSH.
> Use the /etc/ansible/hosts file to add new groups/hosts.
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

## ansible modules

```sh
[user@server1] ansible -m setup all                                 # 'inventory' of all systems
[user@server1] ansible -m ping all                                  # 'ping' inventory
[user@server1] ansible -m service -a 'name=httpd state=started'     # 'service'
```

## system facts

`ansible host -m setup -a 'filter=*ipv4'`

## Q: What does Fact mean in Ansible

> The term “Facts” is commonly used in Ansible environment. They are described in the playbooks areas where it displays known and discovered variables about the system.
> Facts are used to implement conditionals executions and also used for getting ad-hoc information of the information.
