# turbo

> JavaScript 및 TypeScript 코드베이스를 위한 고성능 빌드 시스템.
> 같이 보기: `nx`.
> 더 많은 정보: <https://turborepo.org/docs/reference/command-line-reference>.

- 기본 웹 브라우저를 사용하여 Vercel 계정으로 로그인:

`turbo login`

- 현재 디렉토리를 Vercel 조직에 연결하고 원격 캐싱 활성화:

`turbo link`

- 현재 프로젝트 빌드:

`turbo run build`

- 동시성 없이 작업 실행:

`turbo run {{작업_이름}} --concurrency={{1}}`

- 캐시된 아티팩트를 무시하고 모든 작업을 강제로 다시 실행:

`turbo run {{작업_이름}} --force`

- 패키지 전반에 걸쳐 병렬로 작업 실행:

`turbo run {{작업_이름}} --parallel --no-cache`

- 현재 디렉토리를 Vercel 조직에서 연결 해제하고 원격 캐싱 비활성화:

`turbo unlink`

- 특정 작업 실행의 Dot 그래프 생성 (출력 파일 형식은 파일 이름으로 제어 가능):

`turbo run {{작업_이름}} --graph={{경로/대상/파일.html|jpg|json|pdf|png|svg}}`
