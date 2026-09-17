# chroot

> 특수 루트 디렉토리를 사용하여 명령 또는 대화형 쉘 실행.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- 새 루트 디렉토리에서 `$SHELL`을 실행:

`sudo chroot {{경로/대상/새로운_루트}}`

- 새 루트 디렉터리에서 지정한 명령어를 실행:

`sudo chroot {{경로/대상/새로운_루트}} {{명령어}}`

- 특정 사용자와 그룹을 사용:

`sudo chroot --userspec {{사용자이름_또는_아이디}}:{{그룹_이름_또는_아이디}} {{경로/대상/새로운_루트}}`
