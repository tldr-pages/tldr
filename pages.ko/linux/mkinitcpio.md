# mkinitcpio

> 지정된 프리셋을 기반으로 Linux 커널 부팅을 위한 초기 램디스크 환경을 생성합니다.
> 더 많은 정보: <https://manned.org/mkinitcpio.8>.

- 실행하지 않고 수행할 작업을 출력하는 드라이 런 수행:

`mkinitcpio`

- `linux` 프리셋을 기반으로 램디스크 환경 생성:

`mkinitcpio --preset {{linux}}`

- `linux-lts` 프리셋을 기반으로 램디스크 환경 생성:

`mkinitcpio --preset {{linux-lts}}`

- 모든 기존 프리셋을 기반으로 램디스크 환경 생성 (`/etc/mkinitcpio.conf`의 변경 후 모든 initramfs 이미지를 다시 생성하는 데 사용):

`mkinitcpio --allpresets`

- 대체 설정 파일을 사용하여 initramfs 이미지 생성:

`mkinitcpio --config {{경로/대상/mkinitcpio.conf}} --generate {{경로/대상/initramfs.img}}`

- 현재 실행 중인 커널이 아닌 다른 커널에 대한 initramfs 이미지 생성 (설치된 커널 릴리스는 `/usr/lib/modules/`에 있음):

`mkinitcpio --kernel {{커널_버전}} --generate {{경로/대상/initramfs.img}}`

- 사용 가능한 모든 훅 나열:

`mkinitcpio --listhooks`

- 특정 훅에 대한 도움말 표시:

`mkinitcpio --hookhelp {{훅_이름}}`
