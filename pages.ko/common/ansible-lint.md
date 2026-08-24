# ansible-lint

> 자동화 코드에 대해 규칙을 적용하고 모범 사례를 따르도록 검사하는 도구.
> 더 많은 정보: <https://docs.ansible.com/projects/lint/>.

- 특정 플레이북과 역할 디렉토리 lint 검사:

`ansible-lint {{경로/대상/플레이북_파일}} {{경로/대상/규칙_디렉토리}}`

- 특정 규칙을 제외하고 플레이북 lint 검사:

`ansible-lint {{[-x|--exclude-rules]}} {{rule1,rule2,...}} {{경로/대상/플레이북_파일}}`

- 오프라인 모드로 플레이북 lint 검사하고 결과를 PEP8 형식으로 출력:

`ansible-lint {{[-o|--offline]}} {{[-p|--parseable]}} {{경로/대상/플레이북_파일}}`

- 사용자 정의 규칙 디렉토리를 사용하여 플레이북 lint 검사:

`ansible-lint {{[-r|--rules]}} {{경로/대상/커스텀_규칙_디렉터리}} {{경로/대상/플레이북_파일}}`

- 지정한 디렉토리에서 모든 Ansible 콘텐츠를 재귀적으로 lint 검사:

`ansible-lint {{경로/대상/프로젝트_디렉토리}}`
