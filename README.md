

## Tugas 2

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/

![alt text](https://github.com/jasonirvine76/django-pbp-tugas/blob/main/images/workflows.png)
1. Client meminta request, lalu request akan dikirimkan ke urls.py. urls.py akan memilih view yang sesuai dengan request yang diminta client, setelah request diproses, views.py menentukan apakah terjadi pertukaran data, jika iya views.py akan melakukan transaksi data dengan models.py, jika tidak views.py langsung akan memilih HTML yang sesuai. Jika terjadi pertukaran data maka views.py akan menunggu data dari models.py, setelah data diterima views.py memilih HTML yang sesuai lalu data ditampilkan pada HTML. HTML yang terpilih akan mengirim response sehingga dapat terbentuk di sisi client tampilan beserta data yang diinginkan client.

2. Virtual Environment ini digunakan untuk memisahkan environment atau package luar antar project. Dalam suatu komputer, pastinya kita memiliki beberapa project django. Untuk menghindari konflik, maka diperlukan virtual environment untuk memisahkan package yang diinstal masing-masing project. Virtual environment ini membuat kita tidak menginstall external libraries secara global melainkan secara lokal. Coba bayangkan ketika kalian memiliki 2 project django, project 1 dibuat dengan django versi 2.2.26 dan project 2 dibuat dengan django versi 4.0. Jika kita menginstallnya di global, maka project 1 bisa saja mengalami error karena beberapa syntax tidak berlaku lagi di django versi 4.0 (deprecated). Maka dari itu kita perlu virtual environment sehingga setiap project dapat berjalan dengan django versi masing-masingnya agar tidak ada error saat dijalankan.

3. Penjelasan langkah-langkah :
    + Mengimport model CatalogItem dari models.py di views.py. Pada views.py kita buat fungsi yang isinya dictionary. Dictionary ini kita isi dengan value nama, NPM, 
      data dari CatalogItem dengan menggunakan CatalogItem.objects.all(). Setelah itu jangan lupa untuk me-return request, dictionary tersebut, dan memilih file HTML
      mana yang ingin ditampilkan ketika fungsi tersebut dipanggil.
    + Menambah urlpatterns pada urls.py di app katalog yang isinya path yang diinginkan untuk menampilkan fungsi yang telah kita buat di views.py. Setelah itu, pada
      project_django, pada urls.py-nya kita tambahkan juga route/path yang diinginkan untuk memasukkan urls.py pada app katalog agar bisa ditampilkan pada web saya.
    + Setelah saya buat views-nya, saya membuat file HTML yang saya ingin tampilkan. File HTML ini akan menampilkan data yang berada di dictionary yang di return oleh       fungsi pada views.py. Dengan bantuan django template languange dan HTML, kita dapat menampilkan datanya berupa tabel. Cara menampilkannya kita iterasi data yang
      dikirim karena data yang dikirim tidak satuan sehingga kita harus iterasi terlebih dahulu untuk menampilkannya satu persatu.
    + Cara deploynya, saya membuat app pada akun heroku saya. Setelah itu pada repository github web ini di bagian settings, saya tambahkan secret key, yaitu
      HEROKU_API_KEY dan HEROKU_APP_NAME. Terakhir saya melakukan push sehingga perubahan yang saya lakukan tersimpan di repository saya, setelah selesai di push
      otomatis .github/workflows akan melakukan deployment di heroku

## Tugas 3

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/

* JSON adalah format yang digunakan untuk menyimpan dan mentransfer data (data delivery) atau dapat disebut sebagai format data standard. JSON memiliki kepanjangan JavaScript Object Notation.
* XML adalah bahasa komputer yang dibuat oleh World Wide Consortium (W3C) untuk menyederhanakan proses pertukaran dan penyimpanan data (data delivery). XML memiliki kepanjangan Extensible Markup Language.
* HTML adalah bahasa standar pemrograman yang digunakan untuk membuat halaman website. Perbedaannya dengan JSON dan HTML adalah JSON dan XML format data standard yang berfungsi pada menyimpan dan mentransfer data, sedangkan HTML bukanlah data standard atau dia tidak melakukan data delivery.
* Perbedaan JSON dengan XML:
  * JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk   dilihat, sedangkan XML menyimpan elemen-elemennya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, tetapi kurang efisien.
  * File JSON diakhiri dengan ekstensi .json, sedangkan file XML diakhiri dengan ekstensi .xml
  * File JSON berukuran lebih kecil daripada file XML
  * File XML lebih aman daripada JSON
  * JSON dapat mentransfer data lebih mudah karena dapat disimpan dalam bentuk array, sedangkan XML tidak bisa disimpan dalam bentuk array
* Kita memerlukan data delivery karena pada satu aplikasi dapat digunakan beberapa framework. Biasanya client-side dengan server-side menggunakan framework yang berbeda, sehingga untuk menyambungkan bagian client-side dan server-side kita memerlukan data delivery. Hal ini agar aplikasi dapat tersambung dengan baik, contohnya untuk menghubungkan mobile app dengan web app.
* Pertama kita membuat app mywatchlist dengan perintah "django-admin startapp mywatchlist". Lalu, saya membuat membuat model MyWatchList di models.py yang ada di app mywatchlist. Berikut field yang saya buat pada model MyWatchList:
  * watched : BooleanField
  * title :  CharField
  * rating : CharField
  * release_date : DateField
  * review : TextField
* Setelah itu, saya membuat fungsi pada views.py yang mengembalikan HTML, JSON, dan XML. Kemudian, saya mendaftarkan fungsi pada views ke urls.py pada folder mywatchlist dan juga menambahkan urls.py dari mywatchlist ke urls.py project-django. Lalu git add, commit, dan push ke repository sehingga dapat terdeploy di heroku.
* Postman :

**HTML**
[![Postman-HTML.png](https://i.postimg.cc/QdSGxPx0/Postman-HTML.png)](https://postimg.cc/nXsw33mD)

**JSON**
[![Postman-JSON.png](https://i.postimg.cc/28RV4qdg/Postman-JSON.png)](https://postimg.cc/PNyXH5RM)

**XML**
[![Postman-XML.png](https://i.postimg.cc/Bvkq4yMR/Postman-XML.png)](https://postimg.cc/Jy3wQTwQ)
## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
