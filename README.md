

## Tugas 2

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/

1. 
![alt text](https://github.com/jasonirvine76/django-pbp-tugas/blob/main/images/workflows.png)

Client meminta request, lalu request akan dikirimkan ke urls.py. urls.py akan memilih view yang sesuai dengan request yang diminta client, setelah request diproses, views.py menentukan apakah terjadi pertukaran data, jika iya views.py akan melakukan transaksi data dengan models.py, jika tidak views.py langsung akan memilih HTML yang sesuai. Jika terjadi pertukaran data maka views.py akan menunggu data dari models.py, setelah data diterima views.py memilih HTML yang sesuai lalu data ditampilkan pada HTML. HTML yang terpilih akan mengirim response sehingga dapat terbentuk di sisi client tampilan beserta data yang diinginkan client.



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
