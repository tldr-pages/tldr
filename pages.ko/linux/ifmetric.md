# ifmetric

> IPv4 경로 메트릭 조정 도구.
> 더 많은 정보: <https://0pointer.de/lennart/projects/ifmetric/>.

- 특정 네트워크 인터페이스의 우선순위 설정 (높은 숫자는 낮은 우선순위를 나타냄):

`sudo ifmetric {{인터페이스}} {{값}}`

- 특정 네트워크 인터페이스의 우선순위 초기화:

`sudo ifmetric {{인터페이스}} {{0}}`
