# debootstrap

> 기본 Debian 시스템 생성.
> 더 많은 정보: <https://wiki.debian.org/Debootstrap>.

- `debian-root` 디렉터리 내에 Debian 안정 버전 시스템 생성:

`sudo debootstrap stable {{경로/대상/debian-root/}} http://deb.debian.org/debian`

- 필수 패키지만 포함하는 최소 시스템 생성:

`sudo debootstrap --variant=minbase stable {{경로/대상/debian-root/}}`

- 로컬 미러를 사용하여 `focal-root` 디렉터리 내에 Ubuntu 20.04 시스템 생성:

`sudo debootstrap focal {{경로/대상/focal-root/}} {{file:///경로/대상/미러/}}`

- 부트스트랩된 시스템으로 전환:

`sudo chroot {{경로/대상/root}}`

- 사용 가능한 릴리스 나열:

`ls /usr/share/debootstrap/scripts/`
