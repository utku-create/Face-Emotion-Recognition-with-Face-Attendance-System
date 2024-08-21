#Importlarım
import os.path
import subprocess
import tkinter as tk
from deepface import DeepFace
import matplotlib.pyplot as plt

import cv2
import util
from PIL import Image, ImageTk
import datetime



class App:

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(self.main_window, 'Giriş', 'green', self.login)
        self.login_button_main_window.place(x=775, y=300)


        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Kendini Tanıt',
                                                            'gray', self.register_new_user , fg='black')

        self.register_new_user_button_main_window.place(x=775, y=400)


        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10,y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.text_main_window = tk.Label(self.main_window, text="Duygu Durum Analizi", fg="darkgray", font=("Times New Roman", 35))
        self.text_main_window.place(x=730, y=20)

        self.text_main_window_alttaki = tk.Label(self.main_window, text="Lütfen Duygu Durumu Analiz Programının\nçalışabilmesi için 'Kendini Tanıt',\nardından Giriş Yap:", fg="darkgray",
                                         font=("Times New Roman", 16))
        self.text_main_window_alttaki.place(x=750, y=120)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def analyze_emotion(self, image_array): #duygu durum analizi kısmı

        img_rgb = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
        analysis = DeepFace.analyze(img_rgb, actions=['emotion'], enforce_detection=False)

        if isinstance(analysis, list):
            analysis = analysis[0]

        dominant_emotion = analysis['dominant_emotion']
        print("Duygu Analizi Sonuçları:", dominant_emotion)

        plt.imshow(img_rgb)
        plt.title(f"Duygu: {dominant_emotion}")
        plt.axis('off')
        plt.show()

        return dominant_emotion

    def login(self):  #kullanıcı giriş kısmı
        unknown_img_path = './.tmp.jpg'
        photo = self.most_recent_capture_arr
        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
        output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))

        os.remove(unknown_img_path)
        name = output.split(',')[1][:-5]
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Tekrar Dene!', 'Tekrar Dene. Ya seni tanıyamadım ya da kayıt olmadın!')
        else:
            util.msg_box('Giriş Başarılı!', 'Seni tanıdım {}!'.format(name))
            dominant_emotion = self.analyze_emotion(photo) #duygu durum analizi


            # Log dosyasına ismi, duygu durumunu ve giriş tarihini yaz
            with open(self.log_path, 'a') as f:
                f.write('{}, {}, {}\n'.format(name, dominant_emotion, datetime.datetime.now()))
                f.close()

    def register_new_user(self): #yeni kullanıcı tanımlaması
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Kabul Et', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Tekrar Dene', 'red',
                                                                      self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)


        self.add_image_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,"Lütfen, \nisim giriniz:")
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_image_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)), self.register_new_user_capture)

        util.msg_box('Başarılı!', 'Kullanıcı başarılı bir şekilde kayıt edildi!')
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
