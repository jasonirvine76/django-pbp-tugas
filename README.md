

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



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
