# flake8

> Python 코드의 스타일과 품질을 확인.
> 더 많은 정보: <https://flake8.pycqa.org/en/latest/user/options.html>.

- 파일이나 디렉터리를 재귀적으로 린트:

`flake8 {{경로/대상/파일_또는_디렉터리}}`

- 파일이나 디렉터리를 재귀적으로 린트하고 각 오류가 발생한 줄을 표시:

`flake8 --show-source {{경로/대상/파일_또는_디렉터리}}`

- 파일이나 디렉터리를 재귀적으로 린트하고 규칙 목록을 무시. (사용 가능한 모든 규칙은 flake8rules.com에서 찾을 수 있음):

`flake8 --ignore {{rule1,rule2}} {{경로/대상/파일_또는_디렉터리}}`

- 파일이나 디렉터리를 재귀적으로 린트하지만, 지정된 glob 또는 하위 문자열과 일치하는 파일은 제외:

`flake8 --exclude {{substring1,glob2}} {{경로/대상/파일_또는_디렉터리}}`
