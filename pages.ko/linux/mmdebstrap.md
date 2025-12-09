# mmdebstrap

> Debian chroot 생성 도구.
> `debootstrap`의 대안.
> 더 많은 정보: <https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- Debian Stable 디렉토리 chroot 생성:

`sudo mmdebstrap stable {{경로/대상/debian-root/}}`

- 미러를 사용하여 Debian Bookworm tarball chroot 생성:

`mmdebstrap bookworm {{경로/대상/debian-bookworm.tar}} {{http://mirror.example.org/debian}}`

- 추가 패키지를 포함하여 Debian Sid tarball chroot 생성:

`mmdebstrap sid {{경로/대상/debian-sid.tar}} --include={{pkg1,pkg2}}`
