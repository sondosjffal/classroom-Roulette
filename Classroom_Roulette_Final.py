import tkinter as tk
from tkinter import messagebox
import random, math

class Roulette:
    def __init__(self, root):
        self.root=root; root.title('عجلة أسماء الطلاب'); root.geometry('850x650'); root.configure(bg='#172033')
        self.names=[]; self.remaining=[]; self.angle=0
        tk.Label(root,text='🎡 عجلة أسماء الطلاب',font=('Arial',25,'bold'),fg='white',bg='#172033').pack(pady=12)
        top=tk.Frame(root,bg='#172033'); top.pack()
        self.entry=tk.Entry(top,font=('Arial',14),width=30,justify='right'); self.entry.pack(side='right',pad=5)
        tk.Button(top,text='إضافة طالب',command=self.add,font=('Arial',12)).pack(side='right',pad=5)
        tk.Button(top,text='تحميل أسماء من ملف txt',command=self.load,font=('Arial',12)).pack(side='right',pad=5)
        self.canvas=tk.Canvas(root,width=500,height=400,bg='#172033',highlightthickness=0); self.canvas.pack(pady=8)
        self.result=tk.Label(root,text='أضف أسماء الطلاب ثم اضغط ابدأ',font=('Arial',20,'bold'),fg='#ffd166',bg='#172033'); self.result.pack(pady=8)
        buttons=tk.Frame(root,bg='#172033'); buttons.pack()
        tk.Button(buttons,text='🎯 ابدأ الدوران',font=('Arial',16,'bold'),bg='#06d6a0',command=self.spin).pack(side='right',padx=8)
        tk.Button(buttons,text='إعادة الجولة',font=('Arial',14),command=self.reset).pack(side='right',padx=8)
        tk.Button(buttons,text='مسح الأسماء',font=('Arial',14),command=self.clear).pack(side='right',padx=8)
        self.draw()
    def add(self):
        n=self.entry.get().strip()
        if n: self.names.append(n); self.remaining.append(n); self.entry.delete(0,'end'); self.draw()
    def load(self):
        from tkinter import filedialog
        p=filedialog.askopenfilename(filetypes=[('Text files','*.txt')])
        if p:
            with open(p,encoding='utf-8-sig') as f: self.names=[x.strip() for x in f if x.strip()]
            self.remaining=self.names.copy(); self.draw()
    def reset(self): self.remaining=self.names.copy(); self.result.config(text='تمت إعادة الجولة'); self.draw()
    def clear(self): self.names=[]; self.remaining=[]; self.result.config(text='أضف أسماء الطلاب'); self.draw()
    def draw(self):
        c=self.canvas; c.delete('all'); cx=250; cy=200; r=175
        if not self.remaining: c.create_oval(cx-r,cy-r,cx+r,cy+r,fill='#34415e',outline='white',width=3); c.create_text(cx,cy,text='أضف أسماء',fill='white',font=('Arial',20)); return
        count=len(self.remaining); colors=['#ef476f','#ffd166','#06d6a0','#118ab2','#9b5de5','#f15bb5']
        for i,n in enumerate(self.remaining):
            a1=90-i*360/count; extent=-360/count
            c.create_arc(cx-r,cy-r,cx+r,cy+r,start=a1,extent=extent,fill=colors[i%len(colors)],outline='white',width=2)
            mid=math.radians(a1+extent/2); c.create_text(cx+ r*.58*math.cos(mid),cy-r*.58*math.sin(mid),text=n[:18],fill='white',font=('Arial',10,'bold'))
        c.create_polygon(cx-12,cy-r-8,cx+12,cy-r-8,cx,cy-r+18,fill='white')
    def spin(self):
        if not self.remaining: messagebox.showinfo('تنبيه','لا توجد أسماء متبقية. أعد الجولة أو أضف أسماء.'); return
        chosen=random.choice(self.remaining); self.remaining.remove(chosen); self.draw(); self.result.config(text='🎉 الطالب المختار: '+chosen); self.root.bell()
if __name__=='__main__':
    root=tk.Tk(); app=Roulette(root); root.mainloop()
