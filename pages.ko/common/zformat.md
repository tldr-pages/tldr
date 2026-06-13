# zformat

> Zsh에서 문자열을 포맷하는 기능.
> 이 내장 명령은 `zsh/zutil` 모듈에 포함되어 있음.
> 관련 항목: `zstyle`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html>.

- zformat 모듈 로드:

`zmodload zsh/zutil`

- `%c`를 특정 값으로 치환하여 문자열 포맷 후 변수에 저장:

`zformat -f {{변수}} "{{Hello %c}}" {{c:world}}`

- 최소 너비 기준으로 오른쪽 패딩 (왼쪽 정렬):

`zformat -f {{변수}} "{{%10c}}" {{c:hello}}`

- 음수 너비를 사용한 왼쪽 패딩 (오른쪽 정렬):

`zformat -f {{변수}} "{{%-10c}}" {{c:hello}}`

- 삼항 표현식을 사용해 조건부 문자열을 생성 (지정된 값이 3일 경우, "yes"를, 그렇지 않을 경우 "no"를 반환):

`zformat -f {{변수}} "{{The answer is '%3(c.yes.no)'.}}" {{c:3}}`

- 음수 너비를 사용한 여러 필드 포맷팅 (오른쪽 정렬):

`zformat -f {{변수}} "name: %-15n value: %-10v" {{n:value1}} {{v:value2}}`

- 문자열 정렬 (콜론을 기준으로 좌:우 쌍을 구분):

`zformat -a {{array}} {{:}} {{left1:right1}} {{left2:right2}}`
