# pipx

> Python 애플리케이션을 격리된 환경에서 설치하고 실행.
> 더 많은 정보: <https://github.com/pypa/pipx>.

- 임시 가상 환경에서 앱 실행:

`pipx run {{pycowsay}} {{moo}}`

- 가상 환경에 패키지 설치 및 진입점을 경로에 추가:

`pipx install {{패키지}}`

- 설치된 패키지 나열:

`pipx list`

- 실행 파일과 다른 패키지 이름으로 임시 가상 환경에서 앱 실행:

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- 기존 가상 환경에 의존성 추가:

`pipx inject {{패키지}} {{의존성1 의존성2 ...}}`

- pip 인자를 사용하여 가상 환경에 패키지 설치:

`pipx install --pip-args='{{pip-인자}}' {{패키지}}`

- 모든 설치된 패키지 업그레이드/재설치/제거:

`pipx {{upgrade-all|uninstall-all|reinstall-all}}`
