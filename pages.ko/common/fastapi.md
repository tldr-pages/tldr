# fastapi

> Uvicorn을 내부적으로 사용하는 FastAPI 앱 실행용 CLI 도구.
> 더 많은 정보: <https://fastapi.tiangolo.com/tutorial/>.

- 자동 리로드를 사용하여 FastAPI 앱 실행 (개발용):

`fastapi run {{main.py}} --reload`

- `dev` 명령어를 사용하여 개발 또는 프로덕션 모드로 앱 실행:

`fastapi dev {{main.py}}`

- 실행할 호스트와 포트를 지정:

`fastapi run {{main.py}} --host {{0.0.0.0}} --port {{8000}}`

- 앱 변수 이름이 `app`이 아닌 경우 설정하거나, 앱 디렉터리를 지정:

`fastapi run {{main.py}} --app-dir {{path/to/app}} --app {{custom_app_name}}`

- 전역 도움말 표시:

`fastapi --help`

- 하위 명령어의 도움말 표시:

`fastapi run --help`
