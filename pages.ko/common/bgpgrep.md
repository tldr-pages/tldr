# bgpgrep

> MRT 덤프 내의 BGP 데이터 필터링 및 인쇄.
> `gzip`, `bzip2` 및 `xz`로 압축된 파일을 읽을 수 있음.
> 더 많은 정보: <https://codeberg.org/1414codeforge/ubgpsuite>.

- 모든 경로 나열:

`bgpgrep {{master6.mrt}}`

- 피어의 AS 번호로 결정된 특정 피어로부터 수신된 경로를 나열:

`bgpgrep {{master4.mrt}} -peer {{64498}}`

- 피어의 IP 주소로 결정된 특정 피어로부터 수신된 경로를 나열:

`bgpgrep {{master4.mrt.bz2}} -peer {{2001:db8:dead:cafe:acd::19e}}`

- AS 경로에 특정 ASN이 있는 경로를 나열:

`bgpgrep {{master6.mrt.bz2}} -aspath '{{64498 64510}}'`

- 특정 주소로 연결되는 경로 목록:

`bgpgrep {{master6.mrt.bz2}} -supernet '{{2001:db8:dead:cafe:aef::5}}'`

- 특정 AS의 커뮤니티가 있는 경로를 나열:

`bgpgrep {{master4.mrt}} -communities \( '{{64497}}:*' \)`
