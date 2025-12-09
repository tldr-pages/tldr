# hg serve

> 리포지토리를 탐색하기 위한 독립형 Mercurial 웹 서버 시작.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/serve>.

- 웹 서버 인스턴스 시작:

`hg serve`

- 지정된 포트에서 웹 서버 인스턴스 시작:

`hg serve --port {{포트}}`

- 지정된 수신 주소에서 웹 서버 인스턴스 시작:

`hg serve --address {{주소}}`

- 특정 식별자로 웹 서버 인스턴스 시작:

`hg serve --name {{이름}}`

- 지정된 테마를 사용하여 웹 서버 인스턴스 시작 (템플릿 디렉토리 참조):

`hg serve --style {{스타일}}`

- 지정된 SSL 인증서 번들을 사용하여 웹 서버 인스턴스 시작:

`hg serve --certificate {{경로/대상/인증서}}`
