#Face Emotion Recognition with Face Attendance System

##İşleyiş:
  1- main.py dosyasını çalıştırdığımızda klasörümüze "db" isimli bir klasör oluşturacak. Eğer kayıt etmeden Giriş yapmak isterseniz database'de olmayacağınız için kayıt olmanızı isteyecek.
  2- Kayıt için sizin o anlık net çekilmiş bir fotoğrafınızı alacak ve isminizi girmenizi isteyecek. Face Recognition motorunun çalışma prensibi nedeniyle .jpg uzantılı fotoğrafınıza adınızı kaydedecek ve daha
  sonrasında sizi bu isimle tanıyacak.
  3- İsminizi girip kayıt olduktan sonra Giriş yaptığınızda sizi tanıyacak ve girişinize onay verecek.
  4- Girişten sonra sizin girişte verdiğiniz yüz duygu durumunun analizini yaparak ekrana bunu dönderecek. 
  5- Eğer girişte fotoğraf çekilirken yüzünüz görünmez, yüzünüzün önüne bir engel koyarsanız sizi tanıyamayacak ve uyarı döndürecektir bu yüzden yüzünüz gözükmelidir. 
  6- Tüm bu girişler "log.txt" metin dosyasına "İSİM, DUYGU DURUMU, O ANKİ TARİH VE SAAT" formatında kaydedilmekte ve tutulmaktadır. bknz: "utku, happy, 2024-08-21 15:23:22.539722" gibi.
 
##Açıklama:
  - Projede bir "main.py" dosyası -bu çalışan kodun bulunduğu python dosyası-, bir "util.py" dosyası -GUI için yapılan temel tasarımların bulunduğu python dosyası- bulunmaktadır.
  - "requirements.txt" ve "requirements_windows.txt" dosyalarını bilgisayarınıza kurmalısınız.

##Kullanılan Python Versiyonu ve Kütüphaneler:
  -Python 3.8 
  -datetime
  -PIL
  -util
  -cv2
  -matplotlib
  -deepface(tensorflow, keras...)
  -tkinter
  -cmake
  -dlib
  -face_recognition
  -scikit_learn
  -retina_face
  -numpy
   ...

   ##Uygulamadan Görüntüler:

  ###Uygulama Açıldığında:
  ![image](https://github.com/user-attachments/assets/f3cf06fa-c8dd-4591-8aa7-951e0b236459)
  
  ###Kişi db'ye kayıt olmadığında:
  ![image](https://github.com/user-attachments/assets/a197c4a0-6bbe-4257-a977-903cfc05e164)
  
  ###Kişiyi database'ye kayıt ederken:
    1- ![image](https://github.com/user-attachments/assets/9d1c1941-4806-45dc-a904-e0f061109440)
    2- ![image](https://github.com/user-attachments/assets/0167197f-edf2-4aab-8f12-fb9d91284035)
    
  ###Kayıt ettiken sonra giriş yapıyoruz:
    1- ![image](https://github.com/user-attachments/assets/887c8bf4-7a9f-4100-b5a4-4fa9b60bbdaf)
    2- ![image](https://github.com/user-attachments/assets/c43e8366-05d4-4cc3-9833-37908cc3edc0)

  ###Farklı bir duygu durumu için tekrar giriş yapıyoruz:
    1- ![image](https://github.com/user-attachments/assets/360a34fc-e642-416a-9e9b-e0df49477c43)
    2- ![image](https://github.com/user-attachments/assets/632f8078-0daf-47a8-aee2-ca220864b454)

  ###Bu da girişler sonrasındaki log.txt metin dosyası:
  ![image](https://github.com/user-attachments/assets/cd17b9aa-f1ec-4050-ab02-3fbf2142d3f8)



##Kullandığım kaynaklar:

- https://github.com/computervisioneng/face-attendance-system?tab=readme-ov-file
- https://medium.com/@hakkitoklu/python-ile-yüz-tanıma-uygulaması-8dc4e4bd8fcf
- https://docs.opencv.org/4.3.0/
- https://keras.io/
- https://numpy.org/doc/1.18/
- https://www.tensorflow.org/api_docs/python/


