Nama: Alma Laras Bestari  
NPM: 2206082303  
Kelas: PBP E  

# Memory Bouquet

[memory-bouquet.adaptable.app/main/](https://memory-bouquet.adaptable.app/main/)
---
# Directory
For easy access
-  [Tugas 2](#tugas-2)
-  [Tugas 3](#tugas-3)

# Tugas 2
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

    ```python
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

    ```python
    class Flower(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
    ```

    Setelah itu melakukan migrasi model dengan ```python manage.py makemigrations```, dilanjutkan dnegan ```python manage.py migrate```
- [x] Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    Saya memodifikasi file ```views.py``` untuk menerapkan MTV
    
    ```python
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

    ```python
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

    ## BONUS
    [Referensi Django Testing Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)

    [Dokumentasi Django](https://docs.djangoproject.com/en/4.2/topics/testing/overview/)

    Melalui referensi yang diatas, saya menambahkan implementasi test model seperti ini di ```tests.py```

    ```python
    class FlowerModelTest(TestCase):
        @classmethod
        def setUpTestData(cls):
            # Set up non-modified objects used by all test methods
            Flower.objects.create(name='Lily', amount='4')

        def test_name_label(self):
            flower = Flower.objects.get(id=1)
            field_label = flower._meta.get_field('name').verbose_name
            self.assertEqual(field_label, 'name')

        def test_amount_label(self):
            flower = Flower.objects.get(id=1)
            field_label = flower._meta.get_field('amount').verbose_name
            self.assertEqual(field_label, 'amount')
    ```

    ```setUpTestData()``` membuat object Flower yang akan digunakan pada testcase. Field tests tersebut akan mengetest apakah value dari field label dan apakah character size sesuai.

# Tugas 3
Checklist digunakan juga untuk menjawab pertanyaan terakhir.
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

    Sebelum itu saya mengatur routing dari ```main/``` menjadi ```/```. Setelah itu saya membuat ```forms.py``` dan membuat kode yang sesuai sehingga input form dapat menjadi sebuah objek ```Flower```
    ```python
    from django.forms import ModelForm
    from main.models import Flower

    class FlowerForm(ModelForm):
        class Meta:
            model = Flower
            fields = ["name", "amount", "description"]
    ```

    Setelah itu saya menambahkan beberapa *import* pada ```views.py```
    ```python
    ...
    from django.http import HttpResponseRedirect
    from main.forms import FlowerForm
    from django.urls import reverse
    from main.models import Flower
    ...
    ```

    Sesudah itu, saya membuat fungsi yang bernama ```create_entry()``` yang mengambil parameter ```request``` sehingga entry dapat bertambah secara otomatis jika form disubmit. Saya juga menambahkan ```flowers = Flower.objects.all()``` pada fungsi  ```show_main```  dan menambahkan
    ```python
    context = {
        ...
        'flowers': flowers,
        ...
    }
    ```
    sehingga data dari model dapat dikirimkan ke tampilan.

    Fungsi ```create_entry``` yang sebelumnya telah dibuat harus dilakukan routing URL sehingga pada ```urls.py``` saya import fungsi ```create_entry``` dan menambahkan path url pada ```urlpatterns```
    ```python
    path('create-entry', create_entry, name='create_entry'),
    ```

    Saya selanjutnya membuat berkas HTML baru dengan nama ```create_entry.html``` pada direktori ```main/templates``` sehingga dapat menginput form dengan user interface.
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

    Setelah itu saya memodifikasi ```main.html``` dengan menambahkan
    ```html
    <table class="table-container">
        <tr>
            <th style="width:25%">Name</th>
            <th style="width:15%">Amount</th>
            <th style="width:45%">Description</th>
            <th style="width:15%">Date Added</th>
        </tr>
    
        {% for flower in flowers %}
            <tr>
                <td>{{ flower.name }}</td>
                <td>{{ flower.amount }}</td>
                <td>{{ flower.description }}</td>
                <td>{{ flower.date_added }}</td>
            </tr>
        {% endfor %}
    </table>
    ```

- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    Berikut fungsi views ```show_main``` yang akan me-*render* tampilan HTML (```main.html```) yang sebelumnya sudah dibuat.
    ```python
    def show_main(request):
    flowers = Flower.objects.all()

    total_entries = len(flowers)
    if (total_entries > 1):
        entry_messages = f'You have a total of {total_entries} entries'
    else:
        entry_messages = f'You have a total of {total_entries} entry'

    context = {
        'name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
        'flowers': flowers,
        'total_entry_message': entry_messages,
    }

    return render(request, "main.html", context)
    ```
    Saya juga membuat fungsi-fungsi untuk mengembalikan data-data dalam bentuk XML, JSON, XML by ID, dan JSON by ID dengan menambahkan kode berikut pada ```views.py```

    ```python
    def show_xml(request):
        data = Flower.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Flower.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Flower.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Flower.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    variabel ```data``` di dalam fungsi tersebut berguna untuk menyimpan hasil *query*

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    Saya menambahkan import pada urls.py sesuai fungsi yang telah dibuat pada ```views.py``` seperti ini
    ```python
    from main.views import show_main, create_entry, show_xml, show_json, show_xml_by_id, show_json_by_id 
    ```
    dan menambahkan path URL yang sesuai ke ```urlpatterns```

    ```python
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-entry', create_entry, name='create_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'), 
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
    - Apa perbedaan antara form POST dan form GET dalam Django?

        **Jawaban:** Pada Django, terdapat dua method HTTP request yaitu POST dan GET. Kedua method tersebut memiliki perbedaan dan kegunaan berbeda. POST digunakan untuk request yang membuat perubahan pada database. Sedangkan GET digunakan jika tidak mengubah data dalam database.

        Jika kita menggunakan GET, maka input user akan terlihat dalam URL sehingga ini tidak aman untuk data sensitif seperti username dan password. Sedangkan POST melakukan enkripsi pada data tersebut sehingga input user tidak terlihat dalam URL. Selain itu, GET hanya dapat berupa string data, sedangkan method POST dapat berupa string numeric, binary, etc.

        References:

        [Dokumentasi Django - Working with forms](https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST%20are%20typically,the%20state%20of%20the%20system.)

        [Quora - What is the key difference between GET and POST in Django?](https://www.quora.com/What-is-the-key-difference-between-GET-and-POST-in-Django)
    - Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
        
        **Jawaban:**
        - XML

            XML (eXtensible Markup Language) dapat memproses data type dan structure yang kompleks. XML digunakan untuk mengirim data antara aplikasi. XML didesign menjadi *self-descriptive* sehingga manusia dapat mengerti informasi yang disampaikan oleh data tersebut. XML berisi informasi yang dibungkus di dalam tag.
        - JSON

            JSON (JavaScript Object Notation) sangat mudah untuk dimengerti karena sintaksnya sederhana. JSON juga digunakan untuk mengirim data antara aplikasi. Datanya disimpan dapat bentuk key dan value. Format JSON berbentuk teks membuatnya mudah untuk dibaca.

        - HTML

            HTML (HyperText Markup Language) adalah bahasa markup yang didesign untuk ditampilkan pada browser web. HTML lebih digunakan untuk membuat halaman web yang dapat dilihat oleh pengguna melalui browser web.


    - Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

        **Jawaban:** JSON dapat di parsed oleh standard JavaScript function. JSON mudah dibaca oleh manusia, lebih cepat, dan lebih efisien untuk *web development*.
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

        **Jawaban:** Telah dijelaskan diatas dengan checklist.
- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
    - HTML

        ![Postman HTML](https://media.discordapp.net/attachments/1153279137599995925/1153279235339849878/Screen_Shot_2023-09-18_at_17.38.01.png?width=1762&height=1102)
    - XML

        ![Postman XML](https://media.discordapp.net/attachments/1153279137599995925/1153279235675402350/Screen_Shot_2023-09-18_at_17.38.10.png?width=1762&height=1102)

    - JSON

        ![Postman JSON](https://media.discordapp.net/attachments/1153279137599995925/1153279235960602674/Screen_Shot_2023-09-18_at_17.38.19.png?width=1762&height=1102)
    - XML by ID

        ![Postman XML by ID](https://media.discordapp.net/attachments/1153279137599995925/1153279236627509279/Screen_Shot_2023-09-18_at_17.39.16.png?width=1762&height=1102)
    - JSON by ID

        ![Postman JSON by ID](https://media.discordapp.net/attachments/1153279137599995925/1153279236266790963/Screen_Shot_2023-09-18_at_17.39.03.png?width=1762&height=1102)


- [x] Melakukan add-commit-push ke GitHub.

    ## BONUS
    Saya mengimplementasi bonus dengan menambahkan kode berikut pada ```views.py```
    ```python
    def show_main(request):
    ...
    total_entries = len(flowers)
    if (total_entries > 1):
        entry_messages = f'You have a total of {total_entries} entries'
    else:
        entry_messages = f'You have a total of {total_entries} entry'
    ...
    ```
    dan pada dictionary ```context``` saya juga menambahkan potongan kode berikut
    ```python
        context = {
        ...
        'total_entry_message': entry_messages,
        ...
    }
    ```

    Agar tampilannya dapat terlihat, pada ```main.html``` saya menambahkan kode berikut
    ```html
    ...
    <p class="total-entry">{{ total_entry_message}}</p>
    ...
    ```

