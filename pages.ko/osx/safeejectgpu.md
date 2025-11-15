# SafeEjectGPU

> GPU를 안전하게 제거합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

- 모든 GPU 제거:

`SafeEjectGPU Eject`

- 연결된 모든 GPU 나열:

`SafeEjectGPU gpus`

- GPU를 사용하는 앱 나열:

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- GPU의 상태 확인:

`SafeEjectGPU gpuid {{GPU_ID}} status`

- GPU 제거:

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- GPU에서 앱 실행:

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{경로/대상/App.app}}`
