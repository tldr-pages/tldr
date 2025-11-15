# vipe

> UNIX 파이프라인 중간에서 텍스트 편집기를 실행합니다.
> 더 많은 정보: <https://manned.org/vipe>.

- `command1`의 출력을 편집한 후 `command2`로 파이핑:

`{{command1}} | vipe | {{command2}}`

- 구문 강조를 돕기 위해 지정된 파일 확장자로 임시 파일에 `command1`의 출력을 버퍼링:

`{{command1}} | vipe --suffix {{json}} | {{command2}}`

- 지정된 텍스트 편집기 사용:

`{{command1}} | EDITOR={{vim}} vipe | {{command2}}`
