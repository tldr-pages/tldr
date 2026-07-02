# prek

> 커밋 전에 실행되는 Git hook을 생성하고 관리.
> 더 많은 정보: <https://prek.j178.dev/reference/cli/>.

- Git hook에 prek 설치:

`prek install`

- staging된 모든 파일에 대해 prek hook 실행:

`prek run`

- Staging 여부와 관계없이 모든 파일에 대해 prek hook 실행:

`prek run {{[-a|--all-files]}}`

- prek 캐시 정리:

`prek cache clean`

- prek 설정 파일을 저장소의 최신 버전으로 업데이트:

`prek auto-update`
