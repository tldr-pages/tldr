# ctrlaltdel

> CTRL+ALT+DEL 키 조합을 눌렀을 때의 동작을 제어하는 도구.
> 더 많은 정보: <https://manned.org/ctrlaltdel>.

- 현재 설정 확인:

`ctrlaltdel`

- CTRL+ALT+DEL을 즉시 재부팅하도록 설정 (준비 없이):

`sudo ctrlaltdel hard`

- CTRL+ALT+DEL을 "일반적으로" 재부팅하도록 설정, 프로세스 종료 기회를 제공 (PID1에 SIGINT 전송):

`sudo ctrlaltdel soft`
