# jmtpfs

> MTP 장치에 액세스하기 위한 FUSE 기반 파일 시스템.
> 더 많은 정보: <https://manned.org/jmtpfs>.

- MTP 장치를 디렉토리에 마운트:

`jmtpfs {{경로/대상/폴더}}`

- 마운트 옵션 설정:

`jmtpfs -o {{allow_other,auto_unmount}} {{경로/대상/폴더}}`

- 사용 가능한 MTP 장치 나열:

`jmtpfs --listDevices`

- 여러 장치가 있는 경우 특정 장치 마운트:

`jmtpfs -device={{버스_ID}},{{장치_ID}} {{경로/대상/폴더}}`

- MTP 장치 마운트 해제:

`fusermount -u {{경로/대상/폴더}}`
