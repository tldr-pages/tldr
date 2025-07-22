# starship

> 최소한의 빠르고 무한히 커스터마이즈 가능한 쉘 프롬프트.
> `init`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://starship.rs>.

- 지정한 쉘에 대한 starship 통합 코드 출력:

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh|nu|xonsh|cmd}}`

- 현재 프롬프트의 각 부분을 설명하고 렌더링하는 데 걸린 시간 표시:

`starship explain`

- 계산된 starship 구성 출력 (기본 구성을 출력하려면 `--default` 사용):

`starship print-config`

- 지원하는 모듈 나열:

`starship module --list`

- 기본 편집기에서 starship 구성 편집:

`starship config`

- 시스템 및 starship 구성에 대한 정보를 미리 채운 GitHub 이슈로 버그 보고서 생성:

`starship bug-report`

- 지정한 쉘에 대한 자동 완성 스크립트 출력:

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- 하위 명령에 대한 도움말 표시:

`starship {{하위_명령}} --help`
