import time 
from plyer import notification

if __name__ == "__main__":
    
    notification.notify(
        title = "HEADING HERE",
        message = "DESCRIPTION HERE",
        
        timeout = 2
)
    
    time.sleep(7)
