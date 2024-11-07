# logstash

> Elasticsearch ETL(추출, 변환 및 로드) 도구.
> 주로 다양한 소스(데이터베이스 및 로그 파일 등)에서 Elasticsearch로 데이터를 로드하는 데 사용됩니다.
> 더 많은 정보: <https://www.elastic.co/products/logstash>.

- Logstash 구성의 유효성 검사:

`logstash --configtest --config {{logstash_config.conf}}`

- 구성 파일을 사용하여 Logstash 실행:

`sudo logstash --config {{logstash_구성.conf}}`

- 가장 기본적인 인라인 구성 문자열로 Logstash 실행:

`sudo logstash -e 'input {} filter {} output {}'`
