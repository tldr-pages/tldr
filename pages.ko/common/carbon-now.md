# carbon-now

> 아름다운 코드 이미지 생성.
> 더 많은 정보: <https://github.com/mixn/carbon-now-cli>.

- 기본 설정을 사용하여 파일에서 이미지를 만듬:

`carbon-now {{경로/대상/파일}}`

- 기본 설정을 사용해 클립보드의 텍스트에서 이미지를 생성:

`carbon-now --from-clipboard`

- 기본 설정을 사용해 `stdin`에서 이미지를 만들고 클립보드에서 복사:

`{{입력}} | carbon-now --to-clipboard`

- 사용자 정의 설정을 위해 대화형으로([i]nteractively) 이미지를 생성하고, 선택적으로 사전 설정을 저장:

`carbon-now -i {{경로/대상/파일}}`

- 이전에 저장된 프리셋([p]reset)에서 이미지 생성:

`carbon-now -p {{preset}} {{경로/대상/파일}}`

- 지정된 텍스트 줄에서 시작([s]tart):

`carbon-now -s {{line}} {{경로/대상/파일}}`

- 지정된 텍스트 줄에서 종료([e]nd):

`carbon-now -e {{line}} {{경로/대상/파일}}`

- 이미지를 저장하는 대신, 브라우저에서 열기:

`carbon-now --open {{경로/대상/파일}}`
