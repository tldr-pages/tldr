# arthas-trace

> 메서드 호출 체인을 추적하고, 경로상의 각 노드에 대한 소요 시간을 출력.
> 관련 항목: `arthas`, `arthas-watch`.
> 더 많은 정보: <https://arthas.aliyun.com/en/doc/trace.html>.

- 메서드 호출 체인을 추적:

`trace {{class-pattern}} {{method-pattern}}`

- 메서드 호출 체인을 추적하고, 호출 시간이 10ms보다 긴 경우만 표시:

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}'`

- 여러 클래스 또는 여러 메서드의 호출 체인을 추적:

`trace -E {{class-pattern1}}|{{class-patter2}} {{method-pattern1}}|{{method-pattern2}}|{{method-pattern3}}`

- 메서드 호출 체인을 추적하고, 호출 시간이 10ms를 초과하는 경우만 표시하며, 5회 추적 후 중료:

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}' -n 5`
