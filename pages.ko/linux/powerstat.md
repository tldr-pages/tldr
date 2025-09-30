# powerstat

> 배터리 전원 소스를 사용하거나 RAPL 인터페이스를 지원하는 컴퓨터의 전력 소비를 측정합니다.
> 더 많은 정보: <https://manned.org/powerstat>.

- 10초 간격으로 10번 샘플링하여 전력 측정:

`powerstat`

- 사용자 지정 간격과 샘플 수로 전력 측정:

`powerstat {{간격}} {{샘플_수}}`

- Intel의 RAPL 인터페이스를 사용하여 전력 측정:

`powerstat -R {{간격}} {{샘플_수}}`

- 전력 측정의 히스토그램 표시:

`powerstat -H {{간격}} {{샘플_수}}`

- 모든 통계 수집 옵션 활성화:

`powerstat -a {{간격}} {{샘플_수}}`
