# fdroid

> F-Droid 빌드 도구.
> F-Droid는 Android 플랫폼용 FOSS (무료 및 오픈 소스 소프트웨어) 애플리케이션의 설치 가능한 카탈로그.
> 더 많은 정보: <https://f-droid.org/en/docs/Building_Applications/>.

- 특정 앱 구축:

`fdroid build {{앱_아이디}}`

- 빌드 서버 VM에서 특정 앱을 빌드:

`fdroid build {{앱_아이디}} --server`

- 앱을 로컬 저장소에 게시:

`fdroid publish {{앱_아이디}}`

- 연결된 모든 기기에 앱을 설치:

`fdroid install {{앱_아이디}}`

- 메타데이터의 형식이 올바른지 확인:

`fdroid lint --format {{앱_아이디}}`

- 자동으로 서식을 수정 (가능한 경우):

`fdroid rewritemeta {{앱_아이디}}`
