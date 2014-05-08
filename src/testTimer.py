# -*- coding: utf-8 -*-
'''
Created on 2014-4-2

@author: zqtang
'''
from datetime import datetime
from apscheduler.scheduler import Scheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


def sc2():
    print('2')

def info(sch = None):
    sch.print_jobs()

if __name__ == '__main__':
    scheduler = Scheduler(standalone=True)
#    scheduler2 = Scheduler(standalone=True)
    scheduler.add_interval_job(tick, seconds=3)
#    scheduler2.add_interval_job(sc2,seconds=1)
    scheduler.add_interval_job(sc2,seconds=1)
    scheduler.add_interval_job(info,args=[scheduler],seconds=2)
    print('Press Ctrl+C to exit')
    try:
#        out = ''
#        scheduler.print_jobs(out);
        scheduler.start()
#        scheduler2.start()
    except (KeyboardInterrupt, SystemExit):
        pass

