# chroot

> 특수 루트 디렉토리를 사용하여 명령 또는 대화형 쉘 실행.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- 새로운 루트 디렉토리로 명령어 실행:

`chroot {{/경로/새로운/루트/디렉토리}} {{명령어}}`

- 사용할 사용자 및 그룹(ID 또는 이름) 지정:

`chroot --userspec={{사용자:그룹}}`
