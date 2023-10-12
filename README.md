Nama: Alma Laras Bestari  
NPM: 2206082303  
Kelas: PBP E  

# Memory Bouquet

Should've been successfully deployed here [alma-laras-tugas.pbp.cs.ui.ac.id/](http://dimas-herjunodarpito-tugas.pbp.cs.ui.ac.id/)
---
# Directory
For easy access
-  [Tugas 2](#tugas-2)
-  [Tugas 3](#tugas-3)
-  [Tugas 4](#tugas-4)
-  [Tugas 5](#tugas-5)
-  [Tugas 6](#tugas-6)

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

----
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

----
# Tugas 4
Checklist digunakan juga untuk menjawab pertanyaan terakhir.

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    Pertama, saya import fungsi-fungsi yang dibutuhkan

    ```python
    from django.contrib.auth import authenticate, login
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```

    Setelah itu, saya membuat beberapa fungsi pada ```views.py```, yaitu fungsi ```register```, ```login_user```, dan ```logout_user``` seperti berikut

    ```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {
            ...
        }
    return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {
            ...
        }
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

    Kemudian pada ```urls.py```, saya mengimport fungsi yang telah saya buat dan menambahkan **path url* kke ```urlpatterns```

    ```python
    ...
    from main.views import register, login_user, logout_user
    ...

    app_name = 'main'

    urlpatterns = [
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        ...
    ]

    ```

    Agar halaman utama aplikasi hanya dapat diakses oleh pengguna yang logged in, saya menambahkan kode ```@login_required(login_url='/login')``` diatas fungsi ```show_main```. Selain itu saya juga membuat file html untuk masing-masing fungsi.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    Saya membuat dua akun yaitu alma dan mayaa dan menambahkan tiga dummy model. Namun data entry bunga mereka tercampur karena belum dibedakan model entry antaruser.

    ![alma](https://media.discordapp.net/attachments/1006390336299483188/1156393510510010389/Screen_Shot_2023-09-27_at_07.54.36.png?ex=6514cee1&is=65137d61&hm=f56b0affeb5c79e5651cdc605feb1c02fa34b8079984b16cb084d7c51519649c&=&width=1284&height=828)

    ![mayaa](https://media.discordapp.net/attachments/1006390336299483188/1156393510233190410/Screen_Shot_2023-09-27_at_07.54.28.png?ex=6514cee1&is=65137d61&hm=211d89df9148752ab0f1fe776ae63c40a559a6b68474875d7aaceecc1bf61411&=&width=1300&height=784)

    ![Dummy Data](https://media.discordapp.net/attachments/1006390336299483188/1156393171530551397/Screen_Shot_2023-09-27_at_01.35.39.png?ex=6514ce90&is=65137d10&hm=4bcd1ed0ceb14bb925dbeb4678f82485c421e721921304ea3045b205963ab72e&=&width=1550&height=968)


    Jika semua sudah diimplementasikan seperti ini:

    (data berbeda karena mencoba fitur delete)
    ![alma implementasi](https://cdn.discordapp.com/attachments/1006390336299483188/1156436627963523132/Screen_Shot_2023-09-27_at_10.43.48.png?ex=6514f709&is=6513a589&hm=ee4ec8ef5fedd5a90a29116d48fd430d862139ce394f47643f1bf938b76e3200&)
    ![mayaa Implementasi](https://media.discordapp.net/attachments/1006390336299483188/1156436628336812092/Screen_Shot_2023-09-27_at_10.45.52.png?ex=6514f709&is=6513a589&hm=43dfcceb5728355c5ba7d7c93f71c48ac8d7553fa5f1653161ef421faf4659ba&=&width=1550&height=968)

- [x] Menghubungkan model Item dengan User.

    Agar data model antaruser tidak tercampur, kita akan menghubungkan model Flower dengan User. Pada ```models.py``` kita tambahkam ```from django.contrib.auth.models import User```

    Setelah itu saya tambahkan kode ini sehingga User dapat terhubung dengan Model Flower
    ```python
    class Flower(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

    Pada fungsi ```create_entry``` di ```views.py```, saya mengubah fungsinya sedikit untuk menandakan bahwa objek tersebut dimiliki oleh user yang sedang login.

    ```python
    def create_entry(request):
    form = FlowerForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        ...
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```

    Setelah itu saya menjalankan ```python manage.py makemigrations``` dan ```python manage.py migrate```

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    Agar detail informasi pengguna seperti nama user muncul pada tampilan layar dan menampilkan hanya Flower miliknya saja, saya mengubah sebagian fungsi ```show_main``` menjadi seperti ini

    ```python
    def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        ...
    ...
    ```

    Untuk menerapkan cookies, saya pertama import fungsi yang akan digunakan pada ```views.py```
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```

    Setelah itu saya mengubah kode sedikit di fungsi ```login_user``` dan ```logout_user``` agar User dapat melihat kapan terakhir melakukan *login*. Terdapat pitongan kode ```response.delete_cookie('last_login')``` pada fungsi ```logout_user``` agar saat logout cookies user dihapus.

    ```python

    def login_user(request):
            ...
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            ...
        }
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

    Pada fungsi ```show_main``` saya menambahkan key value baru yaitu ```last_login``` untuk menambahkan informasi cookies

    ```python
       context = {
        ...
        'last_login': request.COOKIES['last_login'],
    }
    ```

    Pada ```main.html``` saya menambahkan kode berikut agar informasinya dapat dilihat oleh User.

    ```python
    ...
        <div class="container">
        <div class ="greetings">
            <h1>Welcome {{ name }} 𓇢𓆸</h1>
            <span>Sesi terakhir login: {{ last_login }}</span>
        </div>
    ...
    ```

    ![Hasil Akhir](https://media.discordapp.net/attachments/1006390336299483188/1156404363871408169/Screen_Shot_2023-09-27_at_08.37.48.png?ex=6514d8fd&is=6513877d&hm=191f802947449cc86863fc940f594354895d556657a909d2a1ddc125024a30e8&=&width=1550&height=968)

- [ ]Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [x] Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
        
        UserCreationForm merupakan build-in module yang diturunkan dari ModelForm dari Django. UserCreationForm memudahkan proses pembuatan User baru.
        
        - Kelebihan: UserCreationForm memungkinkan penggunaan form new User di situs web tanpa harus mengembangkan form dari awal. Selain itu, Django juga menyediakan sistem otentikasi yang terintegrasi, sehingga User yang terdaftar dapat dengan mudah disimpan dan dikelola.

        - Kekurangan: Fieldnya terbatas. Hanya terdapat username, password, dan password confirmation.

    - [x] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

        Perbedaan
        | Autentikasi         | Otorisasi         |   
        | ----------- | ----------- |
        | Dalam django, autentikasi adalah proses/langkah verifikasi identitas User yang masuk aplikasi | Otorisasi lebih berfokus pada pembatasan hak pengguna saat menggunakan aplikasi |
        | Autentikasi dalam Django melibatkan pemeriksaan kredensial, seperti username dan password. | Berhubungan dengan hak akses user. Dalam Django User dapat diberi role yang menentukan hak akses mereka (seperti superuser)|

        Autentikasi dan otoritasi penting untuk menjaga keamanan dalam aplikasi. Mereka berdua bekerja sama untuk melindungi privasi User dan mencegah akses tidak sah.
    
    - [x] Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna

        Cookies adalah data yang disimpan pada perangkat user (*client side*) ketika mereka mengunjungi sebuah situs web (pada aplikasi ini datanya dihapus setelah logout). Cookies memungkinkan server Django untuk menyimpan dan mengambil informasi yang diperlukan pada saat permintaan User selanjutnya.
        
        Django menggunakan cookies untuk menjaga status User, mengidentifikasi User yang terautentikasi, dan menyimpan informasi penting selama sesi user/pengguna. Ketika User melakukan proses login, Django akan membuat *cookies session* khusus untuk user tersebut. *Session cookies* ini digunakan oleh Django untuk menyimpan data sesi yang telah diisi oleh user, yang mencakup berbagai informasi seperti nama user dan preferensi yang mereka pilih, serta Django juag dapat mengelola data tersebut sesuai ID *session cookies*.


    - [x] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

        Penggunaan cookies dalam pengembangan web dapat menjadi aman, namun keamanannya tidak ada secara default dan sangat tergantung pada bagaimana cookies diimplementasikan. Berikut risiko yang harus diwapadai: 

        1. Kebocoran Data: Cookies dapat menyimpan informasi sensitif user seperti otentikasi. Penyerang dapat mencuri data tersebut jika cookies tidak aman
        
        2. Cross-Site Scripting (XSS): Cookies dapat menjadi target serangan XSS jika data yang disimpan dalam cookies tidak dijalankan melalui validasi yang baik. Ini memungkinkan penyerang untuk menyisipkan script jahat yang dapat mencuri atau memanipulasi data cookies user
        
        3. Man in the Middle (MitM) Attacks: Penyerang dapat mencuri atau memodifikasi cookies yang tidak dienkripsi saat data dikirimkan dari server ke browser user
        
        4. Session Fixation: Penyerang dapat mencoba menetapkan ID sesi mereka sendiri kepada user dengan tujuan untuk mencuri sesi user yang telah diotentikasi

    - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Sudah dijelaskan diatas.

- [x]Melakukan add-commit-push ke GitHub.

    ## BONUS
    
    Untuk user dapat menambahkan dan mengurangkan serta delete entry yang sebelumnya sudah dibuat, saya menambahkan beberapa fungsi pada ```views.py```

    ```python
    def increment_flower_amount(request, pk_id):
    if request.method == 'POST':
        flower = Flower.objects.get(id=pk_id)
        flower.amount += 1
        flower.save()
    
    return redirect('main:show_main')

    def decrement_flower_amount(request, pk_id):
        if request.method == 'POST':
            flower = Flower.objects.get(id=pk_id)
            if flower.amount > 0:
                flower.amount -= 1
                flower.save()
        
        return redirect('main:show_main')

    def delete_flower(request, pk_id):
        if request.method == 'POST':
            flower = Flower.objects.get(id=pk_id)
            flower.delete()
        
        return redirect('main:show_main')
    ```

    Kemudian saya melakukan routing URL. Pada ```urls.py``` saya import fungsi-fungsi yang sebelumnya sudah saya buat dan menambahkan path url pada ```urlpatterns```

    ```python
    from main.views import increment_flower_amount, decrement_flower_amount, delete_flower

    app_name = 'main'

    urlpatterns = [
        ...
        path('int-flower/<int:pk_id>/', increment_flower_amount, name='inc_flower'),
        path('dec-flower/<int:pk_id>/', decrement_flower_amount, name='dec_flower'),
        path('del-flower/<int:pk_id>/', delete_flower, name='del_flower'),
        ...
    ```

    Setelah itu saya memodifikasi ```main.html``` dengan menambahkan button

    ```python
                <td>
                    <form action="{% url 'main:dec_flower' flower.id %}" method="POST">
                        {% csrf_token %}
                        <button class="inc-dec-button" type="submit">
                            -
                        </button>
                    </form>
                    {{ flower.amount }}
                    <form action="{% url 'main:inc_flower' flower.id %}" method="POST">
                        {% csrf_token %}
                        <button class="inc-dec-button" type="submit">
                            +
                        </button>
                    </form>
                </td>
                <td>{{ flower.description }}</td>
                <td>{{ flower.date_added }}</td>
                <td>
                    <form action="{% url 'main:del_flower' flower.id %}" method="POST">
                        {% csrf_token %}
                        <button class="del-button" type="submit">
                            <span>Delete</span>
                        </button>
                    </form>
                </td>
    ```
---
# Tugas 5

-  [X] Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

    - [X] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
    - [X] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
- [X] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

    - [X] Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

        1. Element Selector
        Element selector dapat mengubah properti untuk semua elemen dengan tag HTML yang sama. Ini berguna saat Anda ingin menerapkan membuat seragam pada semua elemen dengan tag yang sama. Element selector digunakan untuk mengatur properti dasar yang diterapkan pada semua elemen dengan tag yang sama.
        2. ID Selector
        ID selector digunakan untuk memilih elemen dengan ID unik dalam halaman web. Ini berguna ketika Anda ingin menerapkan modifikasi pada elemen tertentu yang memiliki ID unik. ID selector digunakan ketika perlu merujuk pada elemen tertentu dengan ID yang unik. ID bersifat unik di dalam halaman.
        3. Class selector dapat mengelompokkan elemen dengan karakteristik yang sama, seperti memberi mereka gaya seragam. Class selector adalah salah satu yang paling umum digunakan dalam CSS. Anda dapat menggunakannya untuk mengelompokkan elemen yang memiliki karakteristik yang sama, seperti tombol, menu, atau elemen lain yang harus tampil seragam. Ini juga sangat berguna untuk memisahkan struktur HTML dari styling. Class selector menggunakan format .[class_name]. Class selector digunakan untuk memilih semua elemen yang termasuk dalam atribut kelas tertentu.

    - [X] Jelaskan HTML5 Tag yang kamu ketahui.

        Berikut beberapa HTML5 Tag aku saya ketahui 
        1. ```<div>``` untuk membantu mengelompokkkan data pada suatu web page.
        2. ```<p>``` untuk merepresentasikan sebuah paragraf.
        3. ```<h1>``` sampai ```<h6>``` untuk merepresentasikan heading beserta prioritynya.
        4. ```<header>``` untuk merepresentasikan bagian header.
        5. ```<figure>``` untuk merepresentasikan bagian seld-contained flow content.
        6. ```<table>``` untuk menampilkan table.
        7. ```meter``` untuk merepresentasikan suatu besaran ukuran.
        8. ```<section>``` untuk merepresentasikan bagain generic.
        9. ```<footer>``` untuk merepresentasikan bagian footer.
        10. ```<keygen>``` untuk merepresentasikan kontrol keygen
        11. ```<nav>``` untuk menyatakan bagian navigasi.
        12. ```<progress>``` untuk menampilkan progress.
        13. ```<time> ``` untuk menampilkan waktu.
        14. ```<audio>``` untuk menyatakan audio file.
        15. ```<canvas>``` untuk merender dynamic bitmap seperti games atau graph.

    - [X] Jelaskan perbedaan antara margin dan padding.

        Margin mengatur jarak elemen tersebut antar elemen lain. Sedangkan padding mengatur jarak didalam elemen.

    - [X] Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

        Bootstrap dan Tailwind memiliki beberapa perbedaan walaupun keduanya merupkan framework CSS. Bootstrap lebih mudah untuk dipakai karena Bootstrap menyediakan komponen yang sudah jadi. Jika ingin melakukan banyak customisasi, dengan Tailwind akan lebih mudah. Bootstrap dapat digunakan jika kita ingin hasil yang cepat dan konsisten.

    - [X] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

        Saya menambahkan styling ini pada ```base.html```

        ``` css
                container {
            margin-left: 20px; 
            margin-right: 20px;
        }

        .header{
            width:100%; 
            background-color: #e285af;
            text-align: center;
            color: white;
            padding: 10px;
            border-bottom: 12px solid #73beb0;
        }

        .total-entry{
            font-size: 12px;
            text-align: center;
            margin: 20px;
        }

        .information{
            margin: 0px;
            font-size: 10px
        }

        .table-container {
            margin: 10px auto 20px auto;
            text-align: center;
        }

        .messages{
            text-align: center;
            display: inline-block;
            width: 20%;
            padding: 10px;
            margin: 0 auto;
            font-family: Verdana, sans-serif;
            background-color: #b5e1d9;
            font-size: 12px;
            display: block;
            list-style-type: none;
            border-radius: 4px;
        }

        .flower-input, .login, .register{
            margin: auto;
            padding: 10px;
            text-align: left;
            border-style: none;
        }

        .register {
            width: 45%;
        }

        .flower-input {
            width: 50%;
        }

        .login {
            width: 20%;;
        }

        .flower-input h1, .login h1, .register h1{
            font-size: 32px;
            text-align: center;
        }

        .flower-input label {
            font-size: 14px;
        }

        .login td, .login label, .register label{
            font-size: 12px;
        }

        .register label, .register th {
            vertical-align: top;
            text-align: left;
        }

        .login p, .register span {
            font-size: 12px;
        }

        .login p {
            text-align: center;
        }

        input[type=submit]{
            background-color: #73beb0; 
            border: none;
            font-family: Verdana, sans-serif;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            display: inline-block;
            font-size: 12px;
            text-align: left
        }

        input[type=submit]:hover {
            background-color: #3a5b7b;
        }

        .greetings {
            text-align: center;
        }

        .greetings h1{
            font-size: 24px;
            margin: 16px 10px 0px 10px;
        }

        .greetings span{
            font-size: 10px;
            font-family: Verdana, sans-serif;
            margin: 0px 10px 10px 10px;
        }

        .flower-table{
            text-align: center;
            width: 100%;
        }

        .flower-table table, .flower-table th, .flower-table td{
            margin: 10;
            padding: 10;
            border-collapse: collapse;
        }

        .flower-table th{
            color: white;
            border:1px solid #73beb0;
            background-color: #73beb0;
            border-style: outset;
            font-size: 16px;
        }

        .flower-table td{
            border:px solid #73beb0;
            border-style: inset;
            font-size: 12px;
        }

        .flower-table form {
            display: inline-block;
            margin: 0px 15px;
        }

        .inc-dec-button {
            padding: 2px 8px;
            width: 100%;
            max-width: 100%
        }

        .inc-dec-button:hover {
            background-color: #3a5b7b;
        }

        .del-button {
            background-color: #ffffff;
            color:#e43a6a;
            padding: 4px 8px;
            margin: 8px;
        }

        .del-button:hover {
            color: #6b0d20;
        }

        h1{
            margin: 10px;
            font-family: Georgia, serif;
            font-size: 50px;
        }

        h2{
            margin: 10px;
            font-family: Georgia, serif;
            font-size: 14px;
            letter-spacing: 3px;
        }

        p, table, th, td, li {
            font-family: Verdana, sans-serif;
        }

        button {
            background-color: #e285af; /* Green */
            border: none;
            font-family: Verdana, sans-serif;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            display: inline-block;
            font-size: 12px;
            text-align: left
        }

        a {
            display: inline-block
        }
        
        ```

- [X] Melakukan add-commit-push ke GitHub.

    ## BONUS 

    Menambahkan potongan kode ini sehingga jika berada pada iterasi terakhir warna berubah.

    ```html
    {% for flower in flowers %}
        <tr
        {% if forloop.last %}
        style='background-color:#d4eedd;'
        {% endif %}
        >
    ```
---
# Tugas 6
- Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    **Synchronous Programming**

    Pada ini, *task* (operasi) dieksekusi secara berurutan dan hanya satu *task* yang dapat dieksekusi. Task akan dieksekusi sesuai urutan ia muncul dalam code program kita. Ini berarti *task* lain harus menunggu *task* lainnya untuk selesai dieksekusi terlebih dahulu.

    **Asynchronous Programming**
    Kebalikannya dengan synchronous programming, pada asynchronous programming, *task* dieksekusi secara bersamaan sehingga *task*yang satu tidak harus menunggu *task* yang lain selesai sebelum menjalankan *task*-nya.

- Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    Event-driven programming sering digunakan pada penerapan JavaScript dan AJAX. Paradigma event-driven programming adalah sebuah paradigma dimana alur jalannya program didasarkan pada konsep "events" dari user. Events ini dapat berupa tindakan pengguna seperti mengklik tombol, mengisi formulir, ataupun scrolling. Ketika suatu acara terjadi, program akan merespons dan menjalankan fungsi tertentu yang telah ditetapkan sebelumnya. Paradigma ini memungkinkan pembangunan antarmuka pengguna (UI) yang interaktif dan responsif.

    Salah satu contoh penerapannya pada tugas ini adalah ketika user mengeklik tombol "Add Entry" pada modal untuk menambahkan entry bunga. Ketika tombol "Add Entry" diklik, JavaScript menggunakan event listener untuk mendeteksi event yang terjadi (button click). Ketika event tersebut terjadi, JavaScript akan menjalankan fungsi addFlower().

    ```javascript
    document.getElementById("button-add").onclick = addFlower;
    ```

- Jelaskan penerapan asynchronous programming pada AJAX.

    AJAX merupakan singkatan dari Asynchronous Javascript and XML. AJAX bukan sebuah *programming language* melainkan sebuah teknologi untuk pengembangan web yang memungkinkan aplikasi web untuk bekerja secara asynchronous.

    Dalam konteks AJAX, asynchronous programming memungkinkan permintaan data ke server web dan pemrosesan respons server tidak harus menunggu pemrosesan yang sedang berlangsung untuk selesai, sehingga halaman web tetap responsif. Beberapa penerapan asynchronous programming pada AJAX meliputi pertukaran data, yang memungkinkan pengiriman dan penerimaan data dari server tanpa harus me-*reload* keseluruhan halaman. AJAX memungkinkan Asynchronous Calls ke server web sehingga klien tidak perlu menunggu semua data.

    Contohnya pada tugas ini kita menggunakan fetch, async dan await untuk mengelola kode asynchronous.

- Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

    Dalam penggunaan AJAX, terdapat dua teknologi utama yang digunakan, yaitu Fetch API dan library jQuery.

    Fetch API adalah bagian bawaan dari JavaScript modern dan tidak memerlukan unduhan tambahan. Sedangkan jQuery butuh. Oleh karena hal tersebut, penggunaan fetch API akan lebih efisien dalam hal ukuran dan waktu memuat halaman karena tidak memerlukan perpustakaan eksternal. Selain itu, Fetch API menggunakan promise untuk pengelolaan tugas asinkron, yang membuat kode lebih mudah dibaca dan dikelola.

    Sedangkan jQuery memiliki ukurannya yang besar dan tidak semua fitur pastinya akan digunakan. Penggunaan jQuery juga dapat memperlambat waktu muat halaman. Namun, jQuery lebih cocok untuk browser lama. Selain itu, tersedia banyak plugin jQuery, termasuk yang berhubungan dengan dengan AJAX sehingga dapat memperluas fungsionalitasnya.

    *Overall*, menurut saya dalam masa modern ini, Fetch API lebih baik digunakan dibanding jQuery. Fetch API lebih baik dalam pengembangan web modern karena lebih modern, ringan, dan lebih efisien. Tetapi hal ini jika kita tidak butuh mendukung browser lama dalam aplikasi yang kita buat.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - AJAX GET
        Pertama, pada ```main.py``` saya menambahkan ini. Setelah itu saya mengatur pengaturan url di ```urls.py```

        ```python
        def get_flower_json(request):
            flowers = Flower.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', flowers))
        ```

        Lalu saya menambahkan ```script``` pada bagian bawah ```main.html```. Untuk mengambil data, kita menambahkan kode ini

        ```javascript
        async function getFlowers() {
            return fetch("{% url 'main:get_flower_json' %}").then((res) => res.json())
        }
        ```

        Untuk melakukan rendering main dari data yang diambil menggunakan AJAX, saya menambahkan kode berikut pada bagian ```script``` pada ```main.html```.

        ```javascript
        async function getFlowers() {
            return fetch("{% url 'main:get_flower_json' %}").then((res) => res.json())
        }

        async function refreshFlowers() {
        document.getElementById("flower-card").innerHTML = "";
        const flowers = await getFlowers();

        const decUrl = "{% url 'main:dec_flower' 0 %}";
        const incUrl = "{% url 'main:inc_flower' 0 %}";
        const delUrl = "{% url 'main:del_flower' 0 %}";
            
        flowers.forEach((flower, index, arr) => {
            const card = document.createElement("div");
            card.classList.add("card");


            const cardContent = `
                <h5>${flower.fields.name}</h5>
                <p style="font-size: 10px; margin: 0px 20px 10px 0px;">
                    ${flower.fields.date_added}</p>
                <p>Amount: ${flower.fields.amount}</p>
                <p>${flower.fields.description}</p>

                <form action="${incUrl.replace('0', flower.pk)}" method="POST">
                    {% csrf_token %}
                    <button class="inc-dec-button" type="submit">+</button>
                </form>
                <form action="${decUrl.replace('0', flower.pk)}" method="POST">
                    {% csrf_token %}
                    <button class="inc-dec-button" type="submit">-</button>
                </form>
                <form action="${delUrl.replace('0', flower.pk)}" method="POST">
                    {% csrf_token %}
                    <button class="del-button" type="submit">
                        <span>Delete</span>
                    </button>
                </form>
            `;

            card.innerHTML = cardContent;

            if (index === flowers.length - 1) {
                card.classList.add("last-card"); // Add a CSS class for the last card
            }

            document.getElementById("flower-card").appendChild(card);
        });
        }
        ```

        Setelah itu panggil function ```refreshFlowers()``` sehingga dapat dilihat.

    - AJAX POST

        Saya menulis kode berikut pada ```main.html``` untuk membuat modal dan membuat button Add Entry untuk memunculkan modal.

        ```html
        <div id="modal" class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title">Add New Entry</h1>
                </div>
                <div class="modal-body">
                    <form id="form" method="POST">
                        {% csrf_token %}
                        <table class="table">
                            <tr>
                                <td><label for="name">Name:</label></td>
                                <td><input type="text" id="name" name="name"></td>
                            </tr>
                            <tr>
                                <td><label for="amount">Amount:</label></td>
                                <td><input type="number" id="amount" name="amount"></td>
                            </tr>
                            <tr>
                                <td><label for="description">Description:</label></td>
                                <td><textarea id="description" name="description"></textarea></td>
                            </tr>
                        </table>
                    </form>
                </div>
                <div class="modal-footer">
                    <button id="close-button" class="btn-secondary">Close</button>
                    <button id="button-add" class="btn-primary">Add Entry</button>
                </div>
            </div>
        </div>
        <button id="open-modal" class="btn-primary">Add Entry</button>
        ```

        Selanjutnya saya menambahkan kode berikut pada ```views.py``` dan melakukan import ```from django.views.decorators.csrf import csrf_exempt```

        ```python
        @csrf_exempt
        def add_flower_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                amount = request.POST.get("amount")
                description = request.POST.get("description")
                user = request.user

                new_product = Flower(name=name, amount=amount, description=description, user=user)
                new_product.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
        ```

        Setelah itu saya menambahkan kode berikut, karena saya tidak menggunakan bootstrap saya mereferensi w3schools dan tutorial untuk membuat modalnya

        ```javascript
        // taken from W3Schools because I am not using bootstrap ^^
        const modal = document.getElementById("modal");
        const btn = document.getElementById("open-modal");
        const span = document.getElementById("close-button");

        btn.addEventListener("click", function() {
            modal.style.display = "block";
        });

        span.addEventListener("click", function() {
            modal.style.display = "none";
        });

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        };


        function addFlower(event) {
            fetch("{% url 'main:add_flower_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            })
            .then(response => {
                if (response.ok) {
                    modal.style.display = "none";
                    document.getElementById("form").reset();
                    refreshFlowers();
                }
            });

            return false
        }

        document.getElementById("button-add").onclick = addFlower;
        ```

        Setelah itu jalankan collectstatic dan lakukan git add commit push dan melakukan deployment.






