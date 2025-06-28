# luac

> Lua 바이트코드 컴파일러.
> 더 많은 정보: <https://www.lua.org/manual/5.4/luac.html>.

- Lua 소스 파일을 Lua 바이트코드로 컴파일:

`luac -o {{바이트_코드.luac}} {{소스.lua}}`

- 출력에 디버그 심볼을 포함하지 않음:

`luac -s -o {{바이트_코드.luac}} {{소스.lua}}`
