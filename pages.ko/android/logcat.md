# logcat

> 오류 발생 시, 스택 추적을 포함한 시스템 메시지 로그와 애플리케이션에서 기록한 정보 메시지를 덤프합니다.
> 더 많은 정보: <https://developer.android.com/tools/logcat>.

- 시스템 로그 표시:

`logcat`

- 파일에 시스템 로그 작성:

`logcat -f {{경로/대상/파일}}`

- 정규표현식과 일치하는 행 표시:

`logcat --regex {{정규_표현식}}`

- 특정 PID에 대한 로그 표시:

`logcat --pid {{프로세스_id}}`

- 특정 패키지의 프로세스에 대한 로그 표시:

`logcat --pid $(pidof -s {{패키지}})`
