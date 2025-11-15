# virtualenv

> 가상 격리된 Python 환경 생성.
> 더 많은 정보: <https://virtualenv.pypa.io/en/latest/cli_interface.html>.

- 새 환경 생성:

`virtualenv {{경로/대상/venv}}`

- 프롬프트 접두사를 사용자 정의:

`virtualenv --prompt={{프롬프트_접두사}} {{경로/대상/venv}}`

- virtualenv에 다른 버전의 Python 사용:

`virtualenv --python={{경로/대상/pythonbin}} {{경로/대상/venv}}`

- 환경 시작(선택):

`source {{경로/대상/venv}}/bin/activate`

- 환경 중지:

`deactivate`
