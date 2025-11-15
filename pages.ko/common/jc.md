# jc

> 여러 명령어의 출력을 JSON으로 변환.
> 더 많은 정보: <https://github.com/kellyjonbrazil/jc>.

- 파이프를 통해 명령어 출력을 JSON으로 변환:

`{{ifconfig}} | jc {{--ifconfig}}`

- 매직 구문을 통해 명령어 출력을 JSON으로 변환:

`jc {{ifconfig}}`

- 파이프를 통해 예쁘게 출력된 JSON 출력:

`{{ifconfig}} | jc {{--ifconfig}} -p`

- 매직 구문을 통해 예쁘게 출력된 JSON 출력:

`jc -p {{ifconfig}}`
