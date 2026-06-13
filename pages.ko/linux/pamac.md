# pamac

> GUI 패키지 관리자 pamac의 명령줄 도구.
> AUR 패키지가 보이지 않으면 `/etc/pamac.conf` 또는 GUI에서 활성화하세요.
> 더 많은 정보: <https://wiki.manjaro.org/index.php/Pamac>.

- 새 패키지 설치:

`pamac install {{패키지_이름}}`

- 패키지 및 더 이상 필요하지 않은 의존성(고아) 제거:

`pamac remove --orphans {{패키지_이름}}`

- 패키지 데이터베이스에서 패키지 검색:

`pamac search {{패키지_이름}}`

- 설치된 패키지 나열:

`pamac list --installed`

- 패키지 업데이트 확인:

`pamac checkupdates`

- 모든 패키지 업그레이드:

`pamac upgrade`
