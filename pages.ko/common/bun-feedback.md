# bun feedback

> Bun에 피드백을 전송.
> 더 많은 정보: <https://bun.com/docs/feedback#use-bun-feedback>.

- 텍스트 내용을 피드백으로 전송:

`bun feedback "{{피드백_내용}}"`

- 하나 이상의 파일을 피드백으로 전송:

`bun feedback {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 이메일 주소를 첨부하여 피드백을 전송:

`bun feedback {{경로/대상/파일|텍스트}} {{[-e|--email]}} {{이메일@주소}}`
