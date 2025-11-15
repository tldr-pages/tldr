# grub-script-check

> `grub-script-check` 프로그램은 GRUB 스크립트 파일을 가져와 문법 오류를 검사합니다.
> 경로를 옵션이 아닌 인수로 받을 수 있습니다. 인수가 없을 경우, `stdin`에서 읽습니다.
> 더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dscript_002dcheck>.

- 특정 스크립트 파일의 문법 오류 검사:

`grub-script-check {{경로/대상/grub_설정_파일}}`

- 입력을 읽은 후 각 줄을 표시:

`grub-script-check --verbose`

- 도움말 표시:

`grub-script-check --help`

- 버전 표시:

`grub-script-check --version`
