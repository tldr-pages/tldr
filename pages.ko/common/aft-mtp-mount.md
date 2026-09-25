# aft-mtp-mount

> FUSE를 사용해 MTP(Media Transfer Protocol) 장치를 로컬 파일 시스템에 마운트.
> 관련 항목: `fusermount`.
> 더 많은 정보: <https://github.com/whoozle/android-file-transfer-linux>.

- MTP 장치를 지정한 디렉터리에 마운트:

`aft-mtp-mount {{경로/대상/마운트_포인트}}`

- 지정한 장치를 디렉터리에 마운트:

`aft-mtp-mount -D {{장치_이름}} {{경로/대상/마운트_포인트}}`

- 마운트하기 전에 장치 재설정:

`aft-mtp-mount -R {{경로/대상/마운트_포인트}}`

- USB 인터페이스를 점유하지 않고 장치 마운트:

`aft-mtp-mount -C {{경로/대상/마운트_포인트}}`

- 디버그 출력을 표시하며 장치 마운트:

`aft-mtp-mount -d {{경로/대상/마운트_포인트}}`

- 도움말 표시:

`aft-mtp-mount {{[-h|--help]}}`
