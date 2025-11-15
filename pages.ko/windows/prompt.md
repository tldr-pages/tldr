# prompt

> 명령 창의 기본 DOS 스타일 프롬프트를 변경합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- 기본 설정으로 프롬프트 재설정:

`prompt`

- 지정된 프롬프트로 설정:

`prompt {{프롬프트}}`

- 현재 날짜를 먼저 표시하도록 프롬프트를 변경:

`prompt $D $P$G`

- 현재 시간을 먼저 표시하도록 프롬프트를 변경:

`prompt $T $P$G`

- 특정 텍스트를 먼저 표시하도록 프롬프트를 변경:

`prompt {{텍스트}} $P$G`
