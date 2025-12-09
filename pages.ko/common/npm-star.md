# npm star

> 패키지를 즐겨찾기로 표시.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-star>.

- 기본 레지스트리에서 공개 패키지 즐겨찾기:

`npm star {{패키지_이름}}`

- 특정 스코프 내의 패키지 즐겨찾기:

`npm star @{{스코프}}/{{패키지_이름}}`

- 특정 레지스트리에서 패키지 즐겨찾기:

`npm star {{패키지_이름}} --registry {{레지스트리_URL}}`

- 인증이 필요한 비공개 패키지 즐겨찾기:

`npm star {{패키지_이름}} --auth-type {{legacy|oauth|web|saml}}`

- 2단계 인증을 위한 OTP를 제공하여 패키지 즐겨찾기:

`npm star {{패키지_이름}} --otp {{OTP}}`

- 자세한 로그와 함께 패키지 즐겨찾기:

`npm star {{패키지_이름}} --loglevel verbose`

- 즐겨찾기한 모든 패키지 나열:

`npm star --list`

- 특정 레지스트리에서 즐겨찾기한 패키지 나열:

`npm star --list --registry {{레지스트리_URL}}`
