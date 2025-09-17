# hugo

> 템플릿 기반 정적 사이트 생성기. 모듈, 구성 요소 및 테마를 사용
> `server`와 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
> 더 많은 정보: <https://gohugo.io/commands/>.

- 새로운 Hugo 사이트 생성:

`hugo new site {{경로/대상/사이트}}`

- 새로운 Hugo 테마를 생성 (테마는 <https://themes.gohugo.io/>에서도 다운로드 할 수 있음):

`hugo new theme {{테마_이름}}`

- 새로운 페이지 생성:

`hugo new {{섹션_이름}}/{{페이지_이름}}`

- `./public/` 디렉토리에 사이트를 구축:

`hugo`

- "초안"으로 표시된 페이지를 포함하는 사이트 구축:

`hugo {{[-D|--buildDrafts]}}`

- 로컬 IP에 사이트 구축:

`hugo server --bind {{로컬_ip}} {{[-b|--baseURL]}} {{http://로컬_ip}}`

- 주어진 디렉토리에 사이트를 구축:

`hugo {{[-d|--destination]}} {{경로/대상/목적지}}`

- 사이트를 구축하고, 웹 서버를 시작하여 서비스를 제공하여, 페이지가 편집되면 자동으로 다시 로드됨:

`hugo server`
