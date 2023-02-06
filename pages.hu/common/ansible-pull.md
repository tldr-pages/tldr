# ansible-pull

> Az ansible playbookok lehívása egy VCS repóból és végrehajtása a helyi állomáson. További információ: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Playbookot húz egy VCS-ből és végrehajt egy alapértelmezett local.yml playbookot:

`ansible-pull -U {{repository_url}}`

- Pull a playbook egy VCS-ből és egy adott playbook végrehajtása:

`ansible-pull -U {{repository_url}} {{playbook}}`

- Playbook húzása egy VCS-ből egy adott ágban, és egy adott playbook végrehajtása:

`ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}`

- Playbook húzása egy VCS-ből, hosts fájl megadása és egy adott playbook végrehajtása:

`ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}`
