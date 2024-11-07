# in-toto-record

> 공급망 단계에 대한 증거를 제공하기 위해 서명된 링크 메타데이터 파일을 생성.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- 기록 시작 (예비 링크 파일 생성):

`in-toto-record start -n {{경로/대상/편집_파일1 경로/대상/편집_파일2 ...}} -k {{경로/대상/키_파일}} -m {{.}}`

- 녹음 중지 (예비 링크 파일 예상):

`in-toto-record stop -n {{경로/대상/편집_파일1 경로/대상/편집_파일2 ...}} -k {{경로/대상/키_파일}} -p {{.}}`
