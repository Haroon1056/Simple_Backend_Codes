from plyer import notification

#Display a toast notification

notification.notify(
    title= "Simple notification",
    message= "This is a simple toast notification.",
    timeout= 10   #notification will stay for 10 seconds
)