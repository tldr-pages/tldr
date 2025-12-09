# mt

> 자기 테이프 드라이브 작동 제어 (일반적으로 LTO 테이프).
> 더 많은 정보: <https://manned.org/mt>.

- 테이프 드라이브 상태 확인:

`mt -f {{/dev/nstX}} status`

- 테이프를 처음으로 되감기:

`mt -f {{/dev/nstX}} rewind`

- 주어진 파일 수만큼 앞으로 이동한 후, 다음 파일의 첫 번째 블록에 테이프 위치:

`mt -f {{/dev/nstX}} fsf {{개수}}`

- 테이프를 되감은 후, 주어진 파일의 시작 부분에 테이프 위치:

`mt -f {{/dev/nstX}} asf {{개수}}`

- 유효한 데이터 끝 부분에 테이프 위치:

`mt -f {{/dev/nstX}} eod`

- 테이프를 되감고 언로드/배출:

`mt -f {{/dev/nstX}} eject`

- 현재 위치에 EOF (파일 끝) 마크 작성:

`mt -f {{/dev/nstX}} eof`
