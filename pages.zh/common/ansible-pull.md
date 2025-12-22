# ansible-pull

> 从 VCS 仓库拉取 Ansible playbook 并在本地主机上执行。
> 更多信息: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-pull.html>.

- 从 VCS 拉取一个 playbook 并执行默认的 `local.yml` playbook：

`ansible-pull {{[-U|--url]}} {{仓库 URL}}`

- 从 VCS 拉取一个 playbook 并执行指定的 playbook：

`ansible-pull {{[-U|--url]}} {{仓库 URL}} {{playbook}}`

- 从 VCS 的指定分支拉取一个 playbook 并执行指定的 playbook：

`ansible-pull {{[-U|--url]}} {{仓库 URL}} {{[-C|--checkout]}} {{分支}} {{playbook}}`

- 从 VCS 拉取一个 playbook，指定主机清单文件并执行指定的 playbook：

`ansible-pull {{[-U|--url]}} {{仓库 URL}} {{[-i|--inventory-file]}} {{主机文件}} {{playbook}}`
