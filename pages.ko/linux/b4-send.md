# b4 send

> `b4 prep`으로 준비한 패치 시리즈를 메일링 리스트로 전송.
> 더 많은 정보: <https://b4.docs.kernel.org/en/latest/contributor/send.html>.

- 현재 `b4 prep` 관리 브랜치의 패치 전송:

`b4 send`

- 메일을 전송하지 않고 검토용 메시지 생성:

`b4 send {{[-o|--output-dir]}} {{경로/대상/디렉터리}}`

- 패치 시리즈 버전을 올리지 않고 지정한 수신자에게 미리보기용 패치 전송:

`b4 send --preview-to {{이메일_주소1 이메일_주소2 ...}}`

- 이전에 전송한 특정 버전의 패치 시리즈를 다시 전송:

`b4 send --resend {{버전_번호}}`

- 메일을 전송하지 않고 dry run 수행:

`b4 send {{[-d|--dry-run]}}`
