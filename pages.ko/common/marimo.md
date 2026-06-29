# marimo

> 반응형 Python 노트북 환경.
> Jupyter, Streamlit 및 기타 노트북 도구의 기능을 반응형 실행(Reactive Execution)과 결합한 환경.
> 더 많은 정보: <https://docs.marimo.io/cli/>.

- Marimo 서버를 시작하여 노트북 생성 또는 편집:

`marimo edit`

- 브라우저를 자동 실행하지 않고 특정 포트에서 서버 시작:

`marimo edit {{[-p|--port]}} {{포트_번호}} --headless`

- 특정 노트북 편집:

`marimo edit {{경로/대상/노트북.py}}`

- marimo 노트북을 읽기 전용 앱으로 실행:

`marimo run {{경로/대상/노트북.py}}`

- marimo 학습을 위해 대화형 튜토리얼 실행:

`marimo tutorial {{intro|components|dataflow|io}}`

- 특정 명령의 도움말 보기:

`marimo {{edit|run|tutorial|config|new|...}} --help`
