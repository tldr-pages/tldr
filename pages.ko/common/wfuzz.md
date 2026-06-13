# wfuzz

> 웹 애플리케이션 브루트포스 도구.
> 더 많은 정보: <https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>.

- 지정된 [w]ordlist 및 [p]roxy를 사용하여 디렉토리 및 파일 브루트포스:

`wfuzz -w {{경로/대상/파일}} -p {{127.0.0.1:8080:HTTP}} {{http://example.com/FUZZ}}`

- 결과를 [f]ile에 저장:

`wfuzz -w {{경로/대상/파일}} -f {{파일이름}} {{http://example.com/FUZZ}}`

- 색상 출력 및 지정한 응답 코드만 표시:

`wfuzz -c -w {{경로/대상/파일}} --sc {{200,301,302}} {{http://example.com/FUZZ}}`

- 사용자 정의 [H]eader를 사용하여 서브도메인 퍼징, 특정 응답 [c]odes 및 단어 수 숨김. [t]hreads를 100으로 증가시키고 대상 ip/도메인 포함:

`wfuzz -w {{경로/대상/파일}} -H "{{Host: FUZZ.example.com}}" --hc {{301}} --hw {{222}} -t {{100}} {{example.com}}`

- 파일에서 각 FUZ[z] 키워드에 대한 사용자 명과 비밀번호 목록을 사용하여 기본 인증 브루트포스, 실패한 시도에 대한 응답 [c]odes 숨김:

`wfuzz -c --hc {{401}} -s {{요청 간 지연 시간(초)}} -z file,{{경로/대상/사용자명}} -z file,{{경로/대상/비밀번호}} --basic 'FUZZ:FUZ2Z' {{https://example.com}}`

- 커맨드라인에서 직접 워드리스트 제공 및 POST 요청을 사용하여 퍼징:

`wfuzz -z list,{{word1-word2-...}} {{https://api.example.com}} -d "{{id=FUZZ&showwallet=true}}"`

- 파일에서 워드리스트를 제공하며 base64 및 md5 인코딩 적용 (`wfuzz -e encoders`로 사용 가능한 모든 인코더 나열):

`wfuzz -z file,{{경로/대상/파일}},none-base64-md5 {{https://example.com/FUZZ}}`

- 사용 가능한 인코더/페이로드/이터레이터/프린터/스크립트 나열:

`wfuzz -e {{encoders|payloads|iterators|printers|scripts}}`
