# fastapi

> Uvicorn을 기반으로 동작하는 FastAPI 앱 실행용 CLI 도구.
> 추가 정보: <https://manned.org/fastapi>.

- 자동 재시작 기능을 사용하여 FastAPI 앱 실행 (개발용):

`fastapi run {{경로/파일.py}} --reload`

- 개발 모드에서 앱 실행:

`fastapi dev {{경로/파일.py}}`

- 호스트와 포트를 지정하여 실행:

`fastapi run {{경로/파일.py}} --host {{호스트_주소}} --port {{포트}}`

- 앱 변수 이름을 설정하거나 (기본값은 `app`), 앱 디렉터리를 지정:

`fastapi run {{경로/파일.py}} --app-dir {{경로/앱}} --app {{사용자_정의_앱명}}`

- 전체 도움말 보기:

`fastapi --help`

- 하위 명령어의 도움말 보기:

`fastapi {{하위명령어}} --help`
