# Quran Python 
## Video Demo:  https://youtu.be/56zYQeYQ0gw
This is a quran app that takes the number of surah and the number of ayah then it displays it with the option of hearing the recitation of the ayah.

The app uses python tkinter library to make the gui and uses two different quran api, one for getting the script or the arabic written form of the verse and the other one for the recitation.

the text api 'https://quran.api-docs.io'

the recitation api 'https://alquran.cloud/api'

## Gui setup 
The gui setup is in the main function
it has a label for entering the number of the surah and the number of the ayah
```python
surah_label = tk.Label(root, text = "ادخل رقم السورة")
surah_label.pack(pady = 5)
surah_entry = tk.Entry(root, width=10)
surah_entry.pack(pady=10)

ayah_label = tk.Label(root, text = "ادخل رقم الآية")
ayah_label.pack(pady = 5)
ayah_entry = tk.Entry(root, width=10)
ayah_entry.pack(pady=10)
```
it has also a dropdown menu for chosing the shiekh's name

```python
shiekh = tk.StringVar()
shiekh.set("الحصري")

drop = tk.OptionMenu(root, shiekh, "السديس", "عبدالباسط عبدالصمد", "العفاسي", "محمد جبريل", "محمد أيوب", "ماهر المعيقلي", "الحصري" )
drop.pack()
```

a button for submitting the data for the text api called 'بحث' 'search' the button is connected to a function that manges all the errors and displays an error message 
```python
btn_input = tk.Button(root, height=1, width=10, text="بحث", command=get_text)
btn_input.pack()
```

there is a function called in the button function that takes as input the ayah's and surah's numbers and returns the ayah's text using the api
```python
def get_ayah_text(surah_num, ayah_num):
    try:
        response = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key={surah_num}%3A{ayah_num}")
        return response.json()["verses"][0]["text_uthmani"]
    except IndexError:
        raise IndexError
```

there is also a button for playing the audio of the ayah called 'سماع' 'hear' the button is connected to a function that manges all the errors and displays an error message 
```python
btn_audio = tk.Button(root, height=1, width=10, text="سماع", command=get_audio)
btn_audio.pack()
```

there is a function called in the button function that takes as input the ayah's and surah's numbers and the shiekh's name and returns the ayah's audio link using the api to be played 
```python
def get_ayah_audio(surah_num, ayah_num, shiekh):
    try:
        response_audio = requests.get(f"http://api.alquran.cloud/v1/ayah/{surah_num}:{ayah_num}/{shiekh}")
        return response_audio.json()["data"]["audio"]
    except TypeError:
        raise TypeError
```

the last function is a translator that takes a arabic name of the shiekh's and returns the corresponding Id
```python
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
```       







 


