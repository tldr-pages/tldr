# base32

> 파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함.

- 파일 인코딩:

`base32 {{filename}}`

- 파일 디코딩:

`base32 -d {{filename}}`

- stdin에서 인코딩:

`{{somecommand}} | base32`

- stdin에서 디코딩:

`{{somecommand}} | base32 -d`

