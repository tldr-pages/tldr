# taskset

> دریافت یا تنظیم وابستگی CPU فرایند یا شروع فرایند جدید با وابستگی CPU مشخص.
> اطلاعات بیشتر: <https://manned.org/taskset>.

- دریافت وابستگی CPU فرایند در حال اجرا با PID:

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{process_id}}`

- تنظیم وابستگی CPU فرایند در حال اجرا با PID:

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{cpu_id}} {{process_id}}`

- شروع فرایند جدید با وابستگی به یک CPU:

`taskset {{[-c|--cpu-list]}} {{cpu_id}} {{command}}`

- شروع فرایند جدید با وابستگی به چند CPU غیرمتوالی:

`taskset {{[-c|--cpu-list]}} {{cpu_id_1,cpu_id_2,cpu_id_3,...}} {{command}}`

- شروع فرایند جدید با وابستگی به CPUهای ۱ تا ۴:

`taskset {{[-c|--cpu-list]}} {{cpu_id_1}}-{{cpu_id_4}} {{command}}`
