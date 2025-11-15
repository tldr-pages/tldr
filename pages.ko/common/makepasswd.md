# makepasswd

> 비밀번호 생성 및 암호화.
> 더 많은 정보: <https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>.

- 무작위 비밀번호 생성 (8~10자, 문자 및 숫자 포함):

`makepasswd`

- 10자 길이의 비밀번호 생성:

`makepasswd --chars {{10}}`

- 5~10자 길이의 비밀번호 생성:

`makepasswd --minchars {{5}} --maxchars {{10}}`

- "b", "a", "r" 문자만 포함하는 비밀번호 생성:

`makepasswd --string {{bar}}`
