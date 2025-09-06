# mountpoint

> 디렉토리가 파일 시스템 마운트 지점인지 확인합니다.
> 더 많은 정보: <https://manned.org/mountpoint>.

- 디렉토리가 마운트 지점인지 확인:

`mountpoint {{경로/대상/폴더}}`

- 출력 없이 디렉토리가 마운트 지점인지 확인:

`mountpoint -q {{경로/대상/폴더}}`

- 마운트 지점의 파일 시스템 주요/부 번호 표시:

`mountpoint --fs-devno {{경로/대상/폴더}}`
