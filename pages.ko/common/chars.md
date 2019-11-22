# chars

> 다양한 ASCII 및 유니코드 문자 및 코드 포인트에 대한 이름 및 코드 표시.
> 더 많은 정보: <https://github.com/antifuchs/chars>.

- 밸류 값으로 문자 검색:

`chars '{{ß}}'`

- 유니코드 코드로 문자 검색:

`chars {{U+1F63C}}`

- 모호한 코드 포인트가 주어지면 가능한 문자 검색:

`chars {{10}}`

- 제어 문자 찾기:

`chars "{{^C}}"`
