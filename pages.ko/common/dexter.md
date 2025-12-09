# dexter

> OpenId Connect를 사용하여 Kubectl 사용자를 인증하는 도구.
> 더 많은 정보: <https://github.com/gini/dexter>.

- Google OIDC로 사용자 생성 및 인증:

`dexter auth -i {{클라이언트_아이디}} -s {{클라이언트_secret}}`

- 기본 kube 구성파일 위치 재정의:

`dexter auth -i {{클라이언트_아이디}} -s {{클라이언트_secret}} --kube-config {{예시/구성파일}}`
