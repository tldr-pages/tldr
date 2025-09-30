# kexec

> 새 커널로 직접 재부팅.
> 더 많은 정보: <https://manned.org/kexec>.

- 새 커널 로드:

`kexec -l {{경로/대상/커널}} --initrd={{경로/대상/initrd}} --command-line={{인자들}}`

- 현재 부팅 매개변수로 새 커널 로드:

`kexec -l {{경로/대상/커널}} --initrd={{경로/대상/initrd}} --reuse-cmdline`

- 현재 로드된 커널 실행:

`kexec -e`

- 현재 kexec 대상 커널 언로드:

`kexec -u`
