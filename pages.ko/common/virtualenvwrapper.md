# virtualenvwrapper

> Python의 `virtualenv` 도구를 위한 간단한 래퍼 명령 그룹.
> 더 많은 정보: <https://virtualenvwrapper.readthedocs.org>.

- 새로운 Python `virtualenv`를 `$WORKON_HOME`에 생성:

`mkvirtualenv {{가상환경_이름}}`

- 특정 Python 버전에 대한 `virtualenv` 생성:

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{가상환경_이름}}`

- 다른 `virtualenv` 활성화 또는 사용:

`workon {{가상환경_이름}}`

- `virtualenv` 중지:

`deactivate`

- 모든 가상 환경 나열:

`lsvirtualenv`

- `virtualenv` 제거:

`rmvirtualenv {{가상환경_이름}}`

- 모든 virtualenvwrapper 명령 요약 보기:

`virtualenvwrapper`
