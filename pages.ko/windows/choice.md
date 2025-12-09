# choice

> 사용자에게 선택지를 제시하고 선택한 선택지의 색인을 반환합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- 현재 사용자에게 `Y` 또는 `N` 선택지를 제시:

`choice`

- 현재 사용자에게 특정 세트에서 [c]hoice 선택지를 제시:

`choice /c {{AB}}`

- 현재 사용자에게 특정 [m]essage와 함께 선택지를 제시:

`choice /m "{{메시지}}"`

- 현재 사용자에게 대소문자를 구분하는 [c]ase-[s]ensitive [c]hoice 선택지를 특정 세트에서 제시:

`choice /cs /c {{Ab}}`

- 현재 사용자에게 선택지를 제시하고, 특정 [t]ime 내에 [d]efault 선택지를 선호:

`choice /t {{5}} /d {{N}}`

- 도움말 표시:

`choice /?`
