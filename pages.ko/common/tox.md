# tox

> 여러 Python 버전에서 Python 테스트를 자동화.
> tox.ini를 사용하여 환경 및 테스트 명령을 구성하세요.
> 더 많은 정보: <https://github.com/tox-dev/tox>.

- 모든 테스트 환경에서 테스트 실행:

`tox`

- `tox.ini` 구성 생성:

`tox-quickstart`

- 사용 가능한 환경 나열:

`tox {{[-a|--listenvs-all]}}`

- 특정 환경에서 테스트 실행 (예: Python 3.6):

`tox -e {{py36}}`

- 가상 환경을 강제로 재생성:

`tox {{[-r|--recreate]}} -e {{py27}}`
