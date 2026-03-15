# cariddi

> 도메인 목록에서 URL을 크롤링하고 엔드포인트, 비밀정보, API 키, 파일 확장자, 토큰 등을 탐지.
> 더 많은 정보: <https://github.com/edoardottt/cariddi/wiki>.

- 사용자 정의 `regex`를 사용하여 비밀 정보를 탐지하고 결과를 JSON 형식으로 출력:

`cat {{경로/대상/urls.txt}} | cariddi -s -sf {{경로/대상/사용자지정_비밀정보.txt}} -json`

- 높은 동시성 및 타임아웃 설정으로 유용한 엔드포인트를 탐지하고 결과를 일반 텍스트로 출력:

`cat {{경로/대상/urls.txt}} | cariddi -e -c {{250}} -t {{15}} -plain`

- 디버그 모드로 크롤링하고 HTTP 응답을 저장하며 결과를 `txt` 파일로 출력:

`cat {{경로/대상/urls.txt}} | cariddi -debug -sr -ot {{경로/대상/디버그_출력.txt}}`

- 프록시와 랜덤 사용자 에이전트를 사용해 집중적인 크롤링을 수행하고 결과를 `html` 파일로 출력:

`cat {{경로/대상/urls.txt}} | cariddi -intensive -proxy {{http://127.0.0.1:8080}} -rua -oh {{경로/대상/intensive_crawl.html}}`

- 사용자 정의 지연 시간을 설정해 오류 및 유용한 정보를 탐지하고 `.cariddi_cache` 폴더를 캐시로 사용:

`cat {{경로/대상/urls.txt}} | cariddi -err -info -d {{3}} -cache`

- 사용 예시를 표시:

`cariddi -examples`
