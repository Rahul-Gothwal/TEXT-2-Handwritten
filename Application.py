#kivy modules
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image as Imag
from kivy.core.window import Window
from kivy.graphics import Color,Rectangle
import time
from kivy.clock import Clock
from fpdf import FPDF
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserIconView
import pickle
import os
from PIL import Image

#For Screen colour
Window.clearcolor=(1,1,1,1)

#variable for different screens
w,h=Window.size

BG = Image.open("Font/base.png")
sizeOfSheet = BG.width
gap, _ = 0, 0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("Font/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases


def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketopn'
            elif letter == ')':
                letter = 'braketcls'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)


def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')
        
def pdf_creation(PNG_FILE, flag=False):
    global name
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split())  # paste using alpha channel as mask
    rgb.save(name+'.pdf',append=flag)


def needle(*args):
         global f,s_y,n,yh,yg,sa,name
         if n%2==0:
            z=0
         else:
            z=0.5
            
         if n>10 and n%2==0:
            s_y+=(1.05/(6*s_y))
            sa.size_hint=(1,s_y)
            sa.bt2.size_hint=(0.1,0.05/s_y)
            sa.bt2.pos_hint={'x':0.9,'y':(s_y-0.05)/s_y}
            yh+=0.17
            yg+=0.17
            
            
         nam=name+".pdf"
        
         if n>10 and n%2==0:
            s_yy=s_y-(1.05/6*s_y)
         else:
            s_yy=s_y
  
            
         lab1=Label(color=(0,0,0,1),text=nam,size_hint=(0.5,0.05/s_yy),pos_hint={'x':z,'y':(s_yy-yh)/s_yy})
         sa.add_widget(lab1)
         
         but=Button(background_normal= "Icon/pdf.png",size_hint=(0.2,0.1/s_yy),pos_hint={'x':z+0.15,'y':(s_yy-yg)/s_yy})
         sa.add_widget(but)
         n+=1
#scrren of logo(first)
class LOGO(FloatLayout):
   def __init__(self,*args,**kwargs):
      super().__init__(*args)
      self.img=Imag(source="Icon/T2H.png",size=(w,h),pos=(0,0))
      self.add_widget(self.img)
      
      Clock.schedule_once(self.ss,5/1)

   def ss(self,instance):
      s.current = "2"

#screen for new pdf
class FIRST(FloatLayout):
   def __init__(self,*args,**kwargs):
      super().__init__(*args)
      
      
      with self.canvas:
               Color(0,0.5,1,1)
               Rectangle(pos=(0,h*0.95),size=(w,h*0.05))
               
      self.ti=TextInput(hint_text="Enter yout text here",size_hint=(0.7,0.5),pos_hint={'x':0.15,'y':0.4})
      self.add_widget(self.ti)
      
      self.bt=Button(font_size=30,text="Generate",size_hint=(0.4,0.07),pos_hint={'x':0.15,'y':0.27},background_normal="Icon/button.png")
      self.add_widget(self.bt)
      self.bt.bind(on_press=self.pop)
      
      self.btt5=Button(font_size=30,text="Select",size_hint=(0.4,0.07),pos_hint={'x':0.45,'y':0.27},background_normal="Icon/button.png")
      self.add_widget(self.btt5)
      
      self.bt3=Button(size_hint=(0.1,0.05),pos_hint={'x':0.9,'y':0.95},background_normal="Icon/list.png")
      self.add_widget(self.bt3)
      
      self.img1=Imag(source="Icon/banner.png",size=(w,h*0.4),pos=(0,-0.37*h))
      self.add_widget(self.img1)
      
      self.bt5=Button(size_hint=(0.1,0.05),pos_hint={'x':0,'y':0.95},background_normal="Icon/info.png")
      self.add_widget(self.bt5)
      
      
      self.bt3.bind(on_press=self.shift)
      self.bt5.bind(on_press=self.popinfo)
      self.btt5.bind(on_press=self.openfile)
      
   def shift(self,*args):
      s.current="3"
      
   def popinfo(self,*args):
      f2=FloatLayout()
      
      self.label=Label(markup=True,halign="center",valign="top",font_size=35,text=""" [b][u]To use this application[/u]:-[/b]

-> Copy the text from source and paste in the "enter 
text" window on the home screen.

-> Click on the generate button and name your PDF 
file and save.

-> Your PDF will be generated along with picture of 
every page in your gallery.

-> Or alternatively you can upload a txt file with text 
in it and can get a PDF generated.

[u][b]Created by[/u]:-[/b] 

Rahul Gothwal, Yugam Sachdeva

[b][u] Note[/u]:- [/b]

If you face any issue feel free to report issue at: 
[b]https://bit.ly/T2H-RS[/b]""",color=(0,0,0,1),size_hint=(1,1),pos_hint={'x':0,'y':0})
      f2.add_widget(self.label)
      
      
      pop1=Popup(title_color=(0,0.5,1,1),background="Icon/white.jpeg",content=f2,title="Information",size_hint=(0.8,0.8),pos_hint={'x':0.1,'y':0.1}) 
      
      pop1.open()
      
  
   def pop(self,instance):
      global f,pop,d,pop4,pop3
      try:
         self.remove_widget(pop4)
         self.remove_widget(pop3)
      except:
         pass
      
      d=instance.text
      if d=="Yes":
         if file_text=='':
            try:
               self.remove_widget(self.llb)
            except:
               pass
               
            self.lb=Label(text="File format is wrong or file is empty!",color=(0,0,0,1),size_hint=(1,0.05),pos_hint={'x':0,'y':0.33})
            self.add_widget(self.lb)
         else:
            self.naming()
      else:
            try:
               self.remove_widget(self.lb)
            except:
               pass
            if self.ti.text=='':
               self.llb=Label(text="Empty PDF can't be generated!",color=(0,0,0,1),size_hint=(1,0.05),pos_hint={'x':0,'y':0.33})
               self.add_widget(self.llb)
            else:
               self.naming()
            
   def naming(self,*args):
         global pop,ff
         ff=FloatLayout()
         
         self.ti1=TextInput(hint_text="Enter PDF name",size_hint=(0.8,0.2),pos_hint={'x':0.1,'y':0.6})
         ff.add_widget(self.ti1)
      
         self.bt1=Button(text="Done",size_hint=(0.4,0.3),pos_hint={'x':0.3,'y':0.08},background_normal="Icon/button.png")
         ff.add_widget(self.bt1)
         self.bt1.bind(on_press=self.pdfgene)
         
         
         pop=Popup(auto_dismiss=False,title_color=(0,0.5,1,1),background="Icon/white.jpeg",content=ff,title="Save PDF",size_hint=(0.8,0.3),pos_hint={'x':0.1,'y':0.3}) 
      
         pop.open()
         
   def openfile(self,*args):
      global pop3
      self.filechoose=FileChooserIconView(path=".")
      pop3=Popup(title="File Manager",content=self.filechoose,size_hint=(1,1),pos_hint={'x':0,'y':0})
      self.add_widget(pop3)
      self.filechoose.bind(on_submit=self.pk)
      
   def pk(self,a,path,b):
      global pop3,file_text,pop4
      f=FloatLayout()
      self.ll=Label(color=(0,0,0,1),text="Do you want to covert this Doc into PDF?",size_hint=(1,0.5),pos_hint={'x':0,'y':0.5})
      f.add_widget(self.ll)
      
      self.yes=Button(text="Yes",font_size=30,size_hint=(0.4,0.25),pos_hint={'x':0.1,'y':0.2}, background_normal="Icon/button.png")
      f.add_widget(self.yes)
      self.yes.bind(on_press=self.pop)
      
      self.no=Button(text="No",font_size=30,size_hint=(0.4,0.25),pos_hint={'x':0.5,'y':0.2}, background_normal="Icon/button.png")
      f.add_widget(self.no)
      self.no.bind(on_press=self.denied)
      
      
      pop4=Popup(background="Icon/white.jpeg",title="Confirmation",title_color=(0,0.5,1,1),content=f,size_hint=(0.8,0.3),pos_hint={'x':0.1,'y':0.35})
      self.add_widget(pop4)
      
      for i in [".txt"]:
         if path[0].endswith(i):       
            files=open(path[0],"r")
            file_text=files.read()
         else:
            file_text=''
            
                       
      
                         
   def denied(self,*args):
      global pop4,name
      self.remove_widget(pop4)
          
   def pdfgene(self,instance):
      global BG,sizeofSheet,allowedChars,gap,name,sa,d,pop
      c=instance.text
      daty=os.listdir('.')
      pdf=self.ti1.text+".pdf"
      if len(self.ti1.text)==0 or pdf in daty:
         self.lb1=Label(text="Name is empty or already exist!",color=(0,0,0,1),size_hint=(1,0.05),pos_hint={'x':0,'y':0.38})
         ff.add_widget(self.lb1)
      else:
         pop.dismiss()
         try:  
            self.remove_widget(self.lb)
         except:
            pass
            
         try:
           if d=="Yes":
               date=file_text
           else:
               date=self.ti.text
               
            
             
           data = date.replace('\n', '')
           name=self.ti1.text
            
           with open(name+".pdf", 'w') as file:
              pass
              
           l = len(data)
           nn = len(data) // 600
           chunks, chunk_size = len(data), len(data) // (nn + 1)
           p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
      
           for i in range(0, len(p)):
              worddd(p[i])
              writee('\n')
              BG.save('%doutput.png' % i)
              BG1 = Image.open("Font/base.png")
              BG = BG1
              gap = 0
              _ = 0
                 
         except ValueError as E:
            print("{}\nTry again".format(E))
              
         imagelist = []
         for i in range(0, len(p)):
            imagelist.append('%doutput.png' % i)
         try:      
            pdf_creation(imagelist.pop(0)[20])
      
      
            for PNG_FILE in imagelist:
               pdf_creation(PNG_FILE, flag=True)
         except:
            pass
                 
         needle()
         self.ti.text=""
         s.current="3"
         
         
 #screen for list of pdf        
class PDFLIST(ScrollView):
   def __init__(self,*args,**kwargs):
      global s_y,n,yh,yg,sa
      super().__init__(*args)
      

      dat=os.listdir('.')
      data=[]
      for item in range(len(dat)):
         if dat[item].endswith(".pdf"):
            data.append(dat[item])
      
      n=len(data)
      sa=FloatLayout()
      s_y=1
      if n<10:
         pass
      else:
         s_y=s_y+(n-10)/12
         
      sa.size_hint=(1,s_y)
      
      with sa.canvas:
               Color(0,0.5,1,1)
               Rectangle(pos=(0,(s_y-0.05)*h),size=(w,h*0.05))   
      sa.bt2=Button(size_hint=(0.1,0.05/s_y),pos_hint={'x':0.9,'y':(s_y-0.05)/s_y},background_normal="Icon/add.png")
      sa.add_widget(sa.bt2)
      sa.bt2.bind(on_press=self.change)
      
      
      
      self.do_scroll_x: False
      self.do_scroll_y: True
      self.scroll_y=1
      self.bar_width=5
      self.size=Window.size 
      self.add_widget(sa)
      
      
      yh=0.2
      for i in range(n):
         if i%2==0:
            z=0
         else:
            z=0.5
            
         sa.lab=Label(color=(0,0,0,1),text=data[i],size_hint=(0.5,0.05/s_y),pos_hint={'x':z,'y':(s_y-yh)/s_y})
         sa.add_widget(sa.lab)
         if i%2!=0:
            yh=yh+0.17
            
      yg=0.16
      for i in range(n):
         if i%2==0:
            z=0.15
         else:
            z=0.65
            
         sa.but=Button(background_normal="Icon/pdf.png",size_hint=(0.2,0.1/s_y),pos_hint={'x':z,'y':(s_y-yg)/s_y})
         sa.add_widget(sa.but)
         if i%2!=0:
            yg=yg+0.17
         
      
 
   def change(self,*args):
      s.current="2"

#main class                      
class profileapp(App):
   def build(self):
      return s
      
s=ScreenManager()

s1=Screen(name="1")
s1.add_widget(LOGO())

s2=Screen(name="2")
s2.add_widget(FIRST())

s3=Screen(name="3")
s3.add_widget(PDFLIST())

s.add_widget(s1)
s.add_widget(s2)
s.add_widget(s3)


profileapp().run()
