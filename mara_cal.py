from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import List

# 재료 이미지 변경 함수
def makeImg(i):
    current_img = PhotoImage(file="img/" + str(i) + ".png")
    img_label.configure(image=current_img)
    img_label.image = current_img


# 리스트박스 클릭 이벤트핸들러
def lbClick(event):
    temp = lb.curselection()[0]
    makeImg(temp)


# 재료를 tree에 추가
def addIngredient():
    temp = lb.curselection()[0]
    name = ing_name[temp]
    kcal = ing.get(name)
    addKcal(kcal)
    ingExist(temp, name, kcal)


# 추가한 칼로리 더하기
def addKcal(kcal):
    global total_kcal
    total_kcal += kcal
    kcal_label.configure(text=("총 칼로리 : " + str(total_kcal)))


# 재료 추가 전 존재여부 체크
def ingExist(temp, name, kcal):
    if tree.exists(temp):
        amout_arr[temp] += 1
        tree.item(temp, values=(name, unitSelector(temp), amout_arr[temp] * kcal))
    else:
        tree.insert("", END, iid=temp, values=(name, unitSelector(temp), kcal))


# 재료 단위 결정
def unitSelector(temp):
    if temp in count_arr:
        return str(amout_arr[temp]) + " 개"
    else:
        return str(amout_arr[temp]) + "00g"


# 윈도우 생성
win = Tk()
win.title("마라탕 계산기")
win.geometry("1200x900")
win.resizable(False, False)

# 재료 DB 생성
ing = {
    "건두부": 252,
    "고기완자": 50,
    "국물": 500,
    "메추리알": 14,
    "배추": 12,
    "부죽": 459,
    "분모자": 344,
    "비엔나": 27,
    "새송이버섯": 18,
    "새우": 7,
    "소고기": 250,
    "숙주": 23,
    "양고기": 294,
    "옥수수면": 377,
    "유부": 22,
    "중국당면": 347,
    "청경채": 13,
    "치즈떡": 79,
    "팽이버섯": 22,
    "표고버섯": 16,
}
total_kcal = 0  # 총 칼로리의 합
count_arr = [1, 3, 7, 8, 9, 14, 17, 18, 19]  # 단위가 개수인 재료들
amout_arr = []  # 재료 양 저장하는 배열
ing_name = list(ing.keys())  # 재료 이름들의 리스트
init_img = PhotoImage(file="img/0.png")
for i in range(len(ing_name)):
    amout_arr.append(1)

# 재료 사진칸 생성
img_label = Label(
    win, image=init_img, borderwidth=1, relief="groove", background="white"
)
img_label.place(x=0, y=0, width=900, height=500)

# 재료 선택 안내창 생성
menu_font = ("Malgun Gothic", 12, "bold")
ing_text = Label(
    win,
    text="음식 선택",
    background="white",
    borderwidth=1,
    relief="groove",
    font=menu_font,
)
ing_text.place(x=900, y=0, width=300, height=30)

# 재료 선택창 생성
lb_font = ("Malgun Gothic", 16)
lb = Listbox(win, cursor="heart", font=lb_font)
for i in range(len(ing_name)):
    lb.insert(i, ing_name[i])
lb.select_set(0)
lb.place(x=900, y=30, width=300, height=440)
lb.bind("<ButtonRelease>", lbClick)

# 재료 추가 버튼 생성
ing_add = Button(win, text="추가", command=addIngredient, font=menu_font)
ing_add.place(x=900, y=470, width=300, height=30)

# 추가된 재료란 = 게시판
columns = ("1", "2", "3")
tree = ttk.Treeview(win, columns=columns, show="headings")
tree.column("1", width=600, stretch=NO, anchor=CENTER)
tree.column("2", width=300, stretch=NO, anchor=CENTER)
tree.column("3", width=300, stretch=NO, anchor=CENTER)

tree.heading(1, text="선택 재료", anchor=CENTER)
tree.heading(2, text="분량", anchor=CENTER)
tree.heading(3, text="칼로리", anchor=CENTER)
tree.place(x=0, y=500, width=1200, height=300)

# 총 칼로리
menu_font2 = ("Malgun Gothic", 20, "bold")
kcal_label = Label(
    win,
    text=("총 칼로리 : " + str(total_kcal)),
    background="white",
    borderwidth=1,
    relief="groove",
    font=menu_font2,
)
kcal_label.place(x=0, y=800, width=600, height=100)

# 운동 시간
exercise_label = Label(
    win,
    text="소모 시간 : ",
    background="white",
    borderwidth=1,
    relief="groove",
    font=menu_font2,
)
exercise_label.place(x=600, y=800, width=600, height=100)

# 실행
win.mainloop()
