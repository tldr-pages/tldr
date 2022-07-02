# qsub

> Submits a script to the queue management system TORQUE.
> More information: <https://manned.org/qsub.1>.

- Submit a script with default settings (depends on TORQUE settings):

`qsub {{script.sh}}`

- Submit a script with a specified wallclock runtime limit of 1 hour, 2 minutes and 3 seconds:

`qsub -l walltime={{1}}:{{2}}:{{3}} {{script.sh}}`

- Submit a script that is executed on 2 nodes using 4 cores per node:

`qsub -l nodes={{2}}:ppn={{4}} {{script.sh}}`

- Submit a script to a specific queue. Note that different queues can have different maximum and minimum runtime limits:

`qsub -q {{queue_name}} {{script.sh}}`
