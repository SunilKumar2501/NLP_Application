from tkinter import *
from tkinter import messagebox


from mydb import Database
from myapi import API
class NLPApp:
    def __init__(self):
        #Create db object
        self.dbo = Database()
        self.apio = API()
        # Login GUI load
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap("resources/icon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg = "#34495E")

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()

        heading = Label(self.root,text="NLPApp",bg = "#34495E",fg = "white")
        heading.pack(pady = (30,30))
        heading.configure(font = ("verdana",24,"bold"))

        label1 = Label(self.root,text = "Enter Email")
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (5,10),ipady = 5)

        label2 = Label(self.root,text = "Enter Password")
        label2.pack(pady = (10,10))

        self.password_input = Entry(self.root,width = 50)
        self.password_input.pack(pady = (5,10),ipady = 5)

        login_btn = Button(self.root,text = "Login", width = 30, height = 2, command = self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text= "Not a member ?")
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text = "Register Now", command = self.register_gui)
        redirect_btn.pack(pady = (20,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="sky blue", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50)
        self.password_input.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.root, text="Register", width=30, height=2,
         command = self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a member ?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(20, 10))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success", "Registration successful. You can login now")
        else:
            messagebox.showerror("Error","Email already Exists or Field is empty")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo("Success","Login successfull")
            self.home_gui()
        else:
            messagebox.showerror("Error","Incorrect email/password")

    def home_gui(self):
        self.clear()
        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=4,
        command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        # ner_btn = Button(self.root, text="Named Entity Recoginition", width=30, height=4,
        # command=self.perform_registration)
        # ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=4,
        command=self.emotional_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", command= self.login_gui)
        logout_btn.pack(pady=(10 , 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text="NLPApp",bg = "#34495E",fg = "white")
        heading.pack(pady = (30,30))
        heading.configure(font = ("verdana",24,"bold"))


        heading2 = Label(self.root,text="Sentiment Analysis",bg = "#34495E",fg = "white")
        heading2.pack(pady = (10,20))
        heading2.configure(font = ("verdana",24,))

        label1 = Label(self.root, text="Enter the text: ")
        label1.pack(pady=(20, 10))

        self.sentiment_input = Entry(self.root,width = 50)
        self.sentiment_input.pack(pady = (5,10),ipady = 4)

        sentiment_btn = Button(self.root,text = "Analyze sentiment",command = self.do_sentiment_analysis)
        sentiment_btn.pack(pady = (10,10))

        self.sentiment_result = Label(self.root, text="",bg = "#34495E" , fg = "white")
        self.sentiment_result.pack(pady=(20, 10))
        self.sentiment_result.configure(font = ("verdana" ,16))

        goback_btn = Button(self.root,text = "GO BACK", command = self.home_gui)
        goback_btn.pack(pady = (10,10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        # for i in result:
        #     print(i,result[i])
        self.sentiment_result["text"] = f"(Type -> {result["type"]})" "\n" f"(Score -> {result["score"]})"

    def emotional_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        heading2 = Label(self.root, text="Emotional Prediction", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 24,))

        label1 = Label(self.root, text="Enter the text: ")
        label1.pack(pady=(20, 10))

        self.emotional_input = Entry(self.root, width=50)
        self.emotional_input.pack(pady=(5, 10), ipady=4)

        emotional_btn = Button(self.root, text="Analyze emotions", command=self.emotional_analysis)
        emotional_btn.pack(pady=(10, 10))

        self.emotional_result = Label(self.root, text="", bg="#34495E", fg="white")
        self.emotional_result.pack(pady=(20, 10))
        self.emotional_result.configure(font=("verdana", 16))

        goback_btn = Button(self.root, text="GO BACK", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def emotional_analysis(self):
        text = self.emotional_input.get()
        d = self.apio.emotional_detection(text)
        l = []
        for i in d:
            for j in d[i]:
                res = l.append([j, d[i][j]])
        answer = (sorted(l, key=lambda x: x[1], reverse=True)[:3])
        result = "".join([f"{item[0]}: {item[1]}\n" for item in answer])
        self.emotional_result["text"] = result


nlp = NLPApp()



