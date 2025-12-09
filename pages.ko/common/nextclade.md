# nextclade

> 바이러스 유전체 정렬, 계통 할당 및 품질 검사를 위한 생물정보학 도구.
> 더 많은 정보: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/reference.html>.

- 사용자 제공 [r]eference에 시퀀스를 정렬하고, 정렬 결과를 파일로 출력:

`nextclade run {{경로/대상/시퀀스.fa}} -r {{경로/대상/레퍼런스.fa}} -o {{경로/대상/정렬결과.fa}}`

- 최신 [d]ataset을 자동으로 다운로드하여 [t]SV 보고서 생성:

`nextclade run {{경로/대상/fasta}} -d {{데이터셋_이름}} -t {{경로/대상/보고서.tsv}}`

- 사용 가능한 모든 데이터셋 나열:

`nextclade dataset list`

- 최신 SARS-CoV-2 데이터셋 다운로드:

`nextclade dataset get --name sars-cov-2 --output-dir {{경로/대상/폴더}}`

- 다운로드한 [D]ataset을 사용하여 모든 [O]utputs 생성:

`nextclade run -D {{경로/대상/데이터셋_폴더}} -O {{경로/대상/출력_폴더}} {{경로/대상/시퀀스.fasta}}`

- 여러 파일에서 실행:

`nextclade run -d {{데이터셋_이름}} -t {{경로/대상/출력_tsv}} -- {{경로/대상/입력_fasta_1 경로/대상/입력_fasta_2 ...}}`

- 시퀀스가 정렬되지 않을 경우 역상보 시도:

`nextclade run --retry-reverse-complement -d {{데이터셋_이름}} -t {{경로/대상/출력_tsv}} {{경로/대상/입력_fasta}}`
