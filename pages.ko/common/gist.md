# gist

> <https://gist.github.com>에 코드 업로드.
> 더 많은 정보: <https://github.com/defunkt/gist>.

- 이 컴퓨터에서 gist에 로그인:

`gist --login`

- 원하는 수의 텍스트 파일에서 gist를 생성:

`gist {{파일.txt}} {{파일2.txt}}`

- 설명이 포함된 비공개 gist를 생성:

`gist --private --description "{{의미있는 설명}}" {{파일.txt}}`

- `stdin`의 내용을 읽고 그것으로부터 gist를 생성:

`{{echo "hello world"}} | gist`

- 공개 및 비공개 gist를 나열:

`gist --list`

- 모든 사용자에 대한 모든 공개 gist를 나열:

`gist --list {{사용자명}}`

- URL의 ID를 사용하여 gist를 업데이트:

`gist --update {{GIST_아이디}} {{파일.txt}}`
