# mkswap

> 디바이스나 파일에 Linux 스왑 영역을 설정합니다.
> 참고: `path/to/file`은 일반 파일 또는 스왑 파티션을 가리킬 수 있습니다.
> 더 많은 정보: <https://manned.org/mkswap>.

- 지정된 스왑 영역 설정:

`sudo mkswap {{경로/대상/파일}}`

- 스왑 영역을 생성하기 전에 파티션의 불량 블록 확인:

`sudo mkswap -c {{경로/대상/파일}}`

- 파티션에 레이블 지정 (레이블을 사용하여 `swapon` 사용 가능):

`sudo mkswap -L {{레이블}} {{/dev/sda1}}`
