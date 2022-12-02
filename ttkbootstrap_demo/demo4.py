import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

app = ttk.Window()

toast = ToastNotification(
    title="ttkbootstrap toast message",
    message="This is a toast message",
    duration=3000,
)
toast.show_toast()

app.mainloop()