# dnsx

> 여러 DNS 쿼리를 실행하기 위한 빠르고 목적이 다양한 DNS 도구 키트.
> 참고: 어떤 경우에는 `dnsx`에 대한 입력이 `stdin` (파이프 `|`)를 통해 전달되어야 함.
> 같이 보기: `dig`, `dog`, `dnstracer`.
> 더 많은 정보: <https://docs.projectdiscovery.io/tools/dnsx/running>.

- (하위)도메인의 A 레코드를 쿼리하고 수신된 응답([re]sponse)을 표시:

`echo {{example.com}} | dnsx -a -re`

- 모든 DNS 레코드(A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA)를 쿼리:

`dnsx -recon -re <<< {{example.com}}`

- 특정 유형의 DNS 레코드를 쿼리:

`echo {{example.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- 응답([r]esponse)만 ([o]nly) 출력 (쿼리된 도메인이나 하위 도메인은 표시하지 않음):

`echo {{example.com}} | dnsx -ro`

- 쿼리의 원시 응답을 표시하고, 실패에 대한 시도를 라도 재시도할 [r]esolvers를 지정:

`echo {{example.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- 자리 표시자를 사용한 무차별 대입 DNS 레코드:

`dnsx -domain {{FUZZ.example.com}} -wordlist {{경로/대상/단어목록.txt}} -re`

- DNS 도메인([d]omains) 및 단어 목록의 무차별 대입 DNS 레코드를 색상 코드가 없는([n]o [c]olor) 파일에 출력([o]utput) 결과를 추가:

`dnsx -domain {{경로/대상/도메인.txt}} -wordlist {{경로/대상/단어목록.txt}} -re -output {{경로/대상/출력.txt}} -no-color`

- 초당 DNS 쿼리 속도를 제한하여([r]ate [l]imiting) 지정된 하위 도메인 목록에 대한 `CNAME` 레코드를 추출:

`subfinder -silent -d {{example.com}} | dnsx -cname -re -rl {{숫자}}`
