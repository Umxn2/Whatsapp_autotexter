
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random
lite_texts = [
    # "I am not against Jihad",
    # "lite",
    # "Jigga Jigga Jigga",
    # "boring message"
    "something nuetral"


]
happy_texts = [
    # "you make me cum very hard",
    # "i just wanna squeeze you all day long",
    # "I masturbate to you every night",
    # "Thank you bb girl",
    # "Ill kiss you good night today"
    "something good"

]
angry_texts = [
    # "fuck you retarded nigger",
    # "your cock so small even small kids cant suck it",
    # "kys bhaijaan",
    # "I like muslims more than i like you",
    # "great day for you to die"
    "something bad"
]
def main(words, name):
    sentiment = SentimentIntensityAnalyzer()
    

    words = words.replace('msg-dblcheck','')
    words = words.replace('1 unread message', '')
    #words = words.replace()
    ind = words.find('TODAY')
    words = words[ind+5:]
    
    words = words.replace('tail-in',f"{name}:")
    words = words.replace('tail-out',"Umang:")
    import re
    class Text():
        sender = ""
        Time = ""
        body = ""

    for i in range(len(words)):
        if words[i:i+5]==words[i+5:i+10]:
            words = words.replace(words[i:i+10],words[i:i+5])
    words = words.replace('forward-chat','')


    # Texts = []
    # name = ""
    # t = Text()
    # exp = "\d"
    # for i in range(len(chat_on_day)):
    #     for j in range(0, len(chat_on_day) ):
    #         name+=chat_on_day[j]
    #         if(name=="Umang:"):
    #             t.sender = "Umang"
    #             m = j
    #             break

    #         elif(name=='Saksham'):
    #             t.sender="Saksham"
    #             break
                
    #     if(chat_on_day[i].isdigit()==True and chat_on_day[i+1].isdigit()==True and chat_on_day[i+2]==':'and chat_on_day[i+3].isdigit()==True and chat_on_day[i+4].isdigit()==True):
    #         t.body = chat_on_day[m+1:i]
    #         t.Time = chat_on_day[i:i+5]
    #         break
    # print(t.body,t.sender,t.Time)
        
    # saksham = []
    # umang = []
    # umang_text = ""
    # saksham_text = ""
    # loader = ""
    # direction = True
    # print(words)

    # if(words[:len('Umang:')]=="Umang:"):
    #     direction = True
    # else:
    #     direction = False

    # for i in range(len(words)):
    #     if(words[i:i+len("Umang:")]=="Umang:"):
    #         if(saksham_text!=''):
    #             saksham.append(saksham_text)
    #             saksham_text=""
    #             direction = True
    #     if(words[i:i+len(f"{name}:")]==f"{name}:"):
    #         if(umang_text!=''):
    #             umang.append(umang_text)
    #             umang_text=""
    #             direction = False
    #     if(direction==True):
    #         umang_text+=words[i]
    #     if(direction==False):
    #         saksham_text+=words[i]

            
            

    # print(umang)
    # print(saksham)
    # All_Texts = []
    # for chats in umang:
    #     t = Text
            
                
    print(words)
    His_mess= True
    ind = words.rfind("Umang:")
    ind2 = words.rfind(f"{name}:")
    Last = Text()
    reg = re.compile(r'\d\d:\d\d')
    if(ind>ind2):


        His_mess= False
        last_mess = words[ind:]
        Last.sender = last_mess[:len("Umang")]
        Last.Time = last_mess[-5:]
        mo = reg.findall(last_mess)

        for m in mo[:-1]:
            last_mess = last_mess.replace(m, '')
        
        #a=mo.group()
        #last_mess = last_mess.replace(a, f'{a}\n' )
        Last.body = last_mess[len("Umang:"):-5]
        

    else:
        His_mess = True
        last_mess = words[ind2:]
        Last.sender = last_mess[:len(f"{name}")]
        Last.Time = last_mess[-5:]
        mo = reg.findall(last_mess)

        for m in mo[:-1]:
            last_mess = last_mess.replace(m, '')
        
        #a=mo.group()
        #last_mess = last_mess.replace(a, f'{a}\n' )
        Last.body = last_mess[len(f"name:"):-5]

    print(Last.body, Last.sender, Last.Time)
    
    if(Last.sender!="Umang"):
        se = sentiment.polarity_scores(Last.body)

        print(se)
        score = se["compound"]
        if(score<-0.1):
            text= random.choice(angry_texts)
        elif(score>0.1):
            text=random.choice(happy_texts)
        else:
            text=random.choice(lite_texts)
    else:
        return None
    return text


# if(Last.sender == name):



