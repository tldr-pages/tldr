# zmv

> 지정된 확장 글로브 패턴과 일치하는 파일을 이동하거나 이름 변경.
> 같이 보기: `zcp` 및 `zln`.
> 더 많은 정보: <https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- 정규 표현식과 유사한 패턴을 사용하여 파일 이동:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- 이동 결과를 미리 보기(실제 변경 없음):

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- 각 변경 전에 확인을 요청하면서 파일을 대화식으로 이동:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- 실행 중인 각 작업을 자세히 출력:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`
