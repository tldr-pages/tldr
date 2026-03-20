# chkrootkit

> 시스템에서 루트킷을 검사.
> 더 많은 정보: <https://manned.org/chkrootkit>.

- 조용한([q]uiet) 모드를 활성화하여 일반 테스트 결과 출력을 생략:

`chkrootkit -q`

- 전문가(e[x]pert) 모드를 활성화하여 추가 출력을 표시:

`chkrootkit -x`

- 디버그([d]ebug) 모드를 활성화하여 모든 출력을 표시:

`chkrootkit -d`

- 일부 테스트에서 제외할([e]xcluded) 파일을 지정:

`chkrootkit -e "{{경로/대상/파일}}"`

- 테스트를 위한 루트([r]oot) 디렉터리를 지정 (예. 마운트된 `ext` 드라이브):

`chkrootkit -r {{경로/대상/디렉터리}}`

- NFS로 마운트된([n]fs-mounted) 디렉터리를 무시:

`chkrootkit -n`

- 테스트([T]ests)를 실행하며 특정 파일 시스템 유형을 무시:

`chkrootkit -T {{파일_시스템_유형}}`

- 사용 가능한 테스트 목록([l]ist)을 생성:

`chkrootkit -l`
