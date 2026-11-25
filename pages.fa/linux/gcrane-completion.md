# gcrane completion

> تولید اسکریپت تکمیل خودکار gcrane برای پوستهٔ مشخص.
> پوسته‌های موجود Bash، fish، PowerShell و Zsh هستند.
> اطلاعات بیشتر: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- تولید اسکریپت تکمیل خودکار برای پوسته:

`gcrane completion {{shell_name}}`

- غیرفعال کردن توضیحات تکمیل:

`gcrane completion {{shell_name}} --no-descriptions`

- بارگذاری تکمیل‌ها در نشست فعلی پوسته (Bash/Zsh):

`source <(gcrane completion bash/zsh)`

- بارگذاری تکمیل‌ها در نشست فعلی پوسته (fish):

`gcrane completion fish | source`

- بارگذاری تکمیل‌ها برای هر نشست جدید (Bash):

`gcrane completion bash >/etc/bash_completion.d/gcrane`

- بارگذاری تکمیل‌ها برای هر نشست جدید (Zsh):

`gcrane completion zsh >"${fpath[1]}/_gcrane"`

- بارگذاری تکمیل‌ها برای هر نشست جدید (fish):

`gcrane completion fish >~/.config/fish/completions/gcrane.fish`

- نمایش راهنما:

`gcrane completion {{shell_name}} {{[-h|--help]}}`
