# ansible-pull

> 从版本控制系统（VCS）拉取 Ansible 剧本并为本地主机执行。
> 更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- 从 VCS 拉取剧本并执行默认的 local.yml 剧本：

`ansible-pull -U {{repository_url}}`

- 从 VCS 拉取剧本并执行特定的剧本：

`ansible-pull -U {{repository_url}} {{playbook}}`

- 从 VCS 的特定分支拉取剧本并执行特定的剧本：

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- 从 VCS 拉取剧本，指定主机文件并执行特定的剧本：

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`
