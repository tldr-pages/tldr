# print

> Z Shell (`zsh`) 내장 명령. `echo`와 유사하게 인수를 출력.
> 관련 항목: `echo`, `printf`, `zsh`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- 입력 내용 출력:

`print "Hello" "World"`

- 각 인수를 줄바꿈하여 출력ㄴ:

`print -l "Line1" "Line 2" "Line3"`

- 마지막에 줄바꿈 없이 출력:

`print -n "Hello"; print "World"`

- 백슬래스 이스케이프 문자 사용:

`print -e "Line 1\nLine2"`

- `printf` 형식으로 인수 출력 (쉘 간 호환성을 위해선, `printf` 명령 사용을 권장):

`print -f "%s is %d years old.\n" "Alice" 30`
