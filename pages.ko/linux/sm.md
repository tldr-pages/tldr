# sm

> 전체 화면에 짧은 메시지를 표시합니다.
> 더 많은 정보: <https://github.com/nomeata/screen-message>.

- 메시지를 전체 화면에 표시:

`sm "{{Hello World!}}"`

- 색상을 반전하여 메시지를 표시:

`sm -i "{{Hello World!}}"`

- 사용자 지정 전경색으로 메시지를 표시:

`sm -f {{파란색}} "{{Hello World!}}"`

- 사용자 지정 배경색으로 메시지를 표시:

`sm -b {{#008888}} "{{Hello World!}}"`

- 메시지를 3회 회전하여 표시 (90도씩 반시계 방향):

`sm -r {{3}} "{{Hello World!}}"`

- 다른 명령의 출력을 사용하여 메시지를 표시:

`{{echo "Hello World!"}} | sm -`
