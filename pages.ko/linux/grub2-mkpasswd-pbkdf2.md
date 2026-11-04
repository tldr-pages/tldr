# grub2-mkpasswd-pbkdf2

> GRUB용 기반 비밀번호 해시를 생성.
> 더 많은 정보: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- PBKDF2를 사용하여 GRUB 2 비밀번호 해시를 생성하고 `stdout`으로 출력:

`sudo grub2-mkpasswd-pbkdf2 {{[-c|--iteration-count]}} {{pbkdf2_이터레이션_횟수}} {{[-s|--salt]}} {{솔트_길이}}`
