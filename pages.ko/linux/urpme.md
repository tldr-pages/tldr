# urpme

> Mageia에서 패키지를 제거합니다.
> 같이 보기: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpme.8.html>.

- 패키지 제거:

`sudo urpme {{패키지}}`

- 고아 패키지 제거 (주의: 중요한 패키지가 의도치 않게 제거될 수 있습니다):

`sudo urpme --auto-orphans`

- 패키지 및 의존성 제거:

`sudo urpme --auto-orphans {{패키지}}`
