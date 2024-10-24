# dcode

> 16진수, 10진수, 2진수, base64, URL, FromChar 인코딩, 카이사르 암호, MD5, SHA1 및 SHA2 해시를 지원하여 문자열을 반복적으로 감지하고 디코딩.
> 경고: MD5, SHA1 및 SHA2 해시 조회를 위해 타사 웹 서비스를 사용. 민감한 데이터의 경우, `-s` 옵션을 사용하여 이러한 서비스 사용을 피해야 합니다.
> 더 많은 정보: <https://github.com/s0md3v/Decodify>.

- 문자열을 재귀적으로 감지하고 디코딩:

`dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"`

- 지정된 오프셋만큼 문자열을 회전:

`dcode -rot {{11}} "{{spwwz hzcwo}}"`

- 가능한 26가지 오프셋을 모두 사용하여 문자열을 회전:

`dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"`

- 문자열 뒤집기:

`dcode -rev "{{hello world}}"`
