# molecule

> Molecule은 Ansible 역할 테스트를 돕습니다.
> 더 많은 정보: <https://docs.ansible.com/projects/molecule/usage/>.

- 새 Ansible 역할 생성:

`molecule init role --role-name {{역할_이름}}`

- 테스트 실행:

`molecule test`

- 인스턴스 시작:

`molecule create`

- 인스턴스 구성:

`molecule converge`

- 인스턴스의 시나리오 나열:

`molecule matrix converge`

- 인스턴스에 로그인:

`molecule login`
