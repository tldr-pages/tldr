# 7zr

> 높은 파일압축률을 보여주는 압축 프로그램.
> .7z파일들만을 지원하는 `7z`의 독립형 버전.
> 더 많은 정보: <https://www.7-zip.org>.

- 파일이나 디렉토리 압축하기:

`7zr a {{경로/archived.7z}} {{경로/파일명_또는_디렉토리명}}`

- 압축파일 암호화 (including file names):

`7zr a {{경로/encrypted.7z}} -p{{비밀번호}} -mhe=on {{경로/archive.7z}}`

- 기존 디렉토리 경로에 존재하는 7z파일 추출하기:

`7zr x {{archived.7z}}`

- 특정 디렉토리에 압축파일 추출:

`7zr x {{경로/archive.7z}} -o{{아웃풋/의/경로}}`

- stdout에 압축파일 추출:

`7zr x {{경로/archive.7z}} -so`

- 압축 파일의 내용 리스트:

`7zr l {{경로/archived.7z}}`

- 사용가능한 압축 타입 리스트:

`7zr i`
