from celery.task import task, periodic_task
from celery.schedules import crontab


import logging
logger = logging.getLogger(__name__)

@task
def do_something():
    print "Foo"
    logger.info('I am doing something')

MINUTE = "38"

@periodic_task(run_every=crontab(hour="0", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic0():
    logger.info('I am a periodic task running at every 0th hour')

@periodic_task(run_every=crontab(hour="1", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic1():
    logger.info('I am a periodic task running at every 1st hour')

@periodic_task(run_every=crontab(hour="2", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic2():
    logger.info('I am a periodic task running at every 2nd hour')

@periodic_task(run_every=crontab(hour="3", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic3():
    logger.info('I am a periodic task running at every 3rd hour')

@periodic_task(run_every=crontab(hour="4", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic4():
    logger.info('I am a periodic task running at every 4th hour')

@periodic_task(run_every=crontab(hour="5", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic5():
    logger.info('I am a periodic task running at every 5th hour')

@periodic_task(run_every=crontab(hour="6", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic6():
    logger.info('I am a periodic task running at every 6th hour')

@periodic_task(run_every=crontab(hour="7", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic7():
    logger.info('I am a periodic task running at every 7th hour')

@periodic_task(run_every=crontab(hour="8", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic8():
    logger.info('I am a periodic task running at every 8th hour')

@periodic_task(run_every=crontab(hour="9", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic9():
    logger.info('I am a periodic task running at every 9th hour')

@periodic_task(run_every=crontab(hour="10", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic10():
    logger.info('I am a periodic task running at every 10th hour')

@periodic_task(run_every=crontab(hour="11", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic11():
    logger.info('I am a periodic task running at every 11th hour')

@periodic_task(run_every=crontab(hour="12", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic12():
    logger.info('I am a periodic task running at every 12th hour')

@periodic_task(run_every=crontab(hour="13", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic13():
    logger.info('I am a periodic task running at every 13th hour')

@periodic_task(run_every=crontab(hour="14", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic14():
    logger.info('I am a periodic task running at every 14th hour')

@periodic_task(run_every=crontab(hour="15", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic15():
    logger.info('I am a periodic task running at every 15th hour')

@periodic_task(run_every=crontab(hour="16", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic16():
    logger.info('I am a periodic task running at every 16th hour')

@periodic_task(run_every=crontab(hour="17", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic17():
    logger.info('I am a periodic task running at every 17th hour')

@periodic_task(run_every=crontab(hour="18", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic18():
    logger.info('I am a periodic task running at every 18th hour')

@periodic_task(run_every=crontab(hour="19", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic19():
    logger.info('I am a periodic task running at every 19th hour')

@periodic_task(run_every=crontab(hour="20", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic20():
    logger.info('I am a periodic task running at every 20th hour')

@periodic_task(run_every=crontab(hour="21", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic21():
    logger.info('I am a periodic task running at every 21st hour')

@periodic_task(run_every=crontab(hour="22", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic22():
    logger.info('I am a periodic task running at every 22nd hour')

@periodic_task(run_every=crontab(hour="23", minute=MINUTE, day_of_week="*"),options={"expires": 60*60})
def do_periodic23():
    logger.info('I am a periodic task running at every 23rd hour')

@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"),options={"expires": 60*60})
def minute_tick():
    logger.info('Minute tick')