# urpmi

> Mageia에서 패키지를 설치합니다.
> 같이 보기: `urpm.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpmi.8.html>.

- 저장소 또는 로컬 RPM 파일에서 패키지 설치:

`sudo urpmi {{패키지|경로/대상/파일.rpm}}`

- 패키지를 다운로드만 하고 설치하지 않음:

`urpmi --no-install {{패키지}}`

- 설치된 모든 패키지 업데이트 (`urpmi.update -a`를 실행하여 사용 가능한 업데이트 확인):

`sudo urpmi --auto-select`

- 네트워크의 하나 이상의 머신에서 `/etc/urpmi/parallel.cfg`에 따라 패키지 업데이트:

`sudo urpmi --parallel local {{패키지}}`

- 모든 고아 패키지를 수동으로 설치됨으로 표시:

`sudo urpmi $(urpmq --auto-orphans -f)`
