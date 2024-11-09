# mongoimport

> JSON, CSV, 또는 TSV 파일의 내용을 MongoDB 데이터베이스로 가져오기.
> 더 많은 정보: <https://docs.mongodb.com/database-tools/mongoimport/>.

- 특정 컬렉션에 JSON 파일 가져오기:

`mongoimport --file={{경로/대상/파일.json}} --uri={{mongodb_uri}} --collection={{컬렉션_이름}}`

- CSV 파일을 가져와서 파일의 첫 번째 줄을 필드 이름으로 사용:

`mongoimport --type={{csv}} --file={{경로/대상/파일.csv}} --db={{데이터베이스_이름}} --collection={{컬렉션_이름}}`

- JSON 배열을 가져와서 각 요소를 별도의 문서로 사용:

`mongoimport --jsonArray --file={{경로/대상/파일.json}}`

- 특정 모드와 기존 문서를 일치시키는 쿼리를 사용하여 JSON 파일 가져오기:

`mongoimport --file={{경로/대상/파일.json}} --mode={{delete|merge|upsert}} --upsertFields="{{필드1,필드2,...}}"`

- 별도의 CSV 파일에서 필드 이름을 읽고 빈 값의 필드를 무시하여 CSV 파일 가져오기:

`mongoimport --type={{csv}} --file={{경로/대상/파일.csv}} --fieldFile={{경로/대상/필드_파일.csv}} --ignoreBlanks`

- 도움말 표시:

`mongoimport --help`
