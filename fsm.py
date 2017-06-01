from transitions.extensions import GraphMachine

singer1='如果我是 dj 你會愛我嗎:\n https://www.youtube.com/watch?v=UIBlXO4OIbI'
singer2='帝雉:\nhttps://www.youtube.com/watch?v=WqtfKb4yYAE&list=PLVnPXvGuX__R74_huVRIWY5VyEC23NRdM'
singer3='殺梗之歌:\nhttps://www.youtube.com/watch?v=di6iytkal-8'

singer4='closer:\nhttps://www.youtube.com/watch?v=PT2_F-1esPk'
singer5='Hitorigoto:\nhttps://www.youtube.com/watch?v=vblA_pg1kKM'

string6='Guilty Crown - Departures ～ Blessing:\nhttps://www.youtube.com/watch?v=pQyjzmB_YeU&list=RDAgnrim_5pio&index=3'
string7='Egoist - All Alone With You:\nhttps://www.youtube.com/watch?v=Q5eYNOnyBcU&list=RDAgnrim_5pio&index=6'
xargon1='殺梗 wiki:\nhttps://zh.wikipedia.org/wiki/Xargon'
xargon2='殺梗 twitch:\nhttps://www.twitch.tv/xargon0731'
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '能給我一些糞歌嗎' or text.lower() == '來點糞歌' or text.lower() =='幹你老師點糞歌' or text.lower() =='糞歌' or text.lower() =='國動愛聽的' or text.lower() =='最糞那種歌'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '好心情' or text.lower()=='愉悅的歌' 
    def is_going_to_user(self,update):
        text = update.message.text
        return text.lower()== '回去選歌' or text.lower()== '回' or text.lower()== '選歌'   
    
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '殺梗是誰' or text.lower()=='那個拉風的男人是誰' or text.lower()=='殺梗??'       
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '他有老婆嗎？' or text.lower()=='他老婆是誰'
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '抒情的歌' or text.lower()=='放鬆的歌'    

    def on_enter_state1(self, update):
        global singer1
        global singer2
        global singer3
        update.message.reply_text(singer1 +'\n' + singer2 + '\n' + singer3)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        global singer4
        global singer5
        update.message.reply_text(singer4 +'\n' + singer5)
        
    def on_enter_state3(self, update):
        update.message.reply_text(xargon1 + '\n' + xargon2)
    def on_enter_user(self,update):
        update.message.reply_text("歡迎回來選歌")
    def on_enter_state4(self, update):
        update.message.reply_text("xargon 老婆是優格姊姊\n 附上新聞網址:\nhttp://star.ettoday.net/news/840489 ") 
    def on_enter_state5(self, update):
        global string6
        global string7
        update.message.reply_text(string6+'\n'+string7)       
   
   

    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_exit_state3(self, update):
        print('Leaving state1')        

  
