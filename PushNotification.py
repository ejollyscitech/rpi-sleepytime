import time

from winotify import Notification, audio

def fiveMinutesBefore(x):
    if (int(x[3:]) <= 4):
        five_before_str = str((int(x[3:]) + 60) - 5)

        if (int(x[:2]) == 00):
            new_time = ( "23" + x[2] + five_before_str)
        elif int(x[:2]) <= 10:
            new_time = ( "0" + str(int(x[:2]) - 1) + x[2] + five_before_str)
        else:
            new_time = (str(int(x[:2]) - 1) + x[2] + five_before_str)

    elif int(x[3:]) >= 15:
        new_time =  (x[0:3] + str(int(x[3:]) - 5))

    else:
        new_time =  (x[0:3] + "0" + str(int(x[3:]) - 5))

    return new_time

reminder_time = input("What time do you want to sleep? ") #time to shut off. Will probably add the ability to get user input in HH:MM
warning_time = fiveMinutesBefore(reminder_time)

print (reminder_time)
print (warning_time)


# 5 Minutes before shut down time
while True:
    current_time = time.strftime("%H:%M") #reads the time as HH:MM
    print ("-", current_time)
    print ("--", current_time)
    if (current_time == warning_time):
        countdownNotification = Notification(app_id = "PushNotification Script",
                                        title = "Shutdown Timer has been executed",
                                        msg = "Shut down will commence in 5 minutes",
                                        duration = "long"
                                        )
        countdownNotification.set_audio(audio.Reminder, loop = False)
        countdownNotification.add_actions(label = "Okay")
        countdownNotification.show()
        break

# Shut down time reached
while True:
    current_time = time.strftime("%H:%M") #reads the time as HH:MM
    print (current_time)
    if (current_time == reminder_time):
        timeNotification = Notification(app_id = "PushNotification Script",
                                        title = "Shutdown commencing",
                                        msg = "Configured sleep time is has been reached",
                                        duration = "long"
                                        )

        timeNotification.set_audio(audio.Reminder, loop = False)
        timeNotification.show()
        break

with open('C:\\Users\\vince\\OneDrive\\Desktop\\Shutdown.py', 'r') as f:
    code = f.read()
    exec(code)

