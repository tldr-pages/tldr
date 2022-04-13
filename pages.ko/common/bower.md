# bower

> front-end 웹 개발에 최적화된 패키지 관리자. 패키지는 GitHub 사용자/reop 요약, Git의 엔드포인트, URL 혹은 등록된 패키지일 수 있습니다.
> 더 많은 정보: <https://bower.io/>.

- bower.json에 나열된 프로젝트의 종속성 설치:

`bower install`

- bower_components 디렉토리에 하나 이상의 패키지 설치:

`bower install {{패키지}} {{패키지}}`

- bower_components 디렉토리에서 로컬로 패키지 제거:

`bower uninstall {{패키지}} {{패키지}}`

- 로컬 패키지 및 가능한 업데이트 나열:

`bower list`

- bower 명령에 대한 도움말 표시:

`bower help {{명령}}`

- 패키지에 대한 bower.json 파일 생성:

`bower init`

- 특정 종속 버전을 설치하고, bower.json에 추가:

`bower install {{로컬명}}={{패키지}}#{{버젼}} --save`
