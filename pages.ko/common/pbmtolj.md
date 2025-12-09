# pbmtolj

> PBM 파일을 HP LaserJet 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtolj.html>.

- PBM 파일을 HP LaserJet 파일로 변환:

`pbmtolj {{경로/대상/입력.pbm}} > {{경로/대상/output.lj}}`

- 지정된 방법으로 출력 파일 압축:

`pbmtolj -{{packbits|delta|compress}} {{경로/대상/입력.pbm}} > {{경로/대상/output.lj}}`

- 필요한 해상도 지정:

`pbmtolj -resolution {{75|100|150|300|600}} {{경로/대상/입력.pbm}} > {{경로/대상/output.lj}}`
