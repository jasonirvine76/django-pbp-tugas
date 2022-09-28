## Tugas 4

Silahkan mengunjungi: https://initugaspbp.herokuapp.com/todolist

* CSRF token digunakan untuk mengenkapsulasi data yang dikirim dalam method POST, jika tidak ada CSRF token data dapat dilihat di url sehingga dapat terjadi serangan dari hacker. Jika kita menghilangkan {% csrf_token %} lalu kita POST data akan menyebabkan error (Forbidden (403))
* Ya, kita dapat membuat form tanpa menggunakan generator seperti {{ form.as_table }}. Salah satu caranya, yaitu :
    1. Buatlah table pada html dengan membuat "<table> </table>"
    2. Dalam "<table> </table>" buatlah row dengan cara membuat tag "<tr> </tr>"
    3. Dalam tag "<tr> </tr>" buatlah data yang nanti akan diisi form yang diinginkan, caranya dengan membuat tag "<td> </td>"
    4. Dalam tag "<td> </td>" buatlah form yang diinginkan dengan tag "<input type="text"(isi bisa dengan text, password, submit) name="(nama yang diinginkan)" class="form-control"/>"
    5. Buatlah tombol untuk mengirim data seperti "<td><input class="btn login_btn" type="submit" value="(Isi)"></td>"
* Alur data sebagai berikut: User menginput data pada form yang tersedia lalu tekan tombol submit. Request yang berisi data akan dikirim dengan url yang sesuai, lalu url memilih views yang sesuai. Dalam views tersebut data disimpan bisa dengan form.save() atau langsung dari objectnya (object.save()). Setelah itu, data akan diambil dengan NamaModel.objects.all() lalu dikirim dengan dictionary di response atau bisa juga render
 



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
