# ntfyme

> 장기 실행 종료 프로세스를 추적하고 알림을 보내는 알림 도구.
> Gmail, Telegram 등을 통해 성공/오류 메시지로 알림을 전송.
> 더 많은 정보: <https://github.com/AnirudhG07/ntfyme>.

- 명령어를 직접 실행:

`ntfyme exec {{[-c|--cmd]}} {{명령어}}`

- 명령어를 파이프로 전달하여 실행:

`echo {{명령어}} | ntfyme exec`

- 여러 명령어를 큰따옴표로 묶어 실행:

`echo "{{명령어1; 명령어2; 명령어3}}" | ntfyme exec`

- 장기 중단 후 프로세스를 추적하고 종료:

`ntfyme exec {{[-t|--track-process]}} {{[-c|--cmd]}} {{명령어}}`

- 도구 구성을 대화식으로 설정:

`ntfyme setup`

- 비밀번호 암호화:

`ntfyme enc`

- 로그 기록 보기:

`ntfyme log`

- 구성 파일 열기 및 편집:

`ntfyme config`
