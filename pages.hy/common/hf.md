#հֆ

> Շփվել Hugging Face Hub-ի հետ:.
> Մուտք գործեք, կառավարեք տեղական քեշը, ներբեռնեք կամ վերբեռնեք ֆայլեր:.
> Լրացուցիչ տեղեկություններ. <https://huggingface.co/docs/huggingface_hub/guides/cli>:.

- Մուտք գործեք Hugging Face Hub:

`hf auth login`

- Ցուցադրել մուտք գործած օգտատիրոջ անունը.:

`hf auth whoami`

- Դուրս գալ.:

`hf auth logout`

- Տպել տեղեկատվություն շրջակա միջավայրի մասին.:

`hf env`

- Ներբեռնեք ֆայլերը պահոցից և տպեք ուղին (բաց թողեք ֆայլերի անունները՝ ամբողջ պահեստը ներբեռնելու համար).:

`hf download --repo-type {{repo_type}} {{repo_id}} {{filename1 filename2 ...}}`

- Վերբեռնեք մի ամբողջ թղթապանակ կամ ֆայլ Hugging Face:

`hf upload --repo-type {{repo_type}} {{repo_id}} {{path/to/local_file_or_directory}} {{path/to/repo_file_or_directory}}`

- Սկանավորեք քեշը՝ ներբեռնված պահոցները և դրանց սկավառակի օգտագործումը տեսնելու համար.:

`hf cache ls`
