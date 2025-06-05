# atool

> 다양한 형식의 압축 파일을 관리합니다.
> 더 많은 정보: <https://www.nongnu.org/atool/>.

- Zip 압축 파일의 파일 목록 표시:

`atool --list {{경로/대상/압축_파일.zip}}`

- tar.gz 압축 파일을 새로운 하위 디렉토리(또는 파일이 하나뿐인 경우 현재 디렉토리)에 풀기:

`atool --extract {{경로/대상/압축_파일.tar.gz}}`

- 두 개의 파일로 새로운 7z 압축 파일 생성:

`atool --add {{경로/대상/압축_파일.7z}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 현재 디렉토리의 모든 Zip 및 rar 압축 파일 추출:

`atool --each --extract {{*.zip *.rar}}`
