# system_profiler

> Report system hardware and software configuration.

- Display a full system profiler report which can be opened by System Profiler.app:

`system_profiler -xml > MyReport.spx`

- Display a hardware overview (Model, CPU, Memory, Serial, etc):

`system_profiler SPHardwareDataType`

- Print the system serial number:

`system_profiler SPHardwareDataType|grep "Serial Number (system)" |awk '{print $4}'`
