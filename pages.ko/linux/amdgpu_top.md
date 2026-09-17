# amdgpu_top

> AMDGPU 드라이버를 사용하여 AMD GPU 사용률과 하드웨어 지표를 표시하는 도구.
> 관련 항목: `nvtop`, `radeontop`.
> 더 많은 정보: <https://github.com/Umio-Yasuno/amdgpu_top#usage>.

- AMDGPU 장치 목록 출력:

`amdgpu_top --list`

- 모든 GPU 프로세스 및 프로세스 별 메모리 사용량 출력:

`amdgpu_top {{[-p|--process]}}`

- PCI 버스로 특정 GPU 선택:

`amdgpu_top --pci "{{0000:01:00.0}}"`

- 대화형 TUI 모니터 실행:

`amdgpu_top`

- GUI 모니터 실행:

`amdgpu_top --gui`

- 간단한 SMI 스타일 TUI 뷰 실행:

`amdgpu_top --smi`
