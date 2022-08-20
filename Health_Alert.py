from plyer import notification
from time import sleep
filelist = ['static/health_icon.ico', 'static/health_icon2.ico', 'static/health_icon3.ico']

while True:
    for item in filelist:
        notification.notify(app_icon=item,
                            title="alert!",
                            message="watch tv",
                            app_name="health",
                            timeout=5,
                            )
        sleep(6)