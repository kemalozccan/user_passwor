user = "admin"
password = "154958"

a = 3
while True:
    if a == 0:
        print("Üst üste 3 kez hatalı bilgi girdiniz. Program sonlandı.")
        break
    user1 = input("Kullanıcı adınızı giriniz :")
    if user == user1:
        password1 = input("Şifrenizi giriniz :")
        if password == password1:
            print("Giriş Başarılı.")
            print(f"Hoş Geldiniz: {user1}")
            break
        else:
            a -= 1
            print(f"Şifre hatalıdır. {a} Hakkınız kaldı. Tekrar deneyiniz. \n")
    else:
        a -= 1
        print(f"Kullanıcı adı hatalıdır. {a} Hakkınız kaldı. Tekrar deneyiniz. \n")
