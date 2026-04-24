# exo

> Exoscale 서비스를 관리하는 도구.
> `compute`와 같은 일부 하위 명령어는 별도의 사용법 문서를 가짐.
> 더 많은 정보: <https://community.exoscale.com/tools/command-line-interface/>.

- exo 커멘드라인 구성:

`exo config`

- 지정한 쉘에 대한 자동완성 스크립트 생성:

`exo completion {{zsh}}`

- 사용 가능한 모든 zone을 json 형식으로 출력:

`exo zone {{[-O|--output-format]}} {{json}}`

- 특정 zone에서 Compute 인스턴스를 조용히 생성(불필요한 명령어 출력을 비활성화):

`exo compute instance create {{인스턴스_이름}} --zone {{zone}} {{[-Q|--quiet]}}`

- 조직의 모든 버킷 이름만 출력:

`exo storage list {{[-O|--output-template]}} '\{\{ .Name \}\}`

- 특정 하위 명령어 도움말 표시:

`exo {{iam}} {{[-h|--help]}}`
