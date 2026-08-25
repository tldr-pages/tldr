# in-toto-record

> 공급망 단계에 대한 증거를 제공하기 위해 서명된 링크 메타데이터 파일을 생성하는 도구.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- 기록 시작 (초기 링크 파일 생성):

`in-toto-record start {{[-n|--step-name]}} {{경로/대상/편집_파일1 경로/대상/편집_파일2 ...}} --signing-key {{경로/대상/키_파일}} {{[-m|--materials]}} {{.}}`

- 기록 종료 (초기 링크 파일이 필요):

`in-toto-record stop {{[-n|--step-name]}} {{경로/대상/편집_파일1 경로/대상/편집_파일2 ...}} --signing-key {{경로/대상/키_파일}} {{[-p|--products]}} {{.}}`
