### インポート
import datetime
import calendar
import tkinter

### 定数
WEEK = ["日", "月", "火", "水", "木", "金", "土"]

### 現在年月取得
year  = datetime.date.today().year
month = datetime.date.today().month


### 関数(カレンダー表示)
def func1(arg):

    ### グローバル変数定義
    global year
    global month

    ### 月を変更
    month += arg

    ### 表示年月を計算
    year,month = func2(year, month)

    ### ラベルウィジェットを初期化
    for widget in frame1.winfo_children():
        if isinstance(widget, tkinter.Label):
            widget.destroy()

    ### ラベルに年月を設定
    label = tkinter.Label(master=frame1, text=str(year) + "年" + str(month) + "月",  font=("游ゴシック",20))

    ### 年月表示
    label.pack()

    ### カレンダーオブジェクト作成
    cl = calendar.Calendar(firstweekday=6)

    ### 該当年月のカレンダーを取得
    cal = cl.monthdayscalendar(year, month)

    ### ウィジェット初期化
    for widget in frame2.winfo_children():
        widget.destroy()

    ### 曜日配列を取得
    for i,x in enumerate(WEEK):

        ### 日曜日は赤、土曜日は青にする
        if   i == 0:
            label_day = tkinter.Label(master=frame2, text=x, font=("游ゴシック",18), width=3, fg="red")
        elif i == 6:
            label_day = tkinter.Label(master=frame2, text=x, font=("游ゴシック",18), width=3, fg="blue")
        else:
            label_day = tkinter.Label(master=frame2, text=x, font=("游ゴシック",18), width=3)

        ### 曜日を表示
        label_day.grid(row=0, column=i, pady=2)

    ### 前月を計算
    year_pre,month_pre = func2(year, month-1)

    ### 前月のカレンダーを取得
    cal_pre = cl.monthdayscalendar(year_pre, month_pre)

    ### 前月の最終週を取得
    week_pre = cal_pre[-1]

    ### 翌月を計算
    year_aft,month_aft = func2(year, month+1)

    ### 翌月のカレンダーを取得
    cal_aft = cl.monthdayscalendar(year_aft, month_aft)

    ### 翌月の初週と2週目を取得
    week_aft1 = cal_aft[0]
    week_aft2 = cal_aft[1]

    ### 行カウンター
    row_cnt = 1

    ### カレンダー配列を取得
    for i,week in enumerate(cal):
        for j,day in enumerate(week):

            ### 日曜日は赤、土曜日は青にする
            if   j == 0:
                color = "red"
            elif j == 6:
                color = "blue"
            else:
                color = "black"

            ### 0だったら前月または翌月を設定
            if day == 0 and i == 0:
                day = week_pre[j]
                color = "gray"
            elif day == 0 and (i >= 4):
                day = week_aft1[j]
                color = "gray"

            ### 日にちを整形
            label_day = tkinter.Label(master=frame2, text="{:>2}".format(day), font=("游ゴシック",18), height=1, fg=color)

            ### 日にちを表示
            label_day.grid(row=row_cnt, column=j, padx=2, pady=2)

        ### カウントアップ
        row_cnt = row_cnt + 1

    ### 週が4行(2月1日が日曜日で閏年ではない場合)
    if len(cal) == 4:

        ### 5行目の色を灰色にして表示
        for i,day in enumerate(week_aft1):
            label_day = tkinter.Label(master=frame2, text="{:>2}".format(day), font=("游ゴシック", 18), height=1, fg="gray")
            label_day.grid(row=5, column=i, padx=2, pady=2)

        ### 6行目の色を灰色にして表示
        for i,day in enumerate(week_aft2):
            label_day = tkinter.Label(master=frame2, text="{:>2}".format(day), font=("游ゴシック", 18), height=1, fg="gray")
            label_day.grid(row=6, column=i, padx=2, pady=2)

    ### 週が5行
    elif len(cal) == 5:

        ### 最終行を設定
        if cal[-1][6] != 0:
            week_spc = week_aft1
        else:
            week_spc = week_aft2

        ### 6行目の色を灰色にして表示
        for i,day in enumerate(week_spc):
            label_day = tkinter.Label(master=frame2, text="{:>2}".format(day), font=("游ゴシック", 18), height=1, fg="gray")
            label_day.grid(row=6, column=i, padx=2, pady=2)

### 関数(年月調整)
def func2(l_year, l_month):

    ### 月が1未満の場合は前年にする
    if   l_month < 1:
        l_month = 12
        l_year -= 1

    ### 月が12より大きい場合は翌年にする
    elif l_month > 12:
        l_month = 1
        l_year += 1

    ### 年と月を返す
    return l_year,l_month

### メイン画面作成
main = tkinter.Tk()

### 画面サイズ設定
main.geometry("400x400")
main.colormapwindows="#141414"

### フレーム設定
frame1 = tkinter.Frame(master=main)
frame2 = tkinter.Frame(master=main)

### フレーム表示
frame1.pack(pady=20, side="top")
frame2.pack()

### ボタン作成
button1 = tkinter.Button(master=frame1, text="<", font=(None,12), command=lambda:func1(-1))
button2 = tkinter.Button(master=frame1, text=">", font=(None,12), command=lambda:func1(1))

### ボタン表示
button1.pack(side="left")
button2.pack(side="right")

### カレンダー表示
func1(0)

### イベントループ
main.mainloop()
