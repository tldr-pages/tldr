# waitpid

> انتظار برای پایان فرایندهای دلخواه.
> همچنین ببینید: `wait`.
> اطلاعات بیشتر: <https://manned.org/waitpid>.

- خوابیدن تا پایان همهٔ فرایندهای دارای PID مشخص:

`waitpid {{process_id1 process_id2 ...}}`

- خوابیدن برای حداکثر `n` ثانیه:

`waitpid {{[-t|--timeout]}} {{n}} {{process_id1 process_id2 ...}}`

- خطا ندادن اگر PIDهای مشخص از قبل پایان یافته‌اند:

`waitpid {{[-e|--exited]}} {{process_id1 process_id2 ...}}`

- خوابیدن تا پایان `n` فرایند از فرایندهای مشخص:

`waitpid {{[-c|--count]}} {{n}} {{process_id1 process_id2 ...}}`

- نمایش راهنما:

`waitpid {{[-h|--help]}}`
