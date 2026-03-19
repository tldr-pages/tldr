# cowsay

> ASCII 아트 (기본값은 소)를 사용해 말하거나 생각하는 메시지를 출력.
> 더 많은 정보: <https://manned.org/cowsay>.

- ASCII 소가 "hello, world"라고 말하도록 출력:

`cowsay "{{hello, world}}"`

- `stdin`으로부터 입력받은 텍스트를 ASCII 소가 말하도록 출력:

`echo "{{hello, world}}" | cowsay`

- 사용 가능한 모든 아트 유형을 표시:

`cowsay -l`

- 지정한 ASCII 아트가 "hello, world"라고 말하도록 출력:

`cowsay -f {{아트}} "{{hello, world}}"`

- 생각하는(dead) 상태의 ASCII 소를 출력:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- 사용자 정의 눈 모양을 가진 ASCII 소가 "hello, world"라고 말하도록 출력:

`cowsay -e {{문자열}} "{{hello, world}}"`
