

## Tugas 2

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/

![alt text](https://github.com/jasonirvine76/django-pbp-tugas/blob/main/images/workflows.png)
1. Client meminta request, lalu request akan dikirimkan ke urls.py. urls.py akan memilih view yang sesuai dengan request yang diminta client, setelah request diproses, views.py menentukan apakah terjadi pertukaran data, jika iya views.py akan melakukan transaksi data dengan models.py, jika tidak views.py langsung akan memilih HTML yang sesuai. Jika terjadi pertukaran data maka views.py akan menunggu data dari models.py, setelah data diterima views.py memilih HTML yang sesuai lalu data ditampilkan pada HTML. HTML yang terpilih akan mengirim response sehingga dapat terbentuk di sisi client tampilan beserta data yang diinginkan client.

2. Virtual Environment ini digunakan untuk memisahkan environment atau package luar antar project. Dalam suatu komputer, pastinya kita memiliki beberapa project django. Untuk menghindari konflik, maka diperlukan virtual environment untuk memisahkan package yang diinstal masing-masing project. Virtual environment ini membuat kita tidak menginstall external libraries secara global melainkan secara lokal. Coba bayangkan ketika kalian memiliki 2 project django, project 1 dibuat dengan django versi 2.2.26 dan project 2 dibuat dengan django versi 4.0. Jika kita menginstallnya di global, maka project 1 bisa saja mengalami error karena beberapa syntax tidak berlaku lagi di django versi 4.0 (deprecated). Maka dari itu kita perlu virtual environment sehingga setiap project dapat berjalan dengan django versi masing-masingnya agar tidak ada error saat dijalankan.

3. 



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
