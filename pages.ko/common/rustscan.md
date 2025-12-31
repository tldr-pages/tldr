# rustscan

> Rust로 작성된 빠른 포트 스캐너로 `nmap`이 내장되어 있습니다.
> 더 많은 정보: <https://github.com/bee-san/RustScan/wiki>.

- 기본값을 사용하여 쉼표로 구분된 하나 이상의 주소의 모든 포트를 스캔합니다:

`rustscan {{[-a|--addresses]}} {{ip_또는_호스트명}}`

- 서비스 및 버전 감지 기능으로 상위 1000개 포트 스캔하기:

`rustscan --top {{[-a|--addresses]}} {{주소_또는_주소들}}`

- 특정 포트 목록 스캔:

`rustscan {{[-p|--ports]}} {{포트1,포트2,...,포트N}} {{[-a|--addresses]}} {{주소_또는_주소들}}`

- 특정 범위의 포트를 스캔:

`rustscan {{[-r|--range]}} {{시작}}-{{끝}} {{[-a|--addresses]}} {{주소_또는_주소들}}`

- `nmap`에 스크립트 인수 추가:

`rustscan {{[-a|--addresses]}} {{주소_또는_주소들}} -- -O {{[-sC|--script=default]}}`

- 사용자 정의 batch 크기(기본: 4500) 및 timeout(기본: 1500ms)으로 스캔:

`rustscan {{[-b|--batch-size]}} {{배치_크기}} {{[-t|--timeout]}} {{타임아웃}} {{[-a|--addresses]}} {{주소_또는_주소들}}`

- 특정 포트 순서로 스캔:

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{주소_또는_주소들}}`

- greppable 모드로 스캔(`nmap` 없이 포트 출력만):

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{주소_또는_주소들}}`
