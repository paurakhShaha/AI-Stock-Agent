from apscheduler.schedulers.blocking import BlockingScheduler

from weekly_runner import run_daily



scheduler = BlockingScheduler()


@scheduler.scheduled_job(
    "cron",
    hour=8,
    minute=0
)
def daily_job():
    run_daily()



scheduler.start()