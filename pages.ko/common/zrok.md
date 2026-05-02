# zrok

> 로컬 서비스와 파일을 인터넷에 노출할 수 있는 도구.
> OpenZiti 프로젝트의 일부로, 보안 중심의 zero-trust 공유를 제공.
> 더 많은 정보: <https://docs.zrok.io/>.

- 공개 zrok 서비스 사용을 위한 초대 요청 (최초 1회 실행):

`zrok invite`

- 초대 이메일의 토큰으로 zrok 환경 활성화:

`zrok enable {{토큰}}`

- 로컬 웹 서버를 공개 URL로 공유:

`zrok share public {{http://localhost:8080}}`

- 고유 토큰으로만 접근 가능한 보안 공유 생성:

`zrok share private {{http://localhost:3000}}`

- 다른 사용자가 만든 private 공유에 접근:

`zrok access private {{공유_토큰}}`

- 로컬 디렉터리를 간단한 웹사이트로 공개:

`zrok share public --backend-mode web {{경로/대상/디렉터리}}`

- zrok 환경 상태 및 활성 공유 확인:

`zrok status`
