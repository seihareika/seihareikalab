import tkinter as tk
from tkinter import messagebox


class Timer:
    def __init__(self, master):
        self.master = master
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.timer_running = False


        self.timer_frame = tk.Frame(master)
        self.timer_frame.pack()


        self.hours_label = tk.Label(self.timer_frame, text="00", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.hours_label.pack(side=tk.LEFT)


        self.separator1_label = tk.Label(self.timer_frame, text=":", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.separator1_label.pack(side=tk.LEFT)


        self.minutes_label = tk.Label(self.timer_frame, text="00", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.minutes_label.pack(side=tk.LEFT)


        self.separator2_label = tk.Label(self.timer_frame, text=":", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.separator2_label.pack(side=tk.LEFT)


        self.seconds_label = tk.Label(self.timer_frame, text="00", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.seconds_label.pack(side=tk.LEFT)


        self.separator3_label = tk.Label(self.timer_frame, text=".", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.separator3_label.pack(side=tk.LEFT)


        self.milliseconds_label = tk.Label(self.timer_frame, text="00", font=("Helvetica", 72),bg="#141414",foreground="#13FF13")
        self.milliseconds_label.pack(side=tk.LEFT)


        self.button_frame = tk.Frame(master)
        self.button_frame.pack()


        self.hours_button = tk.Button(self.button_frame, text="時", command=self.increment_hours, font=("Helvetica", 24),bg="#141414",foreground="#13FF13")
        self.hours_button.pack(side=tk.LEFT)


        self.minutes_button = tk.Button(self.button_frame, text="分", command=self.increment_minutes, font=("Helvetica", 24),bg="#141414",foreground="#13FF13")
        self.minutes_button.pack(side=tk.LEFT)


        self.seconds_button = tk.Button(self.button_frame, text="秒", command=self.increment_seconds, font=("Helvetica", 24),bg="#141414",foreground="#13FF13")
        self.seconds_button.pack(side=tk.LEFT)


        self.reset_button = tk.Button(self.button_frame, text="リセット", command=self.reset_timer, font=("Helvetica", 24),bg="#141414",foreground="#13FF13")
        self.reset_button.pack(side=tk.LEFT)


        self.start_stop_button = tk.Button(self.button_frame, text="スタート", command=self.start_stop_timer, font=("Helvetica", 24),bg="#141414",foreground="#13FF13")
        self.start_stop_button.pack(side=tk.LEFT)


    def increment_hours(self):
        if not self.timer_running:
            self.hours += 1
            self.update_labels()


    def increment_minutes(self):
        if not self.timer_running:
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
            self.update_labels()


    def increment_seconds(self):
        if not self.timer_running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            self.update_labels()


    def reset_timer(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.update_labels()


    def update_labels(self):
        self.hours_label.config(text=str(self.hours).zfill(2))
        self.minutes_label.config(text=str(self.minutes).zfill(2))
        self.seconds_label.config(text=str(self.seconds).zfill(2))
        self.milliseconds_label.config(text=str(self.milliseconds).zfill(2))


    def start_stop_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_stop_button.config(text="ストップ")
            self.countdown()
        else:
            self.timer_running = False
            self.start_stop_button.config(text="スタート")


    def countdown(self):
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0 and self.milliseconds == 0:
            messagebox.showinfo("タイマー終了", "タイマーが終了しました！")
            self.timer_running = False
            self.start_stop_button.config(text="スタート")
            return


        if self.milliseconds == 0:
            self.milliseconds = 99
            if self.seconds == 0:
                self.seconds = 59
                if self.minutes == 0:
                    self.minutes = 59
                    self.hours -= 1
                else:
                    self.minutes -= 1
            else:
                self.seconds -= 1
        else:
            self.milliseconds -= 1


        self.update_labels()


        if self.timer_running:
            self.master.after(10, self.countdown)


app = tk.Tk()
app.geometry("600x200")
app.title("Timer")
app.configure(bg="#141414")
timer = Timer(app)
app.mainloop()
