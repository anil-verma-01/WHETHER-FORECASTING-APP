from tkinter import *

import requests
import json



df =Tk()

df.title("WHETHER STATUS")

label1 = Label(font=("arial black",15),text="WHETHER FORECASTING APP",bg="orange",width=29)
label1.place(x=565,y=515)


img = PhotoImage(file=r"C:\Users\anilv\Downloads\img.png")
imgl=Label(df,image=img)
imgl.pack()
s=StringVar()

def whether_status(event=None):
    city = s.get()
    url="https://api.weatherapi.com/v1/current.json?key=f6026d8544084f08a8270106243008&q="+city
    df = requests.get(url)
    data = json.loads(df.content)
    show_state.config(text=str(data["location"]["region"]))
    show_country.config(text=str(data["location"]["country"]))
    show_celcius.config(text=str(data["current"]["temp_c"]))
    show_f.config(text=str(data["current"]["temp_f"]))
    show_wind.config(text=str(data["current"]["wind_kph"]))
    show_angle.config(text=str(data["current"]["wind_degree"]))
    show_direction.config(text=str(data["current"]["wind_dir"]))



entbox = Entry(df,font=("arial black",12),bg="orange",width=37,textvariable=s)
entbox.place(x=565,y=555)


btn = Button(df,font=("arial black",14),text="SUBMIT",bg="green",command=whether_status)
btn.place(x=1000,y=530)

entbox.bind("<Return>",whether_status)



txt =Label(font=("Arial black",8),text="PLEAESE ENTER THE NAME HERE WHICH YOU WANT TO CHECK WHETHER STATUS :-")
txt.place(x=30,y=555)

state = Label(font=("Arial black",10),text="STATE AND COUNTRY OF GIVEN CITY")
state.place(x=350,y=580)

show_state =Label(df,font=("arial rounded mt bold",12),fg="red")
show_state.place(x=380,y=600)

show_country = Label(df,font=("arial rounded mt bold",12),fg="red")
show_country.place(x=510,y=600)

temp_c = Label(font=("arial black",10),text="TEMPERATURE IN CELCIUS (°C)")
temp_c.place(x=640,y=580)

show_celcius = Label(df,font=("arial rounded mt bold",12),fg="red")
show_celcius.place(x=750,y=600)

temp_f = Label(font=("Arial black",10),text="TEMPERATURE IN FARHENEITH (°F)")
temp_f.place(x=890,y=580)

show_f = Label(df,font=("arial rounded mt bold",12),fg="red")
show_f.place(x=995,y=600)

wind_speed = Label(font=("arial black",10),text="WIND SPEED IN KPH")
wind_speed.place(x=380,y=620)

show_wind =Label(df,font=("Arial rounded mt bold",12),fg="green")
show_wind.place(x=450,y=638)

wind_angle =Label(font=("arial black",10),text="WIND ANGLE (°)")
wind_angle.place(x=700,y=620)

show_angle =Label(df,font=("arial rounded mt bold",12),fg="green")
show_angle.place(x=750,y=638)

wind_direction =Label(font=("arial black",10),text="WIND DIRECTION")
wind_direction.place(x=950,y=620)

show_direction =Label(df,font=("arial rounded mt bold",12),fg="green")
show_direction.place(x=1000,y=638)


img1 = PhotoImage(file=r"C:\Users\anilv\Downloads\wind degree.png")
imgl1 = Label(df,image=img1)
imgl1.place(x=715,y=663)

img2 = PhotoImage(file=r"C:\Users\anilv\Downloads\wind1.png")
imgl2=Label(df,image=img2)
imgl2.place(x=955,y=660)

img3 = PhotoImage(file=r"C:\Users\anilv\Downloads\wind speed1.png")
imgl3 = Label(df,image=img3)
imgl3.place(x=400,y=665)


img4 = PhotoImage(file=r"C:\Users\anilv\Downloads\wind-logo-png-transparent.png")
imgl4 = Label(df,image=img4)
imgl4.place(x=80,y=600)

img5 =PhotoImage(file=r"C:\Users\anilv\Downloads\OIP.png")
imgl5 = Label(df,image=img5)
imgl5.place(x=200,y=150)

img6 = PhotoImage(file=r"C:\Users\anilv\Downloads\Ws.png")
imgl6 = Label(df,image=img6)
imgl6.place(x=1140,y=150)

txtl = Label(font=("broadway",20),text="Current Whether Information")

txtl.place(x=60,y=300)

txtl2 = Label(font=("broadway",20),text="Real-Time Whether API")
txtl2.place(x=1050,y=300)










df.mainloop()


#"C:\Users\anilv\Downloads\pasted image 01.png"