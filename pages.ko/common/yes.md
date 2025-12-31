# yes

> 무언가를 반복적으로 출력.
> 이 명령은 일반적으로 설치 명령(예: `apt-get`)의 모든 프롬프트에 'yes'로 응답하기 위해 사용됩니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- "메시지"를 반복적으로 출력:

`yes {{메시지}}`

- "y"를 반복적으로 출력:

`yes`

- `apt-get` 명령의 모든 프롬프트에 수락:

`yes | sudo apt-get install {{프로그램}}`

- 항상 프롬프트의 기본 옵션을 수락하도록 줄바꿈을 반복적으로 출력:

`yes ''`
