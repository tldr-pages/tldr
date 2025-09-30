# pammixinterlace

> 이미지의 각 행을 인접한 두 행과 병합.
> 같이 보기: `pamdeinterlace`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>.

- 이미지의 각 행을 인접한 두 행과 병합:

`pammixinterlace {{경로/대상/이미지.ppm}} > {{경로/대상/출력.ppm}}`

- 지정된 필터링 메커니즘 사용:

`pammixinterlace {{[-f|-filter]}} {{linear|fir|ffmpeg}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력.ppm}}`

- 적응형 필터링 모드 활성화, 즉 명백히 빗살무늬 패턴의 일부인 픽셀만 수정:

`pammixinterlace {{[-a|-adaptive]}} {{경로/대상/이미지.ppm}} > {{경로/대상/출력.ppm}}`
