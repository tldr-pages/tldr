# fish

> 사용자 친화적으로 설계된 명령줄 해석기인 Friendly Interactive SHell입니다.
> 더 많은 정보: <https://fishshell.com/docs/current/cmds/fish.html>.

- 대화형 쉘 세션을 시작:

`fish`

- 시작 구성을 로드하지 않고 대화형 쉘 세션을 시작:

`fish {{[-N|--no-config]}}`

- 특정 명령을 실행:

`fish {{[-c|--command]}} "{{echo 'fish is executed'}}"`

- 특정 스크립트를 실행:

`fish {{경로/대상/스크립트.fish}}`

- 구문 오류가 있는지 특정 스크립트를 확인:

`fish {{[-N|--no-execute]}} {{경로/대상/스크립트.fish}}`

- `stdin`에서 특정 명령을 실행:

`{{echo "echo 'fish is executed'"}} | fish`

- 쉘이 이전 기록에 액세스하거나 새 기록을 저장하지 않는 비공개 모드에서 대화형 쉘 세션을 시작:

`fish {{[-P|--private]}}`

- 쉘을 다시 시작해도 지속되는 환경 변수를 정의하고 내보냄 (기본 제공):

`set {{[-U|--universal]}} {{[-x|--export]}} {{변수_이름}} {{변수_값}}`
