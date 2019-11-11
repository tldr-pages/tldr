# ansible-galaxy

> 수용 가능한 역할 생성 및 관리. 
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- 역할 설치:

`ansible-galaxy install {{username.role_name}}`

- 역할 제거:

`ansible-galaxy remove {{username.role_name}}`

- 설치된 역할 리스트:

`ansible-galaxy list`

- 주어진 역할에 대해 검색:

`ansible-galaxy search {{role_name}}`

- 새로운 역할 생성:

`ansible-galaxy init {{role_name}}`