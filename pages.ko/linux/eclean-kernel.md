# eclean-kernel

> Gentoo에서 오래된 커널을 정리.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Kernel/Removal#Using_eclean-kernel>.

- 모든 커널 파일 목록 표시:

`sudo eclean-kernel {{[-l|--list-kernels]}}`

- 최신 두 개를 제외한 모든 커널 삭제:

`sudo eclean-kernel {{[-n|--num]}} 2`

- 최신 두 개를 제외한 모든 커널을 삭제하기 전에 확인 요청:

`sudo eclean-kernel {{[-a|--all]}} {{[-n|--num]}} 2`
