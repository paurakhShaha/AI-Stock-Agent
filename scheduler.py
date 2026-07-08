from apscheduler.schedulers.blocking import BlockingScheduler

from weekly_runner import run_weekly



scheduler = BlockingScheduler()



@scheduler.scheduled_job(
    "cron",
    day_of_week="mon",
    hour=8
)
def weekly():

    run_weekly()



scheduler.start()