# kill

> Bir sürece, genellikle süreci durdurmakla ilgili bir sinyal gönder.
> `SIGKILL` ve `SIGSTOP` dışındaki tüm sinyaller, düzgün bir çıkış yapabilmesi için süreç tarafından yakalanabilir.
> Daha fazla bilgi için: <https://manned.org/kill.1posix>.

- Bir programı varsayılan `SIGTERM` (sonlandır) sinyaliyle sonlandır:

`kill {{süreç_kimliği}}`

- Kullanılabilir sinyal adlarını listele (`SIG` öneki olmadan kullanılır):

`kill -l`

- Bir programı `SIGHUP` (hat kapandı) sinyaliyle sonlandır. Birçok arka plan programı sonlanmak yerine yeniden yüklenir:

`kill {{[-1|-SIGHUP]}} {{süreç_kimliği}}`

- Bir programı `SIGINT` (kesme) sinyaliyle sonlandır. Bu sinyal genellikle kullanıcının `<Ctrl c>` tuşlarına basmasıyla gönderilir:

`kill {{[-2|-SIGINT]}} {{süreç_kimliği}}`

- İşletim sistemine bir programı hemen sonlandırması için sinyal gönder (program sinyali yakalama fırsatı bulamaz):

`kill {{[-9|-SIGKILL]}} {{süreç_kimliği}}`

- İşletim sistemine, bir `SIGCONT` ("devam et") sinyali alınana kadar programı duraklatması için sinyal gönder:

`kill {{[-19|-SIGSTOP]}} {{süreç_kimliği}}`

- Verilen GID'ye (grup kimliği) sahip tüm süreçlere bir `SIGUSR1` sinyali gönder:

`kill -SIGUSR1 -{{grup_kimliği}}`
