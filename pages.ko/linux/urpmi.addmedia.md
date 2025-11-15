# urpmi.addmedia

> Mageia에 미디어 추가.
> 참고: Mageia 문서에서는 미디엄과 저장소를 동의어로 사용합니다.
> 같이 보기: `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpmi.addmedia.8.html>.

- 미디엄 추가:

`sudo urpmi.addmedia {{미디엄}} {{ftp://ftp.site.com/path/to/Mageia/RPMS}}`

- 하드 드라이브에서 미디엄 추가 (먼저 해당 디렉터리에서 `genhdlist2` 실행):

`sudo urpmi.addmedia --distrib HD file:/{{경로/대상/저장소}}`

- 선택한 미러에서 중요한 미디어 추가:

`sudo urpmi.addmedia --distrib ftp://{{미러_웹사이트}}/mirror/mageia/distrib/{{버전}}/{{아키텍처}}`

- 미러 목록에서 자동으로 미러 선택:

`sudo urpmi.addmedia --distrib --mirrorlist {{미러리스트}}`
