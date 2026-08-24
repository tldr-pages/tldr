# gst-launch-1.0 capsfilter

> 파이프라인 capability 필터링.
> 더 많은 정보: <https://gstreamer.freedesktop.org/documentation/coreelements/capsfilter.html>.

- 그레이스케일 형식만 허용하도록 필터링:

`gst-launch-1.0 {{테스트용_비디오_소스}} ! capsfilter caps=video/x-raw,format=GRAY8 ! {{videoconvert ! autovideosink}}`

- 위와 동일한 작업을 축약 문법으로 수행:

`gst-launch-1.0 {{테스트용_비디오_소스}} ! video/x-raw,format=GRAY8 ! {{videoconvert ! autovideosink}}`

- 비디오 capability를 특정 해상도로 제한:

`gst-launch-1.0 {{테스트용_비디오_소스}} ! video/x-raw,width={{640}},height={{480}} ! {{videoconvert ! autovideosink}}`

- 특정 프레임레이트 지정:

`gst-launch-1.0 {{테스트용_비디오_소스}} ! video/x-raw,framerate={{30}}/1 ! {{videoconvert ! autovideosink}}`
