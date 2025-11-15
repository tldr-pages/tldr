# getopt

> 명령줄 인수를 파싱합니다.
> 더 많은 정보: <https://manned.org/getopt>.

- 축약형으로 `verbose`/`version` 플래그를 파싱:

`getopt {{[-o|--options]}} vV {{[-l|--longoptions]}} verbose,version -- --version --verbose`

- 축약형 `-f`로 필수 인자를 갖는 `--file` 옵션 추가:

`getopt {{[-o|--options]}} f: {{[-l|--longoptions]}} file: -- --file=somefile`

- 축약형 `-v`로 선택적 인자를 갖는 `--verbose` 옵션 추가 및 비옵션 매개변수 `arg` 전달:

`getopt {{[-o|--options]}} v:: {{[-l|--longoptions]}} verbose:: -- --verbose arg`

- `-r` 및 `--verbose` 플래그, 선택적 인자를 갖는 `--accept` 옵션, 필수 인자를 갖는 `--target` 옵션을 축약형으로 추가:

`getopt {{[-o|--options]}} rv::s::t: {{[-l|--longoptions]}} verbose,source::,target: -- -v --target target`
