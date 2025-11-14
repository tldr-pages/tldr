# samtools

> 고처리량 시퀀싱(유전체학) 데이터를 처리하기 위한 도구.
> SAM/BAM/CRAM 형식의 데이터를 읽기/쓰기/편집/색인/보기 위해 사용됩니다.
> 더 많은 정보: <https://www.htslib.org/doc/samtools.html>.

- SAM 입력 파일을 BAM 스트림으로 변환하고 파일로 저장:

`samtools view -S -b {{입력.sam}} > {{출력.bam}}`

- `stdin`(-)에서 입력을 받아 특정 영역과 겹치는 모든 읽기 및 SAM 헤더를 `stdout`에 출력:

`{{다른_명령어}} | samtools view -h - chromosome:start-end`

- 파일을 정렬하여 BAM으로 저장 (출력 형식은 출력 파일의 확장자로 자동 결정됨):

`samtools sort {{입력}} -o {{출력.bam}}`

- 정렬된 BAM 파일 색인 ({{sorted_input.bam.bai}} 생성):

`samtools index {{정렬된_입력.bam}}`

- 파일의 정렬 통계 출력:

`samtools flagstat {{정렬된_입력}}`

- 각 색인(염색체/컨티그)에 대한 정렬 수 계산:

`samtools idxstats {{정렬된_색인_입력}}`

- 여러 파일 병합:

`samtools merge {{출력}} {{입력1 입력2 ...}}`

- 읽기 그룹에 따라 입력 파일 분할:

`samtools split {{병합된_입력}}`
