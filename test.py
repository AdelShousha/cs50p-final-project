# 
# from turtle import width
# from PIL import Image, ImageTk
# import tkinter as tk
# 
# import arabic_reshaper
# from bidi.algorithm import get_display
# import sys
# root = tk.Tk()

# canvas = tk.Canvas(root, width=600, height=300)
# canvas.grid(columnspan=3)

# logo = Image.open("logo.jpg")
# logo= logo.resize((300,205), Image.ANTIALIAS)
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)

# response = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key=2%3A255")
# var = response.json()["verses"][0]["text_uthmani"]
# # text_to_be_reshaped = response.json()["verses"][0]["text_uthmani"]

# # # reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
# # # var = get_display(reshaped_text)
# # # var = reshaped_text[::-1]  # slice backwards


# inst = tk.Label(root, text=f"{var}") #wrap=tk.WORD)
# inst.grid(column=1, row=1)#, width= 10)

# # T = tk.Text(root, height=10, width=30, wrap=tk.WORD)
# # T.pack()
# # T.insert(tk.END, var)

# root.mainloop()

# response = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key=1%3A3")
# response.json()["verses"][0]["text_uthmani"]

# import vlc
# p = vlc.MediaPlayer("https://download.quranicaudio.com/qdc/khalil_al_husary/murattal/1.mp3")
# p.play()

# import requests
# from playsound import playsound

# import json
# import sys
# # response = requests.get("http://api.alquran.cloud/v1/edition?format=audio&language=ar&type=versebyverse")



# surah_num = input("Surah:" )
# ayah_num = input("Ayah:" )

# response_audio = requests.get(f"http://api.alquran.cloud/v1/ayah/{surah_num}:{ayah_num}/ar.alafasy")

# audio = response_audio.json()["data"]["audio"]
# # 2. download the data behind the URL
# response = requests.get(audio)
# # 3. Open the response into a new file called instagram.ico
# open("h.mp3", "wb").write(response.content)

# playsound('./h.mp3')

import json
import requests
import sys
response = requests.get("http://api.alquran.cloud/v1/edition?format=audio&language=ar&type=versebyverse")
print(json.dumps(response.json(), indent=2))