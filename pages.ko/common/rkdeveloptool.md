# rkdeveloptool

> Rockchip 기반 컴퓨터 장치의 부팅 펌웨어를 플래시, 덤프 및 관리.
> USB를 통해 연결하기 전에 장치를 Maskrom/Bootrom 모드로 전환해야 합니다.
> 일부 하위 명령은 루트 권한으로 실행해야 할 수 있습니다.
> 더 많은 정보: <https://github.com/rockchip-linux/rkdeveloptool>.

- 연결된 모든 Rockchip 기반 플래시 장치 [l]ist:

`rkdeveloptool ld`

- 지정된 파일에서 [b]ootloader를 다운로드 및 설치하도록 장치를 [d]ownload 모드로 초기화:

`rkdeveloptool db {{경로/대상/부트로더.bin}}`

- 부트[l]oader 소프트웨어를 새 버전으로 [u]pdate:

`rkdeveloptool ul {{경로/대상/부트로더.bin}}`

- GPT 형식의 플래시 파티션에 이미지를 작성하고 초기 저장소 섹터를 지정 (일반적으로 `0x0` 또는 `0`):

`rkdeveloptool wl {{초기_섹터}} {{경로/대상/이미지.img}}`

- 사용자 친화적인 이름으로 플래시 파티션에 쓰기:

`rkdeveloptool wlx {{파티션_이름}} {{경로/대상/이미지.img}}`

- [r]eset/재부팅 [d]evice, Maskrom/Bootrom 모드에서 나와 선택된 플래시 파티션으로 부팅:

`rkdeveloptool rd`
