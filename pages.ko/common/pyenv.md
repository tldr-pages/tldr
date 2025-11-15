# pyenv

> 여러 버전의 Python 사이를 쉽게 전환.
> 같이 보기: `asdf`.
> 더 많은 정보: <https://github.com/pyenv/pyenv>.

- 사용 가능한 모든 명령 나열:

`pyenv commands`

- `${PYENV_ROOT}/versions` 디렉토리 아래의 모든 Python 버전 나열:

`pyenv versions`

- 업스트림에서 설치할 수 있는 모든 Python 버전 나열:

`pyenv install --list`

- `${PYENV_ROOT}/versions` 디렉토리에 특정 Python 버전 설치:

`pyenv install {{2.7.10}}`

- `${PYENV_ROOT}/versions` 디렉토리에서 특정 Python 버전 제거:

`pyenv uninstall {{2.7.10}}`

- 현재 컴퓨터에서 전역으로 사용할 Python 버전 설정:

`pyenv global {{2.7.10}}`

- 현재 디렉토리와 하위 디렉토리에서 사용할 Python 버전 설정:

`pyenv local {{2.7.10}}`
