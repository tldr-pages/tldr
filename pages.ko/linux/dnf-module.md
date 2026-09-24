# dnf module

> 패키지 모듈성 관리.
> 더 많은 정보: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- 모듈성 개요 표시:

`dnf module list`

- 특정 프로그램의 모듈 정보 표시:

`dnf module list {{패키지_이름}}`

- 특정 패키지 스트림 활성화:

`sudo dnf module enable {{패키지_이름}}:{{스트림}}`

- 특정 패키지 스트림 활성화:

`dnf module install {{패키지_이름}}:{{스트림}}`
