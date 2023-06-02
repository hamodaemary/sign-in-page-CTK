import webbrowser
import customtkinter
#FUNCTIONS
def facebook():
    webbrowser.open('www.facebook.com')
def youtube():
    webbrowser.open('www.youtube.com')
def insta():
    webbrowser.open('www.instagram.com')
def twitter():
    webbrowser.open('www.twitter.com')
def cc():
 if ent.get() == 'admin':
    ccv = customtkinter.CTk()
    ccv.mainloop()

x = customtkinter.CTk()
x.title('sign in')
ljl = customtkinter.CTkLabel(x,text='Sign in',font=('Gill Sans MT',15),width=700,height=10,bg_color='#1565C0')
ljl.pack()
x.geometry('500x400')
lab = customtkinter.CTkLabel(x,text='Write The Password',font=('Gill Sans MT',15,'bold'))
lab.place(x=180,y=100)
ent = customtkinter.CTkEntry(x,border_width=2)
ent.place(x=180,y=150)
but = customtkinter.CTkButton(x,text='sign in',command=cc)
but.place(x=180,y=200)
fr = customtkinter.CTkFrame(x,width=140,height=300)
fr.place(x=360,y=80)
lkl = customtkinter.CTkLabel(fr,text='Social Media',font=('Gill Sans MT',12))
lkl.place(x=40,y=1)
but1 = customtkinter.CTkButton(fr,text='facebook',command=facebook)
but1.place(x=1,y=30)
but2 = customtkinter.CTkButton(fr,text='instagram',command=insta)
but2.place(x=1,y=60)
but3 = customtkinter.CTkButton(fr,text='youtube',command=youtube)
but3.place(x=1,y=90)
but4 = customtkinter.CTkButton(fr,text='twitter',command=twitter)
but4.place(x=1,y=120)
x.mainloop()

