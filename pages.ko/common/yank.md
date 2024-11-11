# yank

> `stdin`에서 입력을 읽고 선택 인터페이스를 표시하여 필드를 선택하고 클립보드에 복사할 수 있게 합니다.
> 더 많은 정보: <https://manned.org/yank>.

- 기본 구분자 (\f, \n, \r, \s, \t)를 사용하여 Yank:

`{{sudo dmesg}} | yank`

- 전체 라인을 Yank:

`{{sudo dmesg}} | yank -l`

- 특정 구분자를 사용하여 Yank:

`{{echo hello=world}} | yank -d {{=}}`

- 특정 패턴과 일치하는 필드만 Yank:

`{{ps ux}} | yank -g "{{[0-9]+}}"`
