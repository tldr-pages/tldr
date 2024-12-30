# ansible-pull

> 从版本控制系统（VCS）仓库中拉取 Ansible 剧本并在本地主机上执行它们。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>。

- 从 VCS 拉取一个剧本并执行默认的 local.yml 剧本：

`ansible-pull -U {{repository_url}}`

- 从 VCS 拉取一个剧本并执行特定的剧本：

`ansible-pull -U {{repository_url}} {{playbook}}`

- 从 VCS 在特定分支拉取一个剧本并执行特定的剧本：

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- 从 VCS 拉取一个剧本，指定主机文件并执行特定的剧本：

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`