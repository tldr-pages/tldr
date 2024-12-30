# pkgutil

> Mac OS X 설치 패키지 및 영수증을 조회하고 조작.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/pkgutil.1.html>.

- 모든 설치된 패키지의 패키지 ID 나열:

`pkgutil --pkgs`

- 패키지 파일의 암호화 서명 검증:

`pkgutil --check-signature {{경로/대상/파일명.pkg}}`

- 주어진 ID의 설치된 패키지의 모든 파일 나열:

`pkgutil --files {{com.microsoft.Word}}`

- 패키지 파일의 내용을 디렉토리에 추출:

`pkgutil --expand-full {{경로/대상/파일명.pkg}} {{경로/대상/폴더}}`
