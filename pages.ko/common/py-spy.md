# py-spy

> Python 프로그램용 샘플링 프로파일러.
> 더 많은 정보: <https://github.com/benfred/py-spy>.

- 실행 중인 프로세스에서 가장 많은 실행 시간을 차지하는 함수의 실시간 보기 표시:

`py-spy top --pid {{pid}}`

- 프로그램을 시작하고 가장 많은 실행 시간을 차지하는 함수의 실시간 보기 표시:

`py-spy top -- python {{경로/대상/파일.py}}`

- 함수 호출 실행 시간의 SVG 플레임 그래프 생성:

`py-spy record -o {{경로/대상/프로필.svg}} --pid {{pid}}`

- 실행 중인 프로세스의 호출 스택 덤프:

`py-spy dump --pid {{pid}}`
