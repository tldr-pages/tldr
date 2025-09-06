# aws-google-auth

> Google Apps를 페더레이션(Single Sign-On)공급자로 사용하여 AWS 임시(STS) 자격 증명을 획득하는 명령 줄 도구입니다.
> 더 많은 정보: <https://github.com/cevoaustralia/aws-google-auth>.

- IDP및 식별자를 사용하여 Google SSO에 로그인하고 자격 증명 기간을 1시간으로 설정:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- 사용자 역할을 묻는 로그인(여러 개으 사용 가능한 SAML 역할의 경우):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- AWS 계정의 별칭 확인:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- 도움말 정보 보기:

`aws-google-auth -h`
