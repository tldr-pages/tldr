# ps

> 실행 중인 프로세스에 대한 정보.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/ps.1.html>.

- 모든 실행 중인 프로세스 나열:

`ps aux`

- 전체 명령어 문자열을 포함하여 모든 실행 중인 프로세스 나열:

`ps auxww`

- 문자열과 일치하는 프로세스 검색:

`ps aux | grep {{문자열}}`

- 프로세스의 부모 PID 가져오기:

`ps -o ppid= -p {{PID}}`

- 메모리 사용량으로 프로세스 정렬:

`ps -m`

- CPU 사용량으로 프로세스 정렬:

`ps -r`
