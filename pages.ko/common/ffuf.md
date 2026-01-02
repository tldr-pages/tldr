# ffuf

> Go로 작성된 빠른 웹 퍼저.
> `FUZZ` 키워드가 자리 표시자로 사용됨. `ffuf`는 `FUZZ`라는 단어를 단어 목록의 모든 단어로 변경해 URL에 접속하려 시도.
> 더 많은 정보: <https://github.com/ffuf/ffuf#usage>.

- 색상 출력([c]olored output)과 대상 URL([u]RL)을 지정하는 단어 리스트([w]ordlist)를 사용하여 디렉토리를 열거:

`ffuf -c -w {{경로/대상/단어목록.txt}} -u {{http://example.com/FUZZ}}`

- 키워드 위치를 변경하여 하위 도메인의 웹서버를 열거:

`ffuf -w {{경로/대상/서브도메인.txt}} -u {{http://FUZZ.example.com}}`

- 지정된 스레드([t]hreads) (기본값: 40)를 퍼징하고 트래픽을 프로파일링(pro[x]ying)하고 출력([o]utput)을 파일에 저장:

`ffuf -o -w {{경로/대상/단어목록.txt}} -u {{http://example.com/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- 특정 헤더([H]eader) ("이름: 값")를 퍼징하고 HTTP 상태 코드와 일치시킴([m]atch):

`ffuf -w {{경로/대상/단어목록.txt}} -u {{http://example.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- 지정된 HTTP 메소드와 데이터([d]ata)를 퍼즈하고, 쉼표로 구분된 상태 코드([c]odes)를 필터링([f]iltering):

`ffuf -w {{경로/대상/포스트데이터.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{http://example.com/login.php}} -fc {{401,403}}`

- 다양한 모드를 사용하여 여러 단어 목록으로 여러 위치를 퍼즈:

`ffuf -w {{경로/대상/keys:KEY}} -w {{경로/대상/values:VALUE}} -mode {{pitchfork|clusterbomb}} -u {{http://example.com/id?KEY=VALUE}}`

- HTTP MITM 프록시(pro[x]y) (Burp Suite 또는 `mitmproxy`)를 통한 프록시 요청:

`ffuf -w {{경로/대상/단어목록}} -x {{http://127.0.0.1:8080}} -u {{http://example.com/FUZZ}}`
