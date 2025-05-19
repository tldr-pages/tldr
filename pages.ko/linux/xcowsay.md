# xcowsay

> Linux 데스크탑에 귀여운 소와 메시지를 표시합니다.
> 소는 고정된 시간 동안 표시되거나 텍스트 크기에 따라 계산된 시간 동안 표시됩니다. 소를 클릭하면 즉시 닫힙니다.
> 더 많은 정보: <https://manned.org/xcowsay>.

- "hello, world"라고 말하는 소를 표시:

`xcowsay "{{hello, world}}"`

- 다른 명령의 출력을 표시하는 소를 표시:

`ls | xcowsay`

- 지정된 X, Y 좌표에 소를 표시:

`xcowsay --at={{X}},{{Y}}`

- 다른 크기의 소를 표시:

`xcowsay --cow-size={{small|med|large}}`

- 말풍선 대신 생각풍선을 표시:

`xcowsay --think`

- 기본 소 대신 다른 이미지를 표시:

`xcowsay --image={{경로/대상/파일}}`
