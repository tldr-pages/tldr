# git credential-cache

> Git 비밀번호를 메모리에 임시로 저장하는 도구.
> 더 많은 정보: <https://git-scm.com/docs/git-credential-cache>.

- Git 자격 증명을 특정 시간 동안 저장:

`git config credential.helper 'cache --timeout={{초단위_시간}}'`
