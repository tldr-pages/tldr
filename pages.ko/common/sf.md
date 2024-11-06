# sf

> Salesforce 조직과 작업할 때 개발 및 빌드 자동화를 단순화하는 강력한 명령줄 인터페이스.
> 더 많은 정보: <https://developer.salesforce.com/tools/salesforcecli>.

- Salesforce 조직 승인:

`sf force:auth:web:login --setalias {{조직}} --instanceurl {{조직_URL}}`

- 승인된 모든 조직 나열:

`sf force:org:list`

- 기본 웹 브라우저에서 특정 조직 열기:

`sf force:org:open --targetusername {{조직}}`

- 특정 조직에 대한 정보 표시:

`sf force:org:display --targetusername {{조직}}`

- 소스 메타데이터를 조직에 푸시:

`sf force:source:push --targetusername {{조직}}`

- 소스 메타데이터를 조직에서 가져오기:

`sf force:source:pull --targetusername {{조직}}`

- 조직에 로그인한 사용자의 비밀번호 생성:

`sf force:user:password:generate --targetusername {{조직}}`

- 조직에 로그인한 사용자에게 권한 세트 할당:

`sf force:user:permset:assign --permsetname {{권한_세트_이름}} --targetusername {{조직}}`
