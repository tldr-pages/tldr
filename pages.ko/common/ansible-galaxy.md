# ansible-galaxy

> Ansible 역할 생성 및 관리.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- 역할 설치:

`ansible-galaxy install {{사용자명}}.{{역할_이름}}`

- 역할 제거:

`ansible-galaxy remove {{사용자명}}.{{역할_이름}}`

- 설치된 역할 리스트:

`ansible-galaxy list`

- 주어진 역할에 대해 검색:

`ansible-galaxy search {{역할_이름}}`

- 새로운 역할 생성:

`ansible-galaxy init {{역할_이름}}`

- 사용자 역할에 해당하는 정보 가져오기:

`ansible-galaxy role info {{사용자명}}.{{역할_이름}}`

- 컬렉션에 대한 정보 가져오기:

`ansible-galaxy collection info {{사용자명}}.{{컬렉션_이름}}`
