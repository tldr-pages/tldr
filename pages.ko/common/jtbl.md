# jtbl

> JSON 및 JSON Lines 데이터를 터미널에서 표 형태로 출력하는 유틸리티.
> 더 많은 정보: <https://github.com/kellyjonbrazil/jtbl>.

- JSON 또는 JSON Lines 입력으로부터 표 출력:

`cat {{파일.json}} | jtbl`

- 표를 출력하고 열 너비를 지정하여 줄 바꿈 설정:

`cat {{파일.json}} | jtbl --cols={{너비}}`

- 표를 출력하고 줄 바꿈 대신 행 잘라내기:

`cat {{파일.json}} | jtbl -t`

- 표를 출력하고 행을 줄 바꾸거나 잘라내지 않음:

`cat {{파일.json}} | jtbl -n`
