# dmypy

> 더 빠른 실행을 위해 `mypy`를 데몬으로 실행하면서 Python 코드의 타입 검사를 수행.
> 관련 항목: `mypy`.
> 더 많은 정보: <https://mypy.readthedocs.io/en/stable/mypy_daemon.html>.

- 파일의 타입 검사를 수행, 데몬이 실행 중이 아니면 자동으로 시작:

`dmypy run -- {{경로/대상/파일.py}}`

- 데몬 시작:

`dmypy start`

- 파일의 타입 검사 수행 (데몬이 이미 실행 중이어야 함):

`dmypy check -- {{경로/대상/파일.py}}`

- 데몬 중지:

`dmypy stop`
