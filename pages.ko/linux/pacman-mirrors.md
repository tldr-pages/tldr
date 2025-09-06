# pacman-mirrors

> Manjaro Linux용 `pacman` 미러 리스트 생성.
> `pacman-mirrors`를 실행할 때마다 데이터베이스를 동기화하고 `sudo pacman -Syyu`를 사용하여 시스템을 업데이트해야 합니다.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- 기본 설정을 사용하여 미러 리스트 생성:

`sudo pacman-mirrors --fasttrack`

- 현재 미러 상태 확인:

`pacman-mirrors --status`

- 현재 브랜치 표시:

`pacman-mirrors --get-branch`

- 다른 브랜치로 전환:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- 거주 국가의 미러만 사용하여 미러 리스트 생성:

`sudo pacman-mirrors --geoip`
