from plyer import notification
from time import sleep
filelist = ['static/health_icon.ico', 'static/health_icon2.ico', 'static/health_icon3.ico']

while True:
    for item in filelist:
        notification.notify(app_icon=item,
                            title="alert!",
                            message="this means it's been a while that you were using computer take a break and then come back",
                            app_name="health",
                            timeout=15,
                            )
        sleep(5400)
