# urpmi.update

> Mageia에서 패키지 저장소의 패키지 목록을 업데이트합니다.
> 참고: Mageia 문서에서는 medium과 저장소를 동의어로 사용합니다.
> 같이 보기: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpmi.update.8.html>.

- 모든 활성 미디어 업데이트:

`urpmi.update -a`

- 특정 미디어 업데이트 (비활성 미디어 포함):

`urpmi.update {{미디어1 미디어2 ...}}`

- 특정 키워드를 포함하는 모든 미디어 업데이트:

`urpmi.update {{키워드}}`

- 모든 구성된 미디어 업데이트:

`urpmi.update e`
