# btm

> `top`에 대한 대안.
> `top`보다 가볍고 크로스 플랫폼이며 그래픽이 더 많이 존재하는 것을 목표로 함.
> 더 많은 정보: <https://clementtsang.github.io/bottom/nightly/#usage-and-configuration>.

- 기본 레이아웃 표시 (CPU, 메모리, 온도, 디스크, 네트워크 및 프로세스):

`btm`

- 기본 모드를 활성화하여, 차트를 제거하고 데이터를 압축 (`top`과 유사):

`btm --basic`

- 차트에 작은 점 대신 큰 점을 사용:

`btm --dot_marker`

- 배터리 충전 및 상태도 표시:

`btm --battery`

- 250 밀리초마다 새로 고치고 차트에 마지막 30초를 표시:

`btm --rate 250 --default_time_value 30000`
