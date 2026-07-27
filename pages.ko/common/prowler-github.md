# prowler github

> GitHub 계정, 저장소 및 조직의 보안 모범 사례를 점검.
> 관련 항목: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`.
> 더 많은 정보: <https://docs.prowler.com/user-guide/cli/tutorials/misc>.

- 기본 GitHub 보안 검사 실행:

`prowler github`

- GitHub Personal Access Token을 사용해 인증:

`prowler github --personal-access-token {{pat}}`

- GitHub OAuth App Token을 사용하여 인증:

`prowler github --oauth-app-token {{oauth_토큰}}`

- GitHub App ID와 개인 정보키를 사용하여 인증:

`prowler github --github-app-id {{애플리케이션_아이디}} --github-app-key {{애플리케이션_키}}`
