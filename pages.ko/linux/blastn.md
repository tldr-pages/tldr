# blastn

> 뉴클레오타이드-뉴클레오타이드 BLAST.
> 더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- 메가블라스트(기본값)를 사용하여 두 개 이상의 서열 정렬, e-value 임계값 1e-9, 쌍별 출력 형식(기본값):

`blastn -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- blastn을 사용하여 두 개 이상의 서열 정렬:

`blastn -task blastn -query {{query.fa}} -subject {{subject.fa}}`

- 사용자 정의 표형식 출력, 파일로 출력:

`blastn -query {{query.fa}} -subject {{subject.fa}} -outfmt {{'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'}} -out {{output.tsv}}`

- 뉴클레오타이드 쿼리를 사용하여 뉴클레오타이드 데이터베이스 검색, BLAST 검색에 사용할 스레드(CPU) 16개, 최대 10개의 정렬된 서열 유지:

`blastn -query {{query.fa}} -db {{경로/대상/blast_db}} -num_threads {{16}} -max_target_seqs {{10}}`

- 원격 비중복 뉴클레오타이드 데이터베이스를 뉴클레오타이드 쿼리로 검색:

`blastn -query {{query.fa}} -db {{nt}} -remote`

- 도움말 표시 (`-help`로 자세한 도움말 사용):

`blastn -h`
