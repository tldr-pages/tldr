# pw-cli

> مدیریت ماژول‌ها، اشیا، گره‌ها، دستگاه‌ها، پیوندها و موارد دیگر در یک نمونهٔ PipeWire.
> همچنین : `wpctl`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- چاپ اطلاعات همهٔ اشیای نوع مشخص:

`pw-cli {{[ls|list-objects]}} {{Node|Link|Port|Client|Device|Metadata|Factory|Module|Profiler|SecurityContext|Core}}`

- چاپ اطلاعات شیء با شناسهٔ مشخص:

`pw-cli {{[i|info]}} {{4}}`

- چاپ اطلاعات همهٔ اشیا:

`pw-cli {{[i|info]}} all`

- پایش تغییرات اشیا:

`pw-cli {{[-m|--monitor]}}`

- نمایش راهنما:

`pw-cli {{[h|help]}}`
