# Inference snap

> گفت‌وگو با مدل‌های زبانی هوش مصنوعی مولد که به‌صورت محلی و بدون اینترنت اجرا می‌شوند.
> در اینجا inference-snap یکی از مدل‌های پشتیبانی‌شده است: `deepseek-r1`، `gemma3`، `gemma4`، `nemotron3-nano`، `qwen-vl`.
> اطلاعات بیشتر: <https://documentation.ubuntu.com/inference-snaps/>.

- شروع گفت‌وگو در ترمینال (و یک سرور گفت‌وگو در پس‌زمینه در نخستین اجرا):

`{{inference-snap}} chat`

- نمایش موتور فعلی و وضعیت سرور گفت‌وگو:

`{{inference-snap}} status`

- انتخاب موتور مشخص (مثلاً `cuda` برای GPU شرکت NVIDIA)، بارگیری و استفاده از مدل مناسب آن:

`sudo {{inference-snap}} use-engine {{engine}}`

- نمایش اطلاعات مفصل سخت‌افزار دستگاه (RAM، معماری و غیره):

`sudo {{inference-snap}} show-machine`

- دریافت همهٔ تنظیمات (`http.host`، `http.port`) سرور گفت‌وگوی در حال اجرا:

`{{inference-snap}} get`
