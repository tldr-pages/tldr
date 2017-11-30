# qsub

> Submits a script to the queue management system TORQUE.

- Submit a script with default settings (depends on TORQUE settings):

`qsub script.sh`

- Submit a script with a specified wallclock runtime limit of 1h 2m 3s:

`qsub -l walltime=01:02:03 script.sh`

- Submit a script that is executed on 2 nodes using 16 cores per node:

`qsub -l nodes=2:ppn=16 script.sh`

- Submit a script with a specified wallclock runtime limit of 1h 2m 3s to a specific queue. Note that different queues can have different maximum and minimum runtime limits:

`qsub -q QUEUENAME -l walltime=01:02:03 script.sh`
