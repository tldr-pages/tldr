# repo-add

> Pacman을 통해 해당 패키지의 설치를 가능하게 하는 패키지 데이터베이스 유지 관리 유틸리티.
> 더 많은 정보: <https://manned.org/repo-add>.

- 빈 저장소 생성:

`repo-add {{경로/대상/데이터베이스.db.tar.gz}}`

- 현재 디렉토리의 모든 패키지 바이너리를 추가하고 기존 데이터베이스 파일 제거:

`repo-add {{[-R|--remove]}} {{경로/대상/데이터베이스.db.tar.gz}} {{*.pkg.tar.zst}}`

- 경고 및 오류 메시지를 제외하고 조용한 모드로 현재 디렉토리의 모든 패키지 바이너리 추가:

`repo-add {{[-q|--quiet]}} {{경로/대상/데이터베이스.db.tar.gz}} {{*.pkg.tar.zst}}`

- 색상을 표시하지 않고 현재 디렉토리의 모든 패키지 바이너리 추가:

`repo-add --nocolor {{경로/대상/데이터베이스.db.tar.gz}} {{*.pkg.tar.zst}}`
