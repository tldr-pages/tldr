# dnf install

> Red Hat 계열 배포판에서 패키지 설치.
> 더 많은 정보: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- 이름으로 패키지 설치:

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- 로컬 파일로부터 패키지 설치:

`sudo dnf {{[in|install]}} {{path/to/file}}`

- 인터넷에서 패키지 설치:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- Fedora 자유 아닌 패키지 저장소 추가:

`sudo dnf {{[in|install]}} https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm`

- Extra Packages for Enterprise Linux (EPEL) 저장소 추가:

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Remi's RPM 저장소 추가:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`
