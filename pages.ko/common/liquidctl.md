# liquidctl

> 수냉 쿨러 제어.
> 더 많은 정보: <https://github.com/liquidctl/liquidctl>.

- 사용 가능한 장치 나열:

`liquidctl list`

- 지원되는 모든 장치 초기화:

`sudo liquidctl initialize all`

- 사용 가능한 수냉 쿨러의 상태 출력:

`liquidctl status`

- 제품 이름에서 문자열을 일치시켜 장치를 선택하고 팬 속도를 20°C에서 0%, 50°C에서 50%, 70°C에서 100%로 설정:

`liquidctl --match {{문자열}} set fan speed {{20 0 50 50 70 100}}`
