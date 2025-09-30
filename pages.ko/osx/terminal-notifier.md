# terminal-notifier

> macOS 사용자 알림을 전송합니다.
> 더 많은 정보: <https://github.com/julienXX/terminal-notifier>.

- 알림 전송 (메시지만 필수):

`terminal-notifier -group {{tldr-info}} -title {{TLDR}} -message '{{TLDR rocks}}'`

- 소리와 함께 파이프로 전달된 데이터 표시:

`echo '{{파이프로 전달된 메시지 데이터!}}' | terminal-notifier -sound {{default}}`

- 알림을 클릭하면 URL 열기:

`terminal-notifier -message '{{Apple 주식을 확인하세요!}}' -open '{{http://finance.yahoo.com/q?s=AAPL}}'`

- 알림을 클릭하면 앱 열기:

`terminal-notifier -message '{{42개의 연락처를 가져왔습니다.}}' -activate {{com.apple.AddressBook}}`
