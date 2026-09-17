# cfv

> 체크섬 파일을 생성하고 검증하는 명령줄 도구.
> 더 많은 정보: <https://manned.org/cfv>.

- 현재 디렉터리의 체크섬 파일 검증([T]est):

`cfv -T`

- 체크섬 파일([f]ile)을 사용해 테스트([T]est) 상세 출력([v]erbosely), 잘못된 파일 이름 변경(re[n]ame), 검증되지 않은([u]nverified) 파일 표시:

`cfv -Tvnu -f {{path/to/file}}`

- 선택한 파일들에 대해 특정 타입([t]ype)의 체크섬 파일 생성([C]reate):

`cfv -C -t "{{sfv|sha256|md5|...}}" {{file1 file2 ...}}`

- 선택된 디렉터리를 재귀적으로([r]ecursively) 순회하며 각각의 체크섬 파일 생성([C]reate):

`cfv -Cr`

- 모든 재귀 파일([rr]ecursively)에 대해 하나의 `sha256` 체크섬 파일 생성([C]reate):

`cfv -C -f {{sums.sha256}} -rr`

- `g[z]ipped` 으로 압축된 `.sfv` 파일을 상세 출력([v]erbosely)과 함께 생성([C]reate), 심볼릭 링크(`sym[l]inks`)를 따라가고, `경로/대상/디렉터리`를 기본 경로([p]ath)로 설정:

`cfv -Czvl -p {{경로/대상/디렉터리}}`
