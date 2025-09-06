# systemd-detect-virt

> 가상화된 환경에서 실행 여부를 감지.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html>.

- 감지 가능한 가상화 기술 목록 표시:

`systemd-detect-virt --list`

- 가상화 여부를 감지하고 결과를 출력하며, VM이나 컨테이너에서 실행 중이면 0 상태 코드를 반환하고, 그렇지 않으면 0이 아닌 코드를 반환:

`systemd-detect-virt`

- 아무것도 출력하지 않고 조용히 확인:

`systemd-detect-virt --quiet`

- 컨테이너 가상화만 감지:

`systemd-detect-virt --container`

- 하드웨어 가상화만 감지:

`systemd-detect-virt --vm`
