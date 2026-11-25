# spa-resample

> نمونه‌برداری مجدد فایل صوتی با نمونه‌بردار PipeWire.
> توجه: این ابزار عمدتاً برای آزمون و اشکال‌زدایی نمونه‌بردار در نظر گرفته شده است.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_spa-resample_1.html>.

- نمونه‌برداری مجدد فایل صوتی:

`spa-resample {{path/to/input.wav}} {{path/to/output.wav}}`

- نمونه‌برداری مجدد فایل صوتی با نرخ نمونه‌برداری مشخص:

`spa-resample {{[-r|--rate]}} {{48000}} {{path/to/input.wav}} {{path/to/output.wav}}`

- نمونه‌برداری مجدد فایل صوتی با قالب مشخص:

`spa-resample {{[-f|--format]}} {{s8|s16|s32|f32|f64}} {{path/to/input.wav}} {{path/to/output.wav}}`

- نمونه‌برداری مجدد فایل صوتی با کیفیت مشخص (۰ کمترین و ۱۴ بیشترین):

`spa-resample {{[-q|--quality]}} {{0..14}} {{path/to/input.wav}} {{path/to/output.wav}}`

- نمایش راهنما:

`spa-resample -h`
