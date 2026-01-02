# dnf5

> RHEL, Fedora, CentOS를 위한 패키지 관리 도구(dnf를 대체하며, dnf는 yum을 대체).
> DNF5는 C++로 다시 작성된 DNF 패키지 관리자로, 성능이 향상되고 크기가 작아졌습니다.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- 설치된 패키지를 최신 버전으로 업그레이드:

`sudo dnf5 upgrade`

- 키워드로 패키지 검색:

`dnf5 search {{키워드1 키워드2 ...}}`

- 패키지에 대한 세부 정보 표시:

`dnf5 info {{패키지}}`

- 새 패키지 설치 (`-y`를 사용하여 모든 메시지 자동 확인):

`sudo dnf5 install {{패키지1 패키지2 ...}}`

- 패키지 제거:

`sudo dnf5 remove {{패키지1 패키지2 ...}}`

- 설치된 패키지 나열:

`dnf5 list --installed`

- 특정 명령을 제공하는 패키지 찾기:

`dnf5 provides {{명령어}}`

- 캐시된 데이터 제거 또는 만료:

`sudo dnf5 clean all`
