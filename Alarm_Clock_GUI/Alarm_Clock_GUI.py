from tkinter import *
import datetime
import time
import winsound
from threading import *


window = Tk()
window.title("Alarm Clock GUI")
window.geometry("800x600")
window.configure(bg = "red")


def threading():
    t1 = Thread(target = alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
            

L = Label(window, text = "Alarm Clock GUI", font = ("Courier", 30))
L.pack()        
L1 = Label(window, text = "When to wake you up", font = ("Courier", 30))
L1.pack()
L2 = Label(window, text = "Hour Min Sec", font = ("Courier", 30))
L2.pack()

frame = Frame(window)
frame.pack()

hour = StringVar(window)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side = LEFT)

minute = StringVar(window)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side = LEFT)



second = StringVar(window)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
           '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side = LEFT)

B = Button(window, text = "Set the alarm", font = ("Courier", 25), command = threading)
B.place(x = 300, y = 400)

window.mainloop()
