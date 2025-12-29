# apx stacks

> `apx`에서 스택을 관리합니다.
> 참고: 사용자가 생성한 스택 구성은 `~/.local/share/apx/stacks`에 저장됩니다.
> 더 많은 정보: <https://docs.vanillaos.org/docs/en/apx-manpage#stacks>.

- 대화형으로 새로운 스택 구성 생성:

`apx stacks new`

- 대화형으로 스택 구성 업데이트:

`apx stacks update {{이름}}`

- 사용 가능한 모든 스택 구성 나열:

`apx stacks list`

- 지정된 스택 구성 제거:

`apx stacks rm --name {{문자열}}`

- 스택 구성 가져오기:

`apx stacks import --input {{경로/대상/stack.yml}}`

- 스택 구성 내보내기 (참고: 출력 플래그는 선택 사항이며, 기본적으로 현재 작업 디렉터리에 내보내집니다):

`apx stacks export --name {{문자열}} --output {{경로/대상/출력_파일}}`
