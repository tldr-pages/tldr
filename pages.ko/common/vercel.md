# vercel

> 당신의 Vercel 프로젝트들을 관리하고 배포하세요.
> 더 많은 정보: <https://vercel.com/docs/cli>.

- 현재 디렉토리를 배포:

`vercel`

- 현재 디렉토리를 프로덕션에 배포:

`vercel --prod`

- 특정 디렉토리를 배포:

`vercel {{경로/대상/프로젝트}}`

- 예제 프로젝트를 초기화:

`vercel init`

- 환경 변수와 함께 배포:

`vercel --env {{ENV}}={{var}}`

- 환경 변수와 함께 빌드:

`vercel --build-env {{ENV}}={{var}}`

- 배포를 적용할 기본 지역을 설정:

`vercel --regions {{region_id}}`

- 배포된 프로젝트를 제거:

`vercel remove {{프로젝트_이름}}`
