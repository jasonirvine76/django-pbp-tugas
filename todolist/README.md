## Tugas 4

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/todolist

* CSRF token digunakan untuk mengenkapsulasi data yang dikirim dalam method POST, jika tidak ada CSRF token data dapat dilihat di url sehingga dapat terjadi serangan dari hacker. Jika kita menghilangkan {% csrf_token %} lalu kita POST data akan menyebabkan error (Forbidden (403))
* Ya, kita dapat membuat form tanpa menggunakan generator seperti {{ form.as_table }}. Salah satu caranya, yaitu :
    1. Buatlah table pada html dengan membuat ```<table> </table>```
    2. Dalam ```<table> </table>``` buatlah row dengan cara membuat tag ```<tr> </tr>```
    3. Dalam tag ```<tr> </tr>``` buatlah data yang nanti akan diisi form yang diinginkan, caranya dengan membuat tag ```<td> </td>```
    4. Dalam tag ```<td> </td>``` buatlah form yang diinginkan dengan tag ```<input type="text"(isi bisa dengan text, password, submit) name="(nama yang diinginkan)" class="form-control"/>```
    5. Buatlah tombol untuk mengirim data seperti ```<td><input class="btn login_btn" type="submit" value="(Isi)"></td>```
* Alur data sebagai berikut: User menginput data pada form yang tersedia lalu tekan tombol submit. Request yang berisi data akan dikirim dengan url yang sesuai, lalu url memilih views yang sesuai. Dalam views tersebut data disimpan bisa dengan form.save() atau langsung dari objectnya (object.save()). Setelah itu, data akan diambil dengan NamaModel.objects.all() lalu dikirim dengan dictionary ```data:{NamaModel.objects.all()}``` di response atau bisa juga render. Pada bagian htmlnya kalian bisa akses dengan data.NamaAttribute.
* Cara implementasi checklist di atas:
    1. Membuat aplikasi baru bernama todolist dalam folder django-project di cmd dengan command ```django-admin startapp todolist```
    2. Menambahkan path todolist di urls.py di bagian urlpatterns folder django-project agar dapat diakses app yang kita buat
    3. Membuat model Task dengan atribut user, date, title, dan description
    4. Membuat html login, register, dan create-task beserta formnya
    5. Membuat fungsi-fungsi pada views.py yang memproses request masing-masing html.
    6. Membuat html untuk menampilkan data di sini ```todolist.html``` dengan tombol selesai, belum selesai, dan hapus
    7. Membuat fungsi todolist(request) yang mengembalikan render dengan semua object task
    8. Membuat fungsi yang menghandle tombol selesai, belum selesai, dan hapus
    9. Tambahkan path/routing dalam bagian urlpatterns di urls.py pada folder todolist dengan views yang menghandle fitur-fitur pada html
* Untuk penilaian bonus, kita memanggil id dari task yang ingin kita ubah. ID didapat dari url untuk fungsi selesai, belum selesai, dan delete. Setelah kita mendapatkan object tasknya kita dapat mengubahnya dengan ```task.is_finished = True/False lalu di task.save() dan untuk yang delete dengan task.delete()```

## Tugas 5
* Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen html
    ```<div style = "padding: 10px;"><a class="navbar-brand" href="#">Tugas 4 PBP</a></div>```
  kelebihan:
    * Permintaan HTTP yang lebih kecil
    * Berguna untuk perbaikan cepat
    * Berguna jika untuk menguji dan melihat perubahan
  kelemahan:
    * Inline CSS harus diterapkan pada setiap elemen
* Internal CSS adalah kode CSS yang ditulis pada ```tag<style>``` dan kode HTML yang ditulis di bagian header file HTML
    ```
    <style>
        .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.589);
        }
    </style>
    ```
  kelebihan:
    * Perubahan hanya terjadi pada 1 halaman
    * Class dan ID bisa digunakan oleh internal stylesheet
    * Tidak perlu mengupload beberapa file karena html dan css bisa digunakan dalam satu file
  kelemehan:
    * Meningkatkan waktu akses website
    * Perubahan hanya terjadi pada 1 halaman, tidak efisien jika ingin menggunakan CSS pada beberapa halaman.
* External CSS adalah kode CSS yang ditulis terpisah dari kode HTML. External CSS ditulis di sebuah file khusus menggunakan ekstensi .css
  contoh style.css yang berisi:
    ```
    .xleftcol {
    float: left;
    width: 33%;
    background:#809900;
    }
    .xmiddlecol {
    float: left;
    width: 34%;
    background:#eff2df;
    }
    ```
  kelebihannya:
    * Ukuran file HTML menjadi lebih kecil dan lebih rapi
    * Kecepatan loading menjadi lebih cepat
    * File CSS yang sama dapat digunakan di banyak halaman
  kekurangannya:
    * Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil
* Tag : 
    *```<html>...</html>```
    *```<title>...</title>```
    *```<body>...</body>```
    *```<p>...</p>```
    *```<h1>...</h1>```
    *```<a>...</a>```
    *```<li>...</li>```
* Selector:
    * Selektor Tag adalah Selektor Tag disebut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag
        ```
        p {
            color: blue;
        }
        ```
    * Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
        ```
        .card:hover {
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.589);
        }
        ```
        ```
        <div class="card" style="width: 18rem;">
          <h5 class="card-header">{{item.title}}</h5>
          <div class="card-body">
            <h5 class="card-title">{{item.description}}</h5>
            <p class="card-text">{{item.date}}</p>
            <p class="card-text">Status Penyelesaian: {{item.is_finished}}</p>
            <a href="{% url 'todolist:finished' item.id %}" class="btn btn-primary">Selesai</a>
            <a href="{% url 'todolist:not-finished' item.id %}" class="btn btn-primary">Belum Selesai</a>
            <a href="{% url 'todolist:delete' item.id %}" class="btn btn-danger">Hapus</a>
          </div>
        </div>
        ```
    * Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja. Selektor ID ditandai dengan tanda pagar (#) di depannya.
        ```
        #header {
            background: teal;
            color: white;
            height: 100px;
            padding: 50px;
        }
        ``` 
        dengan kode HTML
        ```
        <header id="header">
            <h1>Selamat Datang di Website Saya</h1>
        </header>
        ```
    * Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
        ```
        input[type=text] {
            background: none;
            color: cyan;
            padding: 10px;
            border: 1px solid cyan;
        }
        ```
        artinya kita akan memilih semua elemen ```<input>``` yang memiliki ```type="text"```
    * Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.
        ```
        * {
            border: 1px solid grey;
        }
        ```
        artinya semua elemen akan memiliki border dengan ukuran 1px dengan warna abu-abu
    * Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.
        contoh selektor pseudo-element:
            * ::before untuk memilh elemen semu sebelum elemen;
            * ::after untuk memilh elemen semu setelah elemen;
            * ::marker untuk memilh marker pada list;
            * ::placeholder untuk memilih teks placeholder pada elemen input teks;
* Cara saya mengimplementasikan checklist saya menambahkan bootstrap terlebih dahulu di base.html dengan
    ``` <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">```
  Saya menambahkan css pada halaman login, register, dan create-task sesuai dengan yang saya inginkan. Saya mencari template di google yang sudah responsive.
  Saya menambahkan kode CSS pada halaman todolist dengan membuat navbar yang berisi tugas, tombol create task, dan tombol logout.
  Lalu, saya menambahkan kode CSS pada halaman todolist dengan membuat card yang diisi dengan object todolist.
    








## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
