# swaplabel

> 스왑 영역의 레이블 또는 UUID를 출력하거나 변경합니다.
> 참고: `경로/대상/파일`은 일반 파일 또는 스왑 파티션을 가리킬 수 있습니다.
> 더 많은 정보: <https://manned.org/swaplabel>.

- 스왑 영역의 현재 레이블과 UUID 표시:

`swaplabel {{경로/대상/파일}}`

- 스왑 영역의 레이블 설정:

`swaplabel {{[-L|--label]}} {{새_레이블}} {{경로/대상/파일}}`

- 스왑 영역의 UUID 설정 (UUID는 `uuidgen`을 사용하여 생성할 수 있습니다):

`swaplabel {{[-U|--uuid]}} {{새_UUID}} {{경로/대상/파일}}`
