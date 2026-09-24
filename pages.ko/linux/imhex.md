# imhex

> 리버스 엔지니어링과 프로그래밍을 위한 Hex 편집기.
> 더 많은 정보: <https://docs.werwolv.net/imhex/>.

- ImHex에서 파일 열기:

`imhex {{경로/대상/파일}}`

- 새로운 빈 파일 생성:

`imhex --new`

- 실행 중인 ImHex에서 파일을 열고 지정한 바이트 범위 선택 (오프셋은 16진수):

`imhex --open {{경로/대상/파일}} --select {{0xstart_오프셋}} {{0xend_오프셋}}`

- 파일 정보 표시:

`imhex --file-info {{경로/대상/파일}}`

- 지정한 알고리즘으로 파일 해시 계산:

`imhex --hash {{md5|sha1|sha224|sha256|sha384|sha512}} {{경로/대상/파일}}`

- 파일의 hex dump 생성:

`imhex --hexdump {{경로/대상/파일}}`

- 버전 정보 표시:

`imhex --version`
