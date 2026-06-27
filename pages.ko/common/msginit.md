# msginit

> Portable Object Template 파일을 기반으로 언어별 번역 파일 생성.
> 더 많은 정보: <https://www.gnu.org/software/gettext/manual/gettext.html#msginit-Invocation>.

- 시스템 로케일을 사용하여 `messages.pot` 로부터 Portable Object 파일 생성:

`msginit`

- 특정 로케일에 대한 번역 파일을 특정 템플릿으로부터 생성:

`msginit {{[-l|--locale]}} {{로케일}} {{[-i|--input]}} {{경로/대상/메시지.pot}}`

- 도움말 표시:

`msginit {{[-h|--help]}}`
