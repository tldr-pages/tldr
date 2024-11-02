# pylint

> Python 코드 린터.
> 더 많은 정보: <https://pylint.pycqa.org/en/latest/>.

- 파일 내 린트 오류 표시:

`pylint {{경로/대상/파일.py}}`

- 패키지 또는 모듈 린트 (import 가능해야 하며, `.py` 접미사 없이):

`pylint {{패키지_또는_모듈}}`

- 디렉토리 경로에서 패키지 린트 (`__init__.py` 파일이 포함되어 있어야 함):

`pylint {{경로/대상/폴더}}`

- 파일을 린트하고 구성 파일 사용 (보통 `pylintrc`로 명명됨):

`pylint --rcfile {{경로/대상/pylintrc}} {{경로/대상/파일.py}}`

- 파일을 린트하고 특정 오류 코드를 비활성화:

`pylint --disable {{C,W,no-error,design}} {{경로/대상/파일}}`
