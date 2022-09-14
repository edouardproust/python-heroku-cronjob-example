# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# The cronjob function
from script import writedate

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(writedate, "cron", minute="0/1")

scheduler.start()
