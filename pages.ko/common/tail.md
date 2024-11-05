# tail

> 파일의 마지막 부분을 표시.
> 같이 보기: `head`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/tail>.

- 파일에서 마지막 'count' 줄 표시:

`tail --lines {{줄_수}} {{경로/대상/파일}}`

- 특정 줄 번호부터 파일 출력:

`tail --lines +{{줄_수}} {{경로/대상/파일}}`

- 주어진 파일의 끝에서 특정 바이트 수 출력:

`tail --bytes {{바이트_수}} {{경로/대상/파일}}`

- 주어진 파일의 마지막 줄을 출력하고 `Ctrl + C`를 누를 때까지 계속 읽기:

`tail --follow {{경로/대상/파일}}`

- 파일이 접근할 수 없는 경우에도 `Ctrl + C`를 누를 때까지 계속 읽기:

`tail --retry --follow {{경로/대상/파일}}`

- '파일'의 마지막 'num' 줄을 표시하고 'n' 초마다 새로 고침:

`tail --lines {{줄_수}} --sleep-interval {{초}} --follow {{경로/대상/파일}}`
