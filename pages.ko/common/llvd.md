# llvd

> Linkedin Learning 비디오 다운로드 도구.
> 더 많은 정보: <https://github.com/knowbee/llvd>.

- 쿠키 기반 인증을 사용하여 [c]ourse 다운로드:

`llvd {{[-c|--course]}} {{코스-슬러그}} --cookies`

- 특정 [r]esolution으로 코스 다운로드:

`llvd {{[-c|--course]}} {{코스-슬러그}} {{[-r|--resolution]}} 720`

- [ca]ptions(자막)과 함께 코스 다운로드:

`llvd {{[-c|--course]}} {{코스-슬러그}} {{[-ca|--caption]}}`

- [p]ath를 다운로드하고 10초에서 30초 사이 [t]hrottling 적용:

`llvd {{[-p|--path]}} {{경로-슬러그}} {{[-t|--throttle]}} {{10,30}} --cookies`
