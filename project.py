import tkinter as tk
import requests
from playsound import playsound
import random

def main():
    root = tk.Tk()

    root.geometry("700x500")

    def get_text():
        try:
            surah_num = int(surah_entry.get())
            ayah_num = int(ayah_entry.get())
            error1.config(text="")

            text = get_ayah_text(surah_num, ayah_num)
            
            T.delete(1.0,"end")
            T.tag_configure("center", justify='center')
            T.insert(1.0, text)
            T.tag_add("center", 1.0, "end")
            
        except (ValueError,IndexError):
            error1.config(text="بيانات خاطئة")    

    def get_audio():
        try:
            i = random.randint(0, 10000) 
            surah_num = int(surah_entry.get())
            ayah_num = int(ayah_entry.get())
            shiekh1 = shiekh_name_translator(shiekh.get())
            error2.config(text="")

            audio = get_ayah_audio(surah_num, ayah_num, shiekh1)

            # 2. download the data behind the URL
            response = requests.get(audio)
            
            try:
                open(f"{i}.mp3", "wb").write(response.content)
                playsound(f"./{i}.mp3")
            except PermissionError:
                j = random.randint(0, 10000)
                open(f"{i*j}.mp3", "wb").write(response.content)
                playsound(f"./{i*j}.mp3")    

        except (ValueError, TypeError):
            error2.config(text="ادخل بيانات الآية") 


    surah_label = tk.Label(root, text = "ادخل رقم السورة")
    surah_label.pack(pady = 5)

    surah_entry = tk.Entry(root, width=10)
    surah_entry.pack(pady=10)

    ayah_label = tk.Label(root, text = "ادخل رقم الآية")
    ayah_label.pack(pady = 5)

    ayah_entry = tk.Entry(root, width=10)
    ayah_entry.pack(pady=10)

    shiekh = tk.StringVar()
    shiekh.set("الحصري")

    drop = tk.OptionMenu(root, shiekh, "السديس", "عبدالباسط عبدالصمد", "العفاسي", "محمد جبريل", "محمد أيوب", "ماهر المعيقلي", "الحصري" )
    drop.pack()

    btn_input = tk.Button(root, height=1, width=10, text="بحث", command=get_text)
    btn_input.pack()

    error1 = tk.Label(root, text="" ,anchor='e')
    error1.pack(pady=10)


    T = tk.Text(root, height=10, width=40, wrap=tk.WORD,)
    T.pack()


    btn_audio = tk.Button(root, height=1, width=10, text="سماع", command=get_audio)
    btn_audio.pack()

    error2 = tk.Label(root, text="" ,anchor='e')
    error2.pack(pady=10)


    root.mainloop()

def get_ayah_text(surah_num, ayah_num):
    try:
        response = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key={surah_num}%3A{ayah_num}")
        return response.json()["verses"][0]["text_uthmani"]
    except IndexError:
        raise IndexError

def get_ayah_audio(surah_num, ayah_num, shiekh):
    try:
        response_audio = requests.get(f"http://api.alquran.cloud/v1/ayah/{surah_num}:{ayah_num}/{shiekh}")
        return response_audio.json()["data"]["audio"]
    except TypeError:
        raise TypeError

def shiekh_name_translator(shiekh):
    if shiekh == "الحصري":
        return "ar.husary"
    elif shiekh == "السديس":
        return "ar.abdurrahmaansudais"
    elif shiekh == "عبدالباسط عبدالصمد":
        return "ar.abdulsamad"
    elif shiekh == "العفاسي":
        return "ar.alafasy"
    elif shiekh == "محمد جبريل":
        return "ar.muhammadjibreel"
    elif shiekh == "محمد أيوب":
        return "ar.muhammadayyoub"
    elif shiekh == "ماهر المعيقلي":
        return "ar.mahermuaiqly"     



if __name__ == "__main__":
    main()