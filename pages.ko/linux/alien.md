# alien

> 다양한 설치 패키지를 다른 형식으로 변환합니다.
> 같이 보기: `debtap`, Arch Linux에서 `.deb` 변환을 위한 도구.
> 더 많은 정보: <https://manned.org/alien>.

- 특정 설치 파일을 Debian 형식(`.deb` 확장자)으로 변환:

`sudo alien {{[-d|--to-deb]}} {{경로/대상/파일}}`

- 특정 설치 파일을 Red Hat 형식(`.rpm` 확장자)으로 변환:

`sudo alien {{[-r|--to-rpm]}} {{경로/대상/파일}}`

- 특정 설치 파일을 Slackware 설치 파일(`.tgz` 확장자)로 변환:

`sudo alien {{[-t|--to-tgz]}} {{경로/대상/파일}}`

- 특정 설치 파일을 Debian 형식으로 변환하고 시스템에 설치:

`sudo alien {{[-d|--to-deb]}} --install {{경로/대상/파일}}`
