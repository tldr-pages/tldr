# tsv-filter

> 개별 필드에 대한 테스트를 실행하여 TSV 파일의 행을 필터링합니다.
> 더 많은 정보: <https://github.com/eBay/tsv-utils#tsv-filter>.

- 특정 열이 주어진 숫자와 수치적으로 같은 행을 출력:

`tsv-filter -H --eq {{필드_이름}}:{{숫자}} {{경로/대상/tsv_파일}}`

- 특정 열이 주어진 숫자와 [eq]ual/[n]on [e]qual/[l]ess [t]han/[l]ess than or [e]qual/[g]reater [t]han/[g]reater than or [e]qual한 행을 출력:

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{열_번호}}:{{숫자}} {{경로/대상/tsv_파일}}`

- 특정 열이 주어진 문자열과 [eq]ual/[n]ot [e]qual/포함됨/포함되지 않음을 만족하는 행을 출력:

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{열_번호}}:{{문자열}} {{경로/대상/tsv_파일}}`

- 비어 있지 않은 필드를 필터링:

`tsv-filter --not-empty {{열_번호}} {{경로/대상/tsv_파일}}`

- 특정 열이 비어 있는 행을 출력:

`tsv-filter --invert --not-empty {{열_번호}} {{경로/대상/tsv_파일}}`

- 두 조건을 만족하는 행을 출력:

`tsv-filter --eq {{열_번호1}}:{{숫자}} --str-eq {{열_번호2}}:{{문자열}} {{경로/대상/tsv_파일}}`

- 최소한 하나의 조건을 만족하는 행을 출력:

`tsv-filter --or --eq {{열_번호1}}:{{숫자}} --str-eq {{열_번호2}}:{{문자열}} {{경로/대상/tsv_파일}}`

- 첫 번째 행을 [H]eader로 해석하여 일치하는 행 개수 세기:

`tsv-filter --count -H --eq {{필드_이름}}:{{숫자}} {{경로/대상/tsv_파일}}`
