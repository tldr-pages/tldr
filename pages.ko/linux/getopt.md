# getopt

> 명령줄 인수를 파싱합니다.
> 더 많은 정보: <https://www.gnu.org/software/libc/manual/html_node/Getopt.html>.

- 축약형으로 `verbose`/`version` 플래그를 파싱:

`getopt --options vV --longoptions verbose,version -- --version --verbose`

- 축약형 `-f`로 필수 인자를 갖는 `--file` 옵션 추가:

`getopt --options f: --longoptions file: -- --file=somefile`

- 축약형 `-v`로 선택적 인자를 갖는 `--verbose` 옵션 추가 및 비옵션 매개변수 `arg` 전달:

`getopt --options v:: --longoptions verbose:: -- --verbose arg`

- `-r` 및 `--verbose` 플래그, 선택적 인자를 갖는 `--accept` 옵션, 필수 인자를 갖는 `--target` 옵션을 축약형으로 추가:

`getopt --options rv::s::t: --longoptions verbose,source::,target: -- -v --target target`
