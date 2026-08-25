# gst-launch-1.0 queue

> 파이프라인을 멀티스레드화하고 데이터를 버퍼링.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/coreelements/queue.html>.

- 하나의 블로킹 요소가 전체 파이프라인을 막지 않도록, 여러 스레드로 분리:

`gst-launch-1.0 {{소스}} ! queue ! {{출력}}`
