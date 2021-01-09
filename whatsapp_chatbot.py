from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random,keyboard
from chatterbot import ChatBot
from tkinter import *
from tkinter import filedialog


bot = ChatBot("whatsapp")
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.english.conversations")
def bot_(message,browser):

    query = message
    output = bot.get_response(query)
    message_sent(output,browser)
    return output
def open_chooser():

    result=filedialog.askopenfile(defaultextension=".txt")
    print(result)
    for text in result:
        textField.insert(END,text)
def message_sent(message,browser):
    message_box = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    message_box.send_keys(str(message))
    message_box.send_keys(Keys.ENTER)
def send():
    name = names.get()
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    options.add_argument('--user-data-dir=C:/Users/acer/AppData/Local/Google/Chrome/User Data/Default')
    options.add_argument('--profile-directory=Default')
    chrome_path = "D:/SOFTWARE/chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chrome_path, options=options)
    browser.get("https://web.whatsapp.com/")
    last_message=""
    bot_message=""
    while keyboard.is_pressed('q')==False:
        try:

            search_box = browser.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
            search_box.send_keys(name)
            search_box.send_keys(Keys.ENTER)
            while True:
                try:
                    for i in range(1, 100):
                        try:

                            #msg = browser.find_element_by_xpath(f'//*[@id="main"]/div[3]/div/div/div[3]/div[{i}]')
                            msg=browser.find_element_by_xpath(f'//*[@id="main"]/div[3]/div/div/div[3]/div[{i}]')

                            messgae = msg.text[:len(msg.text) - 6]
                        except Exception as e:
                            break
                    if (str(messgae) != str(last_message) and str(messgae)!=str(bot_message)):
                        last_message = messgae
                        print(messgae)
                        if str(messgae)=="exit":
                            browser.close()
                            root.destroy()
                        bot_message=bot_(messgae, browser)

                    else:
                        #print("Message abort")
                        continue
                except Exception as e:
                    print(e)
        except Exception as e:
            pass






if __name__ == '__main__':
    root=Tk()
    root.geometry("700x500")
    textField=Text(root,width=50,height=30)
    textField.pack(side=LEFT)
    text=Label(root,text="Enter name ")
    text.pack(side=TOP, fill=X,pady=(70,5))
    names = Entry(root)
    names.pack(side=TOP, fill=X)

    button=Button(root,text="choose file",command=open_chooser)
    button.pack(side=RIGHT,padx=(0,30),pady=(0,120))
    button2=Button(root,text="   sent   ",command=send)
    button2.pack(side=LEFT,padx=(30,0),pady=(0,120))

    root.mainloop()
