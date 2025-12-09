# npm unstar

> 패키지에서 즐겨찾기/별표 표시를 제거.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-unstar>.

- 기본 레지스트리에서 공개 패키지의 별표 제거:

`npm unstar {{패키지_이름}}`

- 특정 범위 내의 패키지의 별표 제거:

`npm unstar @{{범위}}/{{패키지_이름}}`

- 특정 레지스트리에서 패키지의 별표 제거:

`npm unstar {{패키지_이름}} --registry {{레지스트리_URL}}`

- 인증이 필요한 비공개 패키지의 별표 제거:

`npm unstar {{패키지_이름}} --auth-type {{legacy|oauth|web|saml}}`

- 이중 인증을 위한 OTP를 제공하여 패키지의 별표 제거:

`npm unstar {{패키지_이름}} --otp {{OTP}}`

- 특정 로깅 수준으로 패키지의 별표 제거:

`npm unstar {{패키지_이름}} --loglevel {{silent|error|warn|notice|http|timing|info|verbose|silly}}`
