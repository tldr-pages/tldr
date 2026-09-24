# cpulimit

> 다른 프로세스의 CPU 사용을 제한하는 도구.
> 더 많은 정보: <https://manned.org/cpulimit>.

- PID 1234인 기존 프로세스의 CPU 사용을 25%로 제한:

`cpulimit {{[-p|--pid]}} {{1234}} {{[-l|--limit]}} {{25%}}`

- 실행 파일 이름으로 기존 프로그램의 CPU 사용 제한:

`cpulimit {{[-e|--exe]}} {{프로그램}} {{[-l|--limit]}} {{25}}`

- 주어진 프로그램을 실행하고 CPU 사용을 50%로 제한:

`cpulimit {{[-l|--limit]}} {{50}} -- {{프로그램 인수1 인수2 ...}}`

- 프로그램을 실행하고 CPU 사용을 50%로 제한하며 cpulimit을 백그라운드에서 실행:

`cpulimit {{[-l|--limit]}} {{50}} {{[-b|--background]}} -- {{프로그램}}`

- 프로그램의 CPU 사용이 50%를 초과하면 프로세스 종료:

`cpulimit {{[-l|--limit]}} 50 {{[-k|--kill]}} -- {{프로그램}}`

- 프로그램과 자식 프로세스의 CPU 사용을 각각 25%로 제한:

`cpulimit {{[-l|--limit]}} {{25}} {{[-m|--monitor-forks]}} -- {{프로그램}}`
