# 7za

> 높은 파일 압축률을 보여주는 파일 압축 프로그램.
> 더 적은 압축 타입을 지원하지만, 크로스플랫폼인 점을 제외하면 `7z`과 유사합니다.
> 더 많은 정보: <https://www.7-zip.org>.

- 파일이나 디렉토리 압축하기:

`7za a {{경로/archived.7z}} {{파일_혹은_디렉토리/의/경로}}`

- 압축파일 암호화 (including file names):

`7za a {{경로/encrypted.7z}} -p{{비밀번호}} -mhe=on {{경로/archive.7z}}`

- 기존 디렉토리 경로에 존재하는 7z 파일 추출:

`7za x {{archive.7z}}`

- 특정 디렉토리에 압축파일 추출:

`7za x {{경로/archive.7z}} -o{{아웃풋/의/경로}}`

- stdout에 압축파일 추출:

`7za x {{경로/archive.7z}} -so`

- 특정 압축 타입을 이용하여 추출하기:

`7za a -t{{zip|gzip|bzip2|tar}} {{archived}} {{path/to/file_or_directory}}`

- 압축 파일의 내용 리스트:

`7za l {{경로/archive.7z}}`

- 사용가능한 압축 타입 리스트:

`7za i`
