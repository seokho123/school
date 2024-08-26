import tkinter as tk
import webbrowser

window = tk.Tk()
window.title("SelfDiagnoseProgramme")
window.geometry("600x900")
window.configure(bg="lightblue")
global fontsize
fontsize=18
pg1qs=['I worry about things that normally do not matter.','I felt afraid.','I felt more depressed than usual.','We talked less than usual.','I could not do something properly.','I felt like people around me hated me.','Tend to be obsessed with the past and future.','I do not get a restful sleep and wake up often in the early morning.','Appetite has noticeably decreased or increased.','Everything felt painful and bothersome.']
pg2qs=['I felt very dissatisfied.','I felt like my life had already failed.','I became more tired than usual.','I thought my appearance was bad.','I am lonely.','I do not know why I go to school.','There are many cases of putting off things that need to be done.','I love myself.','I feel like all unfortunate events are my fault.','Interesting things happen in life.']
pg3qs=['My mood swings have gotten worse.','I think I am as capable as other people.','I felt like I had let myself and my family down.','I feel anxious even while resting.','I have attempted self-harm.','I felt an indescribable pressure.','Even if I get help, I do not think my depression will go away.','Not happy.','I thought it would be better to die than to live a life like this.','Have you attempted or planned suicide?']
page1=[]
page2=[]
page3=[]

def optionpage():
    def bkoption():
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()
        label2.place(relx=0.7, rely=0.15)
        button1.place(relx=0.35, rely=0.3)
        button2.place(relx=0.35, rely=0.4)
        button3.place(relx=0.35, rely=0.5)
        btback.place_forget()
        fontoption.place_forget()
        label2.place_forget()
    def fontpage():
        def fontinit():
            global fontsize
            fontsize = 24
            label.config(font=("Helvetica",fontsize))
        def bkfont():
            btfontup.place_forget()
            btfontdn.place_forget()
            btback1.place_forget()
            fontoption.pack()
            fontoption.place(relx=0.35, rely=0.3)
            btinit.place_forget()
        fontoption.place_forget()
        btfontup=tk.Button(window, text="Font Size Up",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=fontup)
        btfontup.place(relx=0.35,rely=0.3)
        btfontdn=tk.Button(window, text="Font Size Down",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=fontdn)
        btfontdn.place(relx=0.35,rely=0.4)
        btinit=tk.Button(window, text="Initialise Font Size",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=fontinit)
        btinit.place(relx=0.35,rely=0.5)
        btback1=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=bkfont)
        btback1.place(relx=0.35,rely=0.6)
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    label2.place_forget()
    fontoption = tk.Button(window, text="Font option",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=fontpage)
    fontoption.place(relx=0.35, rely=0.3)
    btback=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=bkoption)
    btback.place(relx=0.35,rely=0.5)
    
def fontup():
    global fontsize
    fontsize += 2
    label.config(font=("Helvetica",fontsize))
    label2.config(font=("Helvetica",fontsize))
    if fontsize>=18:
        fontsize=18

def fontdn():
    global fontsize
    fontsize -= 2
    label.config(font=("Helvetica",fontsize))
    if fontsize<=8:
        fontsize=8

def start1():
    def bkmenu():
        window.geometry("600x900")
        button1.pack()
        button2.pack()
        button3.pack()
        label2.pack()
        label2.place(relx=0.7, rely=0.15)
        button1.place(relx=0.35, rely=0.3)
        button2.place(relx=0.35, rely=0.4)
        button3.place(relx=0.35, rely=0.5)
        btback2.place_forget()
        label2.place_forget()
        lbintro.place_forget()
        lbintro2.place_forget()
        lbintro3.place_forget()
        lbintro4.place_forget()
        btnext.place_forget()
        label.pack()
        label2.pack()
        label.place(relx=0.16, rely=0.05)
        label2.place(relx=0.7, rely=0.15)
    def next():
        def qs1():
            btok.place_forget()
            lbexp.place_forget()
            lbexp2.place_forget()
            bgc="grey"
            fgc="white"
            def finish():
                def lookfor():
                    def gohyp():
                        webbrowser.open("youthline.co.nz")
                    btfin1.place_forget()
                    hide=tk.Label(result_window, text="",bg="lightblue",fg="white",font=("Helvetica", 12), width=200, height=17)
                    hide.place(relx=0.01,rely=0.5)
                    option1 = tk.Label(result_window, text="1. To speak to health-related faculty and staff at school and get help.",bg="lightblue", font=("Helvetica", fontsize))
                    option1.place(relx=0.01,rely=0.1)
                    option2 = tk.Label(result_window, text="2. If this is a simple matter, you can talk to your usual best friend or most reliable friend to solve it.",bg="lightblue", font=("Helvetica", fontsize))
                    option2.place(relx=0.01,rely=0.2)
                    option3 = tk.Label(result_window, text="3. You can get a lot of psychiatric services at youthline.co.nz .",bg="lightblue", font=("Helvetica", fontsize))
                    option3.place(relx=0.01,rely=0.3)
                    option4 = tk.Label(result_window, text="4. You can call 111 (emergency telephone number in NZ) to receive information and solutions related to mental health.",bg="lightblue", font=("Helvetica", fontsize))
                    option4.place(relx=0.01,rely=0.4)
                    option5 = tk.Label(result_window, text="5. If you are in extreme conditions such as suicidal thoughts, go to the emergency room in your area. ",bg="lightblue", font=("Helvetica", fontsize))
                    option5.place(relx=0.01,rely=0.5)
                    hyp=tk.Button(result_window, text="GO",bg="gray",fg="white",font=("Helvetica", 12), width=10, height=1,command=gohyp)
                    hyp.place(relx=0.8,rely=0.26)
                    ck2 = tk.Label(result_window, text="Click twice!",bg="lightblue", font=("Helvetica", fontsize))
                    ck2.place(relx=0.42,rely=0.93)
                  

                bcl="lightblue"
                fcl="black"
                global result
        
                result=sum(page1+page2+page3)/30
                result_window = tk.Tk()
                result_window.title("Result")
                result_window.geometry("1600x900")
                result_window.configure(bg="lightblue")
                you_result = tk.Label(result_window, text=f"Your result is : {result}",bg="lightblue", font=("Helvetica", fontsize))
                you_result.place(relx=0.1,rely=0.1)

                btfin1=tk.Button(result_window, text="Look for options",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=lookfor)
                btfin1.place(relx=0.4,rely=0.93)
                btfin2=tk.Button(result_window, text="Exit",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=result_window.quit)
                btfin2.place(relx=0.5,rely=0.93)
                if result > 0 and result <30:
                    rslow1 = tk.Label(result_window, text="You are feeling depressed. Recognizing your feelings and trying to work them out is very difficult, and you have done it.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow1.place(relx=0.02,rely=0.2)
                    rslow2 = tk.Label(result_window, text="First of all, based on the results of the programme, your condition is on the good side and you don't have to worry too much at the moment.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow2.place(relx=0.02,rely=0.3)
                    rslow3 = tk.Label(result_window, text="But the fact that you used this program means that you are worried about your own condition and I can offer some solutions that can ease your concern.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow3.place(relx=0.02,rely=0.4)
                    rslow4 = tk.Label(result_window, text="First, remember the trivial joys of daily life while maintaining a regular life. It will give you a great sense of accomplishment if you gather even these trivial things.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow4.place(relx=0.02,rely=0.5)
                    rslow5 = tk.Label(result_window, text="In fact, you don't have to worry too much because your condition is no different from the average person.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow5.place(relx=0.02,rely=0.6)
                    rslow6 = tk.Label(result_window, text="If you want to get professional help, press the 'Search for help' button below, or if not, you can exit the program with the exit button. Thank you again for using my programme.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rslow6.place(relx=0.02,rely=0.7)
                if result >=30 and result < 60:
                    rsmid1 = tk.Label(result_window, text="You are feeling depressed. Recognizing your feelings and trying to work them out is very difficult, and you have done it.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid1.place(relx=0.01,rely=0.2)
                    rsmid2 = tk.Label(result_window, text="Your condition is not bad, but it is not good enough not to have to worry.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid2.place(relx=0.01,rely=0.3)
                    rsmid3 = tk.Label(result_window, text="This programme provides several ways to relieve your depression.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid3.place(relx=0.01,rely=0.4)
                    rsmid4 = tk.Label(result_window, text="If people feel depressed, people tend to stay indoors. However, the more you do, the more you should enjoy a light walk and relieve your depression.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid4.place(relx=0.01,rely=0.5)
                    rsmid5 = tk.Label(result_window, text="Next, don't obsess too much about the past or the future. Focus on the present and reflect realistically on yourself.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid5.place(relx=0.01,rely=0.6)
                    rsmid6 = tk.Label(result_window, text="Lastly, you should get enough sleep on a regular basis. This is because sleep can greatly alleviate physical and mental fatigue. Cell phones never lead you to a good sleep.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid6.place(relx=0.01,rely=0.7)
                    rsmid7 = tk.Label(result_window, text="If your depression is not alleviated this way, you should consider professional advice. Click the button below to check out the possible options.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rsmid7.place(relx=0.01,rely=0.8)
                if result >=60 and result < 90:
                    rshi1 = tk.Label(result_window, text="You are feeling depressed. Recognizing your feelings and trying to work them out is very difficult, and you have done it.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi1.place(relx=0.01,rely=0.2)
                    rshi2 = tk.Label(result_window, text="Unfortunately, your current condition is not good enough, but it can be good enough.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi2.place(relx=0.01,rely=0.3)
                    rshi3 = tk.Label(result_window, text="First of all, you seem to need professional help and adequate medication.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi3.place(relx=0.01,rely=0.4)
                    rshi4 = tk.Label(result_window, text="You don't have to be afraid of medication. Mental illness is also a problem with the brain, so it is very natural to treat it with medication.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi4.place(relx=0.01,rely=0.5)
                    rshi5 = tk.Label(result_window, text="If you feel like you're hurting yourself or killing yourself, make sure you don't cover yourself up and ask others for help. There is no shame in this.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi5.place(relx=0.01,rely=0.6)
                    rshi6 = tk.Label(result_window, text="Finally, you can look at the available psychiatric treatment options through the button below.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi6.place(relx=0.01,rely=0.7)
                    rshi7 = tk.Label(result_window, text="Thank you for using my programme",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rshi7.place(relx=0.01,rely=0.8)
                if result >=90:
                    rscru1 = tk.Label(result_window, text="You are feeling depressed. Recognizing your feelings and trying to work them out is very difficult, and you have done it.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rscru1.place(relx=0.01,rely=0.2)
                    rscru2 = tk.Label(result_window, text="If you didn't enter a false value, you're in a very serious state.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rscru2.place(relx=0.01,rely=0.3)
                    rscru3 = tk.Label(result_window, text="You are very unlikely to be able to alleviate your condition on your own and need professional help.",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rscru3.place(relx=0.01,rely=0.4)
                    rscru4 = tk.Label(result_window, text="Look at the options through the button below",bg=bcl,fg=fcl, font=("Helvetica", fontsize))
                    rscru4.place(relx=0.01,rely=0.5)
                result_window.mainloop()
                
            def next3():
                def bkfinish():
                    def back3():
                        global page1
                        page1=[]
                        for j in range(0,10):
                            btlbs=tk.Label(window, text=pg1qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                            lbhei=0.05 + 0.09 * (j)      
                            btlbs.place(relx=0.02,rely=lbhei)
                        btnext2=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=next2)
                        btnext2.place(relx=0.4,rely=0.93)
                    global page2
                    page2=[]
                    for j in range(0,10):
                        btlbs=tk.Label(window, text=pg2qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                        lbhei=0.05 + 0.09 * (j)      
                        btlbs.place(relx=0.02,rely=lbhei)
                    btnext3=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=next3)
                    btnext3.place(relx=0.4,rely=0.93)
                    btback3=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=back3)
                    btback3.place(relx=0.5,rely=0.93)
                
                def check3():
                    page3.append(int(ent1.get()))
                    page3.append(int(ent2.get()))
                    page3.append(int(ent3.get()))
                    page3.append(int(ent4.get())*1.25)
                    page3.append(int(ent5.get()))
                    page3.append(int(ent6.get()))
                    page3.append(int(ent7.get())*1.25)
                    page3.append(int(ent8.get()))
                    page3.append(int(ent9.get()))
                    page3.append(int(ent10.get())*1.25)
                for j in range(0,10):
                    btlbs=tk.Label(window, text=pg3qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                    lbhei=0.05 + 0.09 * (j)      
                    btlbs.place(relx=0.02,rely=lbhei)
                btsub2=tk.Button(window, text="Submit",bg=bgc,fg=fgc,font=("Helvetica", 12), width=8, height=1,command=check3)
                btsub2.place(relx=0.63,rely=0.06)
                btlbs=tk.Label(window, text=pg3qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                lbhei=0.05 + 0.09 * (j)      
                btlbs.place(relx=0.02,rely=lbhei)
                btfinish=tk.Button(window, text="Finish",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=finish)
                btfinish.place(relx=0.4,rely=0.93)
                finishbk=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=bkfinish)
                finishbk.place(relx=0.5,rely=0.93)

            def next2():
                def back3():
                    global page1
                    page1=[]
                    for j in range(0,10):
                        btlbs=tk.Label(window, text=pg1qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                        lbhei=0.05 + 0.09 * (j)      
                        btlbs.place(relx=0.02,rely=lbhei)
                    btnext2=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=next2)
                    btnext2.place(relx=0.4,rely=0.93)

                def check2():
                    page2.append(int(ent1.get()))
                    page2.append(int(ent2.get()))
                    page2.append(int(ent3.get()))
                    page2.append(int(ent4.get()))
                    page2.append(int(ent5.get()))
                    page2.append(int(ent6.get())*1.25)
                    page2.append(int(ent7.get()))
                    page2.append(int(ent8.get())*1.25)
                    page2.append(int(ent9.get()))
                    page2.append(int(ent10.get()))
                btsub2=tk.Button(window, text="Submit",bg=bgc,fg=fgc,font=("Helvetica", 12), width=8, height=1,command=check2)
                btsub2.place(relx=0.63,rely=0.06)
                btnext2.place_forget()
                for j in range(0,10):
                    btlbs=tk.Label(window, text=pg2qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                    lbhei=0.05 + 0.09 * (j)      
                    btlbs.place(relx=0.02,rely=lbhei)
                btnext3=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=next3)
                btnext3.place(relx=0.4,rely=0.93)
                btback3=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=back3)
                btback3.place(relx=0.5,rely=0.93)
                                
            def check():
                page1.append(int(ent1.get()))
                page1.append(int(ent2.get()))
                page1.append(int(ent3.get()))
                page1.append(int(ent4.get()))
                page1.append(int(ent5.get()))
                page1.append(int(ent6.get()))
                page1.append(int(ent7.get())*1.25)
                page1.append(int(ent8.get()))
                page1.append(int(ent9.get()))
                page1.append(int(ent10.get()))
            btsub1=tk.Button(window, text="Submit",bg=bgc,fg=fgc,font=("Helvetica", 12), width=8, height=1,command=check)
            btsub1.place(relx=0.63,rely=0.06)   
            for j in range(0,10):
                btlbs=tk.Label(window, text=pg1qs[j],bg="lightblue",font=("Helvetica", fontsize),width=50)       
                lbhei=0.05 + 0.09 * (j)      
                btlbs.place(relx=0.02,rely=lbhei)
            ent1 = tk.Entry()
            ent1.place(relx=0.7,rely=0.06)
            ent2 = tk.Entry()
            ent2.place(relx=0.7,rely=0.15)
            ent3 = tk.Entry()
            ent3.place(relx=0.7,rely=0.24)
            ent4 = tk.Entry()
            ent4.place(relx=0.7,rely=0.33)
            ent5 = tk.Entry()
            ent5.place(relx=0.7,rely=0.42)
            ent6 = tk.Entry()
            ent6.place(relx=0.7,rely=0.51)
            ent7 = tk.Entry()
            ent7.place(relx=0.7,rely=0.60)
            ent8 = tk.Entry()
            ent8.place(relx=0.7,rely=0.69)
            ent9= tk.Entry()
            ent9.place(relx=0.7,rely=0.78)
            ent10 = tk.Entry()
            ent10.place(relx=0.7,rely=0.87)
            btnext2=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=15, height=1,command=next2)
            btnext2.place(relx=0.4,rely=0.93)
    
        btback2.place_forget()
        btnext.place_forget()
        lbintro.place_forget()
        lbintro2.place_forget()
        lbintro3.place_forget()
        lbintro4.place_forget()
        lbexp = tk.Label(window, text="This programme has 30 questions and you can put 0 to 100 for each question.",bg="lightblue", font=("Helvetica", fontsize))
        lbexp.place(relx=0.1,rely=0.05)
        lbexp2 = tk.Label(window, text="Please click submit button after you finish filling numbers.",bg="lightblue", font=("Helvetica", fontsize))
        lbexp2.place(relx=0.1,rely=0.15)
        btok=tk.Button(window, text="OK",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=qs1)
        btok.place(relx=0.35,rely=0.4)

    window.geometry("1600x900")
    label.place_forget()
    label2.place_forget()
    btnext=tk.Button(window, text="Next",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=next)
    btnext.place(relx=0.35,rely=0.5)
    btback2=tk.Button(window, text="Back",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=bkmenu)
    btback2.place(relx=0.35,rely=0.6)
    lbintro = tk.Label(window, text="Hi, I am Seokho and welcome to my programme.",bg="lightblue", font=("Helvetica", fontsize))
    lbintro.place(relx=0.1,rely=0.05)
    lbintro2 = tk.Label(window, text="This programme is made for people who are struggling with mental sickness such as depression.",bg="lightblue", font=("Helvetica", fontsize))
    lbintro2.place(relx=0.1,rely=0.12)
    lbintro3 = tk.Label(window, text="Mental illness is absolutely nothing to be ashamed of, and since it is a type of illness like a cold,",bg="lightblue", font=("Helvetica", fontsize))
    lbintro3.place(relx=0.1,rely=0.19)
    lbintro4 = tk.Label(window, text="it is very natural to self-diagnose and receive treatment accordingly.",bg="lightblue", font=("Helvetica", fontsize))
    lbintro4.place(relx=0.1,rely=0.26)
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    
label = tk.Label(window, text="Self Diagnose Programme",bg="lightblue", font=("Helvetica", fontsize))
label.place(relx=0.16, rely=0.05)
label2 = tk.Label(window, text="By Seokho Kang",bg="lightblue", font=("Helvetica", 10))
label2.place(relx=0.7, rely=0.15)
button1 = tk.Button(window, text="Start",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=start1)
button1.place(relx=0.35, rely=0.3)
button2 = tk.Button(window, text="Option",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2,command=optionpage)
button2.place(relx=0.35, rely=0.4)
button3 = tk.Button(window, text="Exit",bg="gray",fg="white",font=("Helvetica", 12), width=20, height=2, command=window.quit)
button3.place(relx=0.35, rely=0.5)

window.mainloop()
