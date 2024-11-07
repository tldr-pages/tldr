# pipenv

> 간단하고 통합된 Python 개발 워크플로우.
> 프로젝트의 패키지 및 가상 환경 관리.
> 더 많은 정보: <https://pypi.org/project/pipenv>.

- 새 프로젝트 생성:

`pipenv`

- Python 3를 사용하여 새 프로젝트 생성:

`pipenv --three`

- 패키지 설치:

`pipenv install {{패키지}}`

- 프로젝트의 모든 의존성 설치:

`pipenv install`

- 프로젝트의 모든 의존성 설치 (개발 패키지 포함):

`pipenv install --dev`

- 패키지 제거:

`pipenv uninstall {{패키지}}`

- 생성된 가상 환경에서 쉘 시작:

`pipenv shell`

- 프로젝트의 `requirements.txt` (의존성 목록) 생성:

`pipenv lock --requirements`
