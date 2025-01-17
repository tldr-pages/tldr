# bless

> 볼륨 부팅 기능 설정 및 시작 디스크 옵션 설정.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/bless.8.html>.

- Mac OS X 또는 Darwin 시스템이 있는 볼륨에 부팅 설정을 하고, 필요에 따라 BootX 및 `boot.efi` 파일 생성:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- Mac OS 9 및 Mac OS X를 포함한 볼륨을 활성 볼륨으로 설정:

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- 시스템을 NetBoot로 설정하고 사용 가능한 서버를 브로드캐스트:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- 현재 선택된 볼륨에 대한 정보를 수집하여 Property Lists를 구문 분석할 수 있는 프로그램에 전달하기 적합하게 출력:

`bless --info --plist`
