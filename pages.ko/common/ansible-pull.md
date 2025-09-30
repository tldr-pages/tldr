# ansible-pull

> VCS 저장소에서 Ansible 플레이북을 가져와 로컬 호스트에서 실행.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- VCS에서 플레이북을 가져와 기본 local.yml playbook을 실행:

`ansible-pull {{[-U|--url]}} {{저장소_url}}`

- VCS에서 플레이북을 가져와 특정 플레이북을 실행:

`ansible-pull {{[-U|--url]}} {{저장소_url}} {{playbook}}`

- 특정 지점의 VCS에서 플레이북을 가져와 특정 플레이북을 실행:

`ansible-pull {{[-U|--url]}} {{저장소_url}} {{[-C|--checkout]}} {{branch}} {{playbook}}`

- VCS에서 플레이북을 가져오고, 호스트 파일을 지정하고 특정 플레이북을 실행:

`ansible-pull {{[-U|--url]}} {{저장소_url}} {{[-i|--inventory]}} {{hosts_file}} {{playbook}}`
