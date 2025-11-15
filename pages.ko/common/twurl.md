# twurl

> Twitter API에 특화된 Curl과 유사한 명령어.
> 더 많은 정보: <https://github.com/twitter/twurl>.

- Twitter 계정에 대한 접근을 승인:

`twurl authorize --consumer-key {{트위터_API_키}} --consumer-secret {{트위터_API_비밀}}`

- API 엔드포인트에 GET 요청 수행:

`twurl -X GET {{트위터_API_엔드포인트}}`

- API 엔드포인트에 POST 요청 수행:

`twurl -X POST -d '{{엔드포인트_파라미터}}' {{트위터_API_엔드포인트}}`

- Twitter에 미디어 업로드:

`twurl -H "{{트위터_업로드_URL}}" -X POST "{{트위터_업로드_엔드포인트}}" --file "{{경로/대상/미디어.jpg}}" --file-field "media"`

- 다른 Twitter API 호스트에 접근:

`twurl -H {{트위터_API_URL}} -X GET {{트위터_API_엔드포인트}}`

- 요청한 리소스에 대한 별칭 생성:

`twurl alias {{별칭_이름}} {{리소스}}`
