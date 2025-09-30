# mongoexport

> MongoDB 인스턴스에 저장된 데이터를 JSON 또는 CSV 형식으로 내보내기.
> 더 많은 정보: <https://docs.mongodb.com/database-tools/mongoexport/>.

- 컬렉션을 JSON 형식으로 `stdout`에 내보내기:

`mongoexport --uri={{연결_문자열}} --collection={{컬렉션_이름}}`

- 쿼리에 맞는 지정된 컬렉션의 문서를 JSON 파일로 내보내기:

`mongoexport --db={{데이터베이스_이름}} --collection={{컬렉션_이름}} --query="{{쿼리_객체}}" --out={{경로/대상/파일.json}}`

- 문서를 한 줄에 하나의 객체 대신 JSON 배열로 내보내기:

`mongoexport --collection={{컬렉션_이름}} --jsonArray`

- 문서를 CSV 파일로 내보내기:

`mongoexport --collection={{컬렉션_이름}} --type={{csv}} --fields="{{필드1,필드2,...}}" --out={{경로/대상/파일.csv}}`

- 지정된 파일의 쿼리에 맞는 문서를 CSV 파일로 내보내고, 첫 번째 줄에 필드 이름 목록 생략:

`mongoexport --collection={{컬렉션_이름}} --type={{csv}} --fields="{{필드1,필드2,...}}" --queryFile={{경로/대상/파일}} --noHeaderLine --out={{경로/대상/파일.csv}}`

- 문서를 사람이 읽을 수 있는 JSON 형식으로 `stdout`에 내보내기:

`mongoexport --uri={{몽고DB_URI}} --collection={{컬렉션_이름}} --pretty`

- 도움말 표시:

`mongoexport --help`
