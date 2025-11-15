# gau

> 모든 URL 가져오기: AlienVault의 Open Threat Exchange, Wayback Machine, 및 모든 도메인에 대한 Common Crawl에서 알려진 URL을 가져옴.
> 더 많은 정보: <https://github.com/lc/gau>.

- AlienVault의 Open Threat Exchange, Wayback Machine, Common Crawl 및 URLScan에서 도메인의 모든 URL을 가져옴:

`gau {{example.com}}`

- 여러 도메인의 URL을 가져옴:

`gau {{도메인1 도메인2 ...}}`

- 여러 스레드를 실행하여 입력 파일에서 여러 도메인의 모든 URL을 가져옴:

`gau --threads {{4}} < {{경로/대상/도메인.txt}}`

- 출력([o]utput) 결과를 파일에 기록:

`gau {{example.com}} --o {{경로/대상/찾은_주소.txt}}`

- 특정 제공업체의 URL만 검색:

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{example.com}}`

- 여러 제공업체의 URL 검색:

`gau --providers {{wayback,otx,...}} {{example.com}}`

- 특정 날짜 범위 내의 URL 검색:

`gau --from {{YYYYMM}} --to {{YYYYMM}} {{example.com}}`
