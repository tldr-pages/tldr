# pkgmk

> CRUX에서 pkgadd로 사용할 바이너리 패키지를 만듭니다.
> 더 많은 정보: <https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>.

- 패키지 만들기 및 다운로드:

`pkgmk -d`

- 패키지 생성 후 설치:

`pkgmk -d -i`

- 패키지 생성 후 업그레이드:

`pkgmk -d -u`

- 패키지 생성 시 발자국 무시:

`pkgmk -d -if`

- 패키지 생성 시 MD5 합계 무시:

`pkgmk -d -im`

- 패키지의 발자국 업데이트:

`pkgmk -uf`
