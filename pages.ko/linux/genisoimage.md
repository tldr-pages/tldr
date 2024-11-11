# genisoimage

> ISO9660/Joliet/HFS 하이브리드 파일 시스템을 생성하는 프리마스터링 프로그램.
> 더 많은 정보: <https://manned.org/genisoimage.1>.

- 주어진 소스 디렉토리에서 ISO 이미지 생성:

`genisoimage -o {{내_이미지.iso}} {{경로/대상/소스_폴더}}`

- ISO9660 파일 시스템에 대해 작은 겉보기 크기를 보고하여 2GiB보다 큰 파일을 포함한 ISO 이미지 생성:

`genisoimage -o -allow-limited-size {{내_이미지.iso}} {{경로/대상/소스_폴더}}`
