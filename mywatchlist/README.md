## Tugas 3

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/mywatchlist

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
