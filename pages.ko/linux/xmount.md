# xmount

> 여러 입력 및 출력 하드 디스크 이미지 형식을 선택적 쓰기 캐시 지원과 함께 실시간으로 변환합니다.
> FUSE(Filesystem in Userspace)를 사용하여 입력 이미지의 가상 표현을 포함하는 가상 파일 시스템을 만듭니다.
> 더 많은 정보: <https://manned.org/xmount>.

- `.raw` 이미지 파일을 DMG 컨테이너 파일로 마운트:

`xmount --in {{raw}} {{경로/대상/이미지.dd}} --out {{dmg}} {{마운트_포인트}}`

- 쓰기-캐시 지원과 함께 EWF 이미지 파일을 VHD 파일로 마운트하여 부팅:

`xmount --cache {{경로/대상/캐시.ovl}} --in {{ewf}} {{경로/대상/이미지.E??}} --out {{vhd}} {{마운트_포인트}}`

- 섹터 2048의 첫 번째 파티션을 새 `.raw` 이미지 파일로 마운트:

`xmount --offset {{2048}} --in {{raw}} {{경로/대상/이미지.dd}} --out {{raw}} {{마운트_포인트}}`
