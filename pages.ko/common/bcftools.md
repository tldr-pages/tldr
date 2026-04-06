# bcftools

> VCF 및 BCF 파일을 조작하기 위한 도구 모음.
> 더 많은 정보: <https://samtools.github.io/bcftools/bcftools.html>.

- BCF 파일을 확인하고 `stdout`으로 [v]CF 형식으로 변환:

`bcftools view {{경로/대상/입력파일.bcf}} {{[-O|--output-type]}} v`

- VCF 파일의 변이를 염색체와 위치 기준으로 정렬하고, [b]CF 파일로 출력 후 인덱스 생성:

`bcftools sort {{경로/대상/입력파일.vcf.gz}} {{[-O|--output-type]}} b {{[-o|--output]}} {{경로/대상/sorted.bcf}} {{[-W|--write-index]}}`

- 동일한 샘플을 공유하는 정렬된 VCF 파일들을 압축([z]ipped) VCF로 `stdout`에 결합:

`bcftools concat {{경로/대상/chr1.vcf.gz 경로/대상/chr2.vcf.gz ...}} {{[-O|--output-type]}} z`

- 낮은 품질 변이를 필터링하고 FILTER 컬럼에 "LowQual" 태그 추가:

`bcftools filter {{[-e|--exclude]}} 'QUAL<20' {{[-s|--soft-filter]}} LowQual {{경로/대상/입력파일.vcf.gz}}`

- tabix 인덱스된 테이블에서 주석 컬럼을 추가해 `stdout`으로 출력:

`bcftools annotate {{[-a|--annotations]}} {{경로/대상/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{경로/대상/입력파일.vcf.gz}}`

- VCF 파일 간 변이 교집합([i]nter[sec]tion)을 4개 스레드로 계산하여 출력:

`bcftools isec {{경로/대상/a.vcf.gz 경로/대상/b.vcf.gz ...}} --threads 4 {{[-o|--output]}} {{경로/대상/intersection.vcf}}`

- 인덱스 없이 VCF 파일들의 비중복 샘플 병합 `stdout`:

`bcftools merge {{경로/대상/cohort1.vcf.gz}} {{경로/대상/cohort2.vcf.gz}} --no-index`

- bgzip으로 압축된 VCF 파일에 대한 인덱스 생성:

`bcftools index {{경로/대상/입력파일.vcf.gz}}`
