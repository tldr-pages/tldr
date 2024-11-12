# rustscan

> Rust로 작성된 빠른 포트 스캐너로 `nmap`이 내장되어 있습니다.
> 더 많은 정보: <https://github.com/RustScan/RustScan>.

- 기본값을 사용하여 쉼표로 구분된 하나 이상의 [a]드레스를 대상으로 모든 포트를 스캔:

`rustscan --addresses {{ip_또는_호스트명}}`

- [t]op 1000 포트를 서비스 및 버전 감지와 함께 스캔:

`rustscan --top --addresses {{주소_또는_주소들}}`

- 특정 [p]ort 목록을 스캔:

`rustscan --ports {{포트1,포트2,...,포트N}} --addresses {{주소_또는_주소들}}`

- 특정 범위의 포트를 스캔:

`rustscan --range {{시작-끝}} --addresses {{주소_또는_주소들}}`

- `nmap`에 스크립트 인수 추가:

`rustscan --addresses {{주소_또는_주소들}} -- -A -sC`

- 사용자 정의 [b]atch 크기(기본: 4500) 및 [t]imeout(기본: 1500ms)으로 스캔:

`rustscan --batch-size {{배치_크기}} --timeout {{타임아웃}} --addresses {{주소_또는_주소들}}`

- 특정 포트 순서로 스캔:

`rustscan --scan-order {{serial|random}} --addresses {{주소_또는_주소들}}`

- greppable 모드로 스캔(`nmap` 없이 포트 출력만):

`rustscan --greppable --addresses {{주소_또는_주소들}}`
