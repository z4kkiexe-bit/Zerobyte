import datetime
import schedule 
import time 
from plyer import notification



hari_ini = datetime.datetime.now()
minggu_ini = hari_ini.isocalendar().week
materi_1 = ["Ayo Zaki,ini Frontend Time!","Ayo Zaki,ini Backend Time!","Ayo Zaki,ini Database Time!", ]
data = 26
hasil = minggu_ini - data


def kirim_reminder():
    notification.notify(
        title="Waktunya belajar coding!",
        message=materi_1[hasil],
        timeout=3,
    )

for i in range(0, 6):
    time.sleep(1)
    kirim_reminder()
    print(i)
