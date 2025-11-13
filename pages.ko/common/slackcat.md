# slackcat

> 파일 및 명령 출력을 Slack에 전달하는 도구.
> 더 많은 정보: <https://github.com/bcicen/slackcat#usage>.

- 파일을 Slack에 게시:

`slackcat --channel {{채널_이름}} {{경로/대상/파일}}`

- 사용자 지정 파일 이름으로 파일을 Slack에 게시:

`slackcat --channel {{채널_이름}} --filename={{파일_이름}} {{경로/대상/파일}}`

- 명령 출력을 텍스트 스니펫으로 Slack에 파이프:

`{{명령어}} | slackcat --channel {{채널_이름}} --filename={{스니펫_이름}}`

- 명령 출력을 Slack에 지속적으로 스트리밍:

`{{명령어}} | slackcat --channel {{채널_이름}} --stream`
