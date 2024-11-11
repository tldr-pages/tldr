# dnsmap

> dnsmap 명령은 도메인의 일반적인 하위 도메인(e.g. smtp.domain.org)을 스캔합니다.
> 더 많은 정보: <https://github.com/resurrecting-open-source-projects/dnsmap>.

- 내부 단어 목록을 사용하여 하위 도메인 스캔:

`dnsmap {{example.com}}`

- 확인할 하위 도메인 목록 지정:

`dnsmap {{example.com}} -w {{경로/대상/단어목록.txt}}`

- 결과를 CSV 파일에 저장:

`dnsmap {{example.com}} -c {{경로/대상/파일.csv}}`

- 잘못된 양성으로 인식되는 2개의 IP 무시(최대 5개 가능):

`dnsmap {{example.com}} -i {{123.45.67.89,98.76.54.32}}`
