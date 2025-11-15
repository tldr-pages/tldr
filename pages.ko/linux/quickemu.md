# quickemu

> 고도로 최적화된 데스크탑 가상 머신을 빠르게 구축하고 관리합니다.
> 같이 보기: VM 설정 준비를 위한 `quickget`.
> 더 많은 정보: <https://github.com/quickemu-project/quickemu>.

- 구성 파일에서 가상 머신 생성 및 실행:

`quickemu --vm {{경로/대상/파일.conf}}`

- 디스크/스냅샷에 변경 사항을 저장하지 않고 임시 파일에 변경 사항 기록:

`quickemu --status-quo --vm {{경로/대상/파일.conf}}`

- 전체 화면 모드로 가상 머신 시작 (`<Ctrl Alt f>`로 종료) 및 디스플레이 백엔드 선택 (기본값은 `sdl`):

`quickemu --fullscreen --display {{sdl|gtk|spice|spice-app|none}} --vm {{경로/대상/파일.conf}}`

- 가상 오디오 장치를 에뮬레이트하고 데스크탑 바로 가기 생성:

`quickemu --sound-card {{intel-hda|ac97|es1370|sb16|none}} --shortcut --vm {{경로/대상/파일.conf}}`

- 스냅샷 생성:

`quickemu --snapshot create {{태그}} --vm {{경로/대상/파일.conf}}`

- 스냅샷 복원:

`quickemu --snapshot apply {{태그}} --vm {{경로/대상/파일.conf}}`

- 스냅샷 삭제:

`quickemu --snapshot delete {{태그}} --vm {{경로/대상/파일.conf}}`
