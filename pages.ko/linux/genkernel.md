# genkernel

> Gentoo Linux에서 커널을 컴파일하고 설치하는 유틸리티.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Genkernel>.

- 일반 커널을 자동으로 컴파일하고 설치:

`sudo genkernel all`

- bzImage|initramfs|kernel|ramdisk만 빌드하고 설치:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- 컴파일 및 설치 전에 커널 설정을 변경:

`sudo genkernel --menuconfig all`

- 사용자 지정 이름의 커널 생성:

`sudo genkernel --kernname={{사용자_지정_이름}} all`

- 기본 디렉토리 `/usr/src/linux` 외부의 커널 소스를 사용:

`sudo genkernel --kerneldir={{경로/대상/폴더}} all`
