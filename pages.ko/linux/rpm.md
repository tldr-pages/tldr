# rpm

> RPM 패키지 관리 도구.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://rpm-software-management.github.io/rpm/man/rpm.8>.

- httpd 패키지의 버전 표시:

`rpm --query {{httpd}}`

- 모든 일치하는 패키지의 버전 나열:

`rpm --query --all '{{mariadb*}}'`

- 현재 설치된 버전에 상관없이 강제로 패키지 설치:

`rpm --upgrade {{경로/대상/패키지.rpm}} --force`

- 파일의 소유자를 식별하고 패키지 버전 표시:

`rpm --query --file {{/etc/postfix/main.cf}}`

- 패키지가 소유한 파일 나열:

`rpm --query --list {{kernel}}`

- RPM 파일의 스크립트릿 표시:

`rpm --query --package --scripts {{패키지.rpm}}`

- 일치하는 패키지의 변경되었거나 누락되었거나 잘못 설치된 파일 표시:

`rpm --verify --all '{{php-*}}'`

- 특정 패키지의 변경 로그 표시:

`rpm --query --changelog {{패키지}}`
