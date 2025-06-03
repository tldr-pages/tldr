# ansible-doc

> Ansible 라이브러리에 설치된 모듈에 대한 정보를 표시.
> 플러그인과 간단한 설명의 정리된 목록을 표시.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- 사용 가능한 작업 플러그인(모듈) 목록:

`ansible-doc {{[-l|--list]}}`

- 특정 유형의 사용 가능한 플러그인을 나열:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{[-l|--list]}}`

- 특정 작업 플러그인(모듈)에 대한 정보 표시:

`ansible-doc {{plugin_name}}`

- 특정 유형의 플러그인에 대한 정보 표시:

`ansible-doc {{[-t|--type]}} {{become|cache|callback|cliconf|connection|...}} {{플러그인_이름}}`

- 액션 플러그인(모듈)에 대한 플레이북 스니펫 표시:

`ansible-doc {{[-s|--snippet]}} {{플러그인_이름}}`

- 액션 플러그인(모듈)에 대한 정보를 JSON으로 표시:

`ansible-doc {{[-j|--json]}} {{플러그인_이름}}`
