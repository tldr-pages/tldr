# gnomon

> 타임스탬프로 콘솔 로깅 문에 주석을 달고, 느린 프로세스를 찾는 유틸리티.
> 더 많은 정보: <https://github.com/paypal/gnomon>.

- UNIX (또는 DOS) 파이프를 사용하여 gnomon을 통해 명령의 `stdout`을 파이프:

`{{npm test}} | gnomon`

- 프로세스 시작 이후 경과한 시간(초)를 표시:

`{{npm test}} | gnomon --type=elapsed-total`

- UTC로 절대 타임스탬프를 표시:

`{{npm test}} | gnomon --type=absolute`

- 0.5초의 높은 임계값을 사용, 이 값을 초과하면 타임스탬프가 밝은 빨간색으로 표시됨:

`{{npm test}} | gnomon --high 0.5`

- 0.2초의 중간 임계값을 사용, 이를 초과하면 타임스탬프가 밝은 노란색으로 표시됨:

`{{npm test}} | gnomon --medium {{0.2}}`
