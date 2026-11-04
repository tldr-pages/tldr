# intercept

> 지정한 입력 이벤트 장치의 원시(raw) 입력 이벤트를 읽어 `stdout`으로 출력.
> 더 많은 정보: <https://gitlab.com/interception/linux/tools/-/tree/master#intercept>.

- 지정한 입력 장치 파일의 원시 입력 이벤트를 읽어 출력 (t시스템은 키 입력을 인식하지 못함):

`sudo intercept -g {{/dev/input/eventX}}`

- 지정한 입력 장치 파일의 원시 입력 이벤트를 읽어 출력 (시스템과 다른 프로그램도 키 입력을 인식할 수 있음):

`sudo intercept {{/dev/input/eventX}}`
