# blastp

> 단백질-단백질 BLAST.
> 더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- e-value 임계값이 1e-9인 경우, 쌍별 출력 형식으로 두 개 이상의 서열을 blastp로 정렬하고 화면에 출력:

`blastp -query {{쿼리.fa}} -subject {{대상.fa}} -evalue {{1e-9}}`

- blastp-fast를 사용하여 두 개 이상의 서열 정렬:

`blastp -task blastp-fast -query {{쿼리.fa}} -subject {{대상.fa}}`

- 사용자 정의 테이블 형식으로 두 개 이상의 서열 정렬하고 파일에 출력:

`blastp -query {{쿼리.fa}} -subject {{대상.fa}} -outfmt '{{6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident}}' -out {{출력.tsv}}`

- 단백질 쿼리를 사용하여 단백질 데이터베이스 검색, BLAST 검색에 사용할 16개의 스레드, 최대 10개의 정렬된 서열 유지:

`blastp -query {{쿼리.fa}} -db {{blast_데이터베이스_이름}} -num_threads {{16}} -max_target_seqs {{10}}`

- 원격 비중복 단백질 데이터베이스를 단백질 쿼리로 검색:

`blastp -query {{쿼리.fa}} -db {{nr}} -remote`

- 도움말 표시 (`-help`로 자세한 도움말 확인 가능):

`blastp -h`
