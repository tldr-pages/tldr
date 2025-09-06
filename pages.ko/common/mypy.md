# mypy

> Python 코드의 타입을 검사.
> 더 많은 정보: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- 특정 파일의 타입 검사:

`mypy {{경로/대상/파일.py}}`

- 특정 [m]모듈의 타입 검사:

`mypy -m {{모듈_이름}}`

- 특정 [p]패키지의 타입 검사:

`mypy -p {{패키지_이름}}`

- 코드 문자열의 타입 검사:

`mypy -c "{{코드}}"`

- 누락된 import 무시:

`mypy --ignore-missing-imports {{경로/대상/파일_또는_폴더}}`

- 자세한 오류 메시지 표시:

`mypy --show-traceback {{경로/대상/파일_또는_폴더}}`

- 사용자 지정 구성 파일 지정:

`mypy --config-file {{경로/대상/구성_파일}}`

- [h]도움말 표시:

`mypy -h`
