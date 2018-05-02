from tkinter import *
railway=Tk()
count=0
count1=0
def addrec():
    f=open('railwaydb.txt','a')
    trainname=s1.get()
    trainprice=s2.get()
    trainno=s3.get()
    departuredate=s4.get()
    availability=s5.get()
    f.writelines(trainname.ljust(20)+trainprice.ljust(10)+trainno.ljust(30)+departuredate.ljust(15)+availability.ljust(15)+"\n")
    global count1
    count1= count1+1
    f.close()
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
def nextrec():
    i=0
    f=open('railwaydb.txt','r')
    global count
    global count1
    while(i<=count):
        l=f.readline()
        if  len(l) == 0:
            l8=Label(railway, text = "No record Found")
            l8.grid(row=7,column=4)
            return
        i=i+1
    if count1==i:
        l8=Label(railway, text = "On last record")
        l8.grid(row=7,column=4)
        return
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    count=count+1
    f.close()
def prev():
    f=open('railwaydb.txt','r')
    i=0
    l1=[]
    global count
    count=count-1
    while(i<=count-1):
        l=f.readline()
        if  len(l) == 0:
            l8=Label(railway, text = "No record Found")
            l8.grid(row=6,column=4)
            return
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    
    f.close()  
def update():
    trainname=s1.get()
    trainprice=s2.get()
    trainno=s3.get()
    departuredate=s4.get()
    availability=s5.get()
    f=open("railwaydb.txt","r")
    h=f.readlines()
    f.close()
    f=open("railwaydb.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=brand):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
        else :
            f.writelines(brand.ljust(20)+price.ljust(10)+model.ljust(30)+manf.ljust(15)+avl.ljust(15)+"\n")
            flag=1
    f.close()
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("railwaydb.txt","r")
    h=f.readlines()
    f.close()
    f=open("railwaydb.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
    f.close()
def search():
    k=s1.get()
    f=open("railwaydb.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
def lr():
    
    f=open('railwaydb.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[a-1].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
def fr():
    f=open('railwaydb.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[0].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l0=Label(railway,text="..........Railway Enquiry..........")
l1=Label(railway,text="Train Name")
l2=Label(railway,text="Train Price")
l3=Label(railway,text="Train No")
l4=Label(railway,text="Departure Date")
l5=Label(railway,text="Availability")
t1=Entry(railway,textvariable=s1)
t2=Entry(railway,textvariable=s2)
t3=Entry(railway,textvariable=s3)
t4=Entry(railway,textvariable=s4)
t5=Entry(railway,textvariable=s5)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1=Button(railway,text="Next", command=nextrec)
b2=Button(railway,text="Add", command=addrec)
b3=Button(railway,text="Delete", command=delete)
b4=Button(railway,text="Search", command=search)
b5=Button(railway,text="Update", command=update)
b7=Button(railway,text="Last Record", command=lr)
b6=Button(railway,text="First Record", command=fr)
b8=Button(railway,text="Previous", command=prev)
b1.grid(row=8,column=1)
b2.grid(row=2,column=3)
b3.grid(row=8,column=2)
b4.grid(row=4,column=3)
b5.grid(row=8,column=3)
b6.grid(row=7,column=1)
b7.grid(row=7,column=3)
b8.grid(row=7,column=2)
railway.mainloop()
