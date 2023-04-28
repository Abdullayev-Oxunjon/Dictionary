whil=input("\nO'zbekcha-Inglizcha kug'at kerakmi ?\nKerak bo'lsa\nHa"
           "  \nAks holda\nYo'q\n>>>").lower()
s=0
while(whil.startswith('ha')):
    til=input("\n● Quyidagi so'zlardan qaysi so'zning ingliz tilidagi tarjimasini bilmoqchisiz"
          " ?\n\n ● avtomobil\t  ● olma\n ● maktab\t      "
          "● shahar\n ● davlat\t      ● til\n ● salom\t      ● apelsin\n ● aka\t          "
          "● uka\n ● opa\t          ● singil\n ● uy\t          ● quti\n ● kitob\t      ● xona\n\n>>>>> ").upper()
    lugat = {
        "AVTOMOBIL":{
        "key":"car"
    },
    "OLMA":{
        "key":"apple"
    },
    "MAKTAB":{
        "key":"school"
    },
    "SHAHAR":{
        "key":"city"
    },
    "DAVLAT":{
        "key":"country"
    },
    "APELSIN":{
        "key":"orange"
    },
    "SALOM":{
        "key":"hello"
    },
    "TIL":{
        "key":"language"
    },
    "UY":{
        "key":"home"
    },
    "AKA":{
        "key":"brother"
    },
    "UKA": {
        "key": "brother"
    },
    "OPA": {
        "key": "sister"
    },
    "SINGIL": {
        "key": "sister"
    },
    "QUTI":{
        "key":"box"
    },
    "KITOB": {
            "key": "book"
        },
    "XONA": {
            "key": "room"
        }

}
    javob = lugat.get(til, False)
    if javob:
        print("---------------------------------------")
        print("\nInglizcha tarjimasi - ",'●', javob["key"].title())
        s+=1
        print("\n-------------------------------------")
    else:
        print("Lug'atimizda bunday so'z tarjimasi yo'q !")

    bos=input("\nYana boshqa so'zning tarjimasini bilmoqchimisiz ?\n"
              "Bilmoqchi bo'lsangiz\nHa\naks holda\nYo'q\n>>>  ").lower()
    if bos=="yo'q":
        print("Siz dasturni tugatdingiz")
        print(f"● {s} ta so'zni google translate ga kiritdingiz ")
        muammo=input("\n\nTarjimalar borasida muammo bormi ? \nMuammo bo'lsa\nHa\nAks holda\nYo'q\n>>>>").lower()
        if muammo=="ha":
            print("\n● Xurmatli foydalanuvchi dasturda muammo bo'lishi mumkin emas,\n"
                  "Agarda shunda ham muammo bo'lsa hozir qo'limdan kelgani shu.\n"
                  "Nasib bo'lsa kelajakda katta proyektlarimda bu muammolar bo'lmaydi.\n\n")
            print("-------------------------------------------------------------------------")
            break
        elif muammo=="yo'q":
            print("\n ● Bizning dasturimizda foydalanganligingiz uchun rahmat !!!")
            break
        else:
            print("Ha ● Yo'q so'rovlaridan birini kiritmadingiz ! ")
            break


    elif bos=="ha":
        pass
    else:
        print("Siz ha yoki yo'q so'rovlaridan birini tanlamadigiz ! ")
        break

else:
    print("Siz HA so'rovini kiritmadingiz va dasturni tugatdingiz !")