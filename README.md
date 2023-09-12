Nama: Alma Laras Bestari  
NPM: 2206082303  
Kelas: PBP E  

# Memory Bouquet

[memory-bouquet.adaptable.app/main/](https://memory-bouquet.adaptable.app/main/)
---

# Tugas 2 Checklist
Checklist digunakan juga untuk menjawab pertanyaan pertama.
- [x] Membuat sebuah proyek Django baru.

    Pertama saya membuat direktori baru bernama ```memory_bouquet``` karena ini akan menjadi nama dari aplikasi saya. Setelah itu saya membuat virtual enviroment dan mengaktifkan virtual enviroment tersebut dengan menjalankan perintah

    ```
    python3 -m venv env
    ```
    ```
    source env/bin/activate
    ```

    Sesudah itu, saya membuat ```requirements.txt``` dengan menambahkan dependencies ini

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

    dan kemudian menjalankan perintah  ```pip install -r requirements.txt``` dilanjutkan dengan  ```django-admin startproject memory_bouquet .``` untuk membuat proyek baru Django saya.

    Tidak lupa untuk menambahkan ```*``` pada ```ALLOWED_HOSTS``` pada ```settings.py``` dan membuat ```.gitignore```.
- [x] Membuat aplikasi dengan nama ```main``` pada proyek tersebut.
    Saya menjalakan perintah ```python manage.py startapp main```. Setelah itu, saya menambahkan aplikasi ```main``` ke ```memory_bouquet``` dengan menambahkan ```main``` dalam ```settings.py```

    ```
    INSTALLED_APPS = [
    ...,
    "main",
    ...
    ]
    ```

    Sesudah itu, saya membuat direktori ```template``` dalam direktori ```main``` dan membuat file ```main.html```.
- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi ```main```.

    Saya membuka ```urls.py``` pada direktori ```memory_bouquet```, impor fungsi ```include```, dan menambahkan ```path('main/', include('main.urls')),``` pada ```urlpatterns``` untuk melakukan konfigurasi.
- [x] Membuat model pada aplikasi ```main``` dengan nama ```Item``` dan memiliki atribut wajib sebagai berikut.
    - ```name``` sebagai nama *item* dengan tipe ```CharField```.
    - ```amount``` sebagai jumlah *item* dengan tipe ```IntegerField```.
    - ```description``` sebagai deskripsi *item* dengan tipe ```TextField```.

    Pada ```models.py```, saya menambahkan

    ```
    class Flower(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
    ```

    Setelah itu melakukan migrasi model dengan ```python manage.py makemigrations```, dilanjutkan dnegan ```python manage.py migrate```
- [x] Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    Saya memodifikasi file ```views.py``` untuk menerapkan MTV
    
    ```
    from django.shortcuts import render

    def show_main(request):
        context = {
            'name': 'Alma Laras Bestari',
            'npm': '2206082303',
            'class': 'PBP E',
            'application': 'Memory Bouquet',
        }

        return render(request, "main.html", context)
    ```

- [x] Membuat sebuah *routing* pada ```urls.py``` aplikasi ```main``` untuk memetakan fungsi yang telah dibuat pada ```views.py```.

    Pada ```urls.py``` di direktori ```main```, saya menambahkan

    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Saya melakukan git add, commit, push. Setelah itu membuka website Adaptable dan memilih ```create new app```, ```Connect an Existing Repository```, memilih repo ```memory-bouquet```.

    Setelah itu memilih ```Python App Template```, ```PostgreSQL```, menambahkan ```python manage.py migrate && gunicorn memory_bouquet.wsgi``` pada ```start command```, dan memilih opsi ```HTTP Listener on PORT```. Setelah itu, Memory Bouquet siap untuk di deploy.
- [x] Membuat sebuah ```README.md``` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

        **Jawaban:** Telah dijelaskan diatas sesuai urutan checklist
    - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py,``` dan berkas ```html```.

        **Jawaban**
        ![Bagan Django](https://cdn.discordapp.com/attachments/1006390336299483188/1151226601573449779/pbp.png)

        Web browser menerima permintaan HTTP aplikasi dari *client*. Setelah itu, ```urls.py``` melakukan mapping dan meneruskan permintaan HTTP ke ```views.py``` . Kemudian, ```views.py``` akan mengakses data yang dibutuhkan melalui ```models.py```. Data tersebut kemudian ditampilkan dengan ```template``` yang sesuai. HTTP request ini akan dikembalikan oleh ```view``` menjadi HTTP response berupa HTML page.

    - Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    
        **Jawaban:** *Virtual enviroment* digunakan untuk memisahkan *dependencies* antara proyek-proyek yang berbeda. Django dapat dijalankan tanpa *virtual enviroment* tetapi karena *dependencies* tidak dipisahkan, maka terdapat kemungkinan terjadinya konflik antar proyek. Penggunaan *virtual enviroment* dalam membuat aplikasi web berbasis Django akan memudahkan pengelolaan pengembangan aplikasi.
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    
        **Jawaban:**
        - MVC (Model-View-Controller)
            Memisahkan kode menjadi tiga bagian, yaitu Model, View, dan Controller. Model menyimpan data aplikasi dan tidak memiliki informasi mengenai interface aplikasi, View mengatur UI dari aplikasi, dan Controller menjadi jembatan antara model dan view dan mengelola permintaan pengguna.
        - MVT (Model-View-Template)
            Memisahkan kode menjadi tiga bagian, yaitu Model, View, dan Template. Model dan View memiliki peran yang sama seperti MVC. Template ngatur tampilan HTML dan mengatur cara data dari Model ditampilkan dalam View. Model ini adalah model yang digunakan dalam Django
        - MVVM (Model-View-ViewModel)
            Memisahkan kode menjadi tiga bagian, yaitu Model, View, dan ViewModel. Model dan View memiliki peran yang sama seperti MVC dan MVVM. ViewModel berperan sebagai perantara antara Model dan View. 

        Perbedaan
        | MVC         | MVT         | MVVM        |     
        | ----------- | ----------- | ----------- |
        | View tidak memiliki informasi kemengenai Controller      | View menyimpan referensi ke Template | View tidak memiliki referensi ke Model. Viewmodel yang menghubungkan View dan Model.       |

        [Referensi MVC MVVM](https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/)

        [Referensi MVC MVT](https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/)

