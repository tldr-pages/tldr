# grub-file

> 파일이 부팅 가능한 이미지 유형인지 확인.
> 더 많은 정보: <https://manned.org/grub-file>.

- 파일이 ARM EFI 이미지인지 확인:

`grub-file --is-arm-efi {{경로/대상/파일}}`

- 파일이 i386 EFI 이미지인지 확인:

`grub-file --is-i386-efi {{경로/대상/파일}}`

- 파일이 x86_64 EFI 이미지인지 확인:

`grub-file --is-x86_64-efi {{경로/대상/파일}}`

- 파일이 ARM 이미지(Linux 커널)인지 확인:

`grub-file --is-arm-linux {{경로/대상/파일}}`

- 파일이 x86 이미지(Linux 커널)인지 확인:

`grub-file --is-x86-linux {{경로/대상/파일}}`

- 파일이 x86_64 XNU 이미지(macOS 커널)인지 확인:

`grub-file --is-x86_64-xnu {{경로/대상/파일}}`
