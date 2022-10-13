## Tugas 6
* Synchronous programming adalah proses jalannya program secara sequential, program dieksekusi berdasarkan antrian eksekusi program <br>
  Asynchronous programming adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian.

* Event-Driven programming adalah paradigma pemrograman yang alur programmnya ditentukan oleh suatu event/peristiwa yang merupakan keluaran atau <br>
  tindakan pengguna atau bisa berupa pesan dari program lainnya.
  Pada HTML
  ```
  <form id = "form" onsubmit="return false;">
      <div class="modal-body">
          {% csrf_token %}
          <div class="form-outline form-white mb-4">
              <input type="text" name="title" placeholder="Title" class="form-control">
              <label>Title</label>
          </div>

          <div class="form-outline form-white mb-4">
              <input type="text" name="description" placeholder="Description" class="form-control">
              <label>Description</label>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button id = "button" type="button" class="btn btn-primary">Add task</button>
          </div>
      </div>
  </form>
  ```

  JavaScript
  ```
  document.getElementById("button").onclick = addTask
  ```
  Intinya jika button ```Add task``` dengan id = "button" di click maka fungsi addTask akan dijalankan

* 1. Browser membuat JavaScript call yang kemudian akan mengaktifkan XMLHttpRequest.
  2. Di background, web browser mengirimkan permintaan (request) HTTP ke server.
  3. Server menerima, mengambil, dan mengirimkan data kembali ke web browser.
  4. Web browser menerima data yang diminta dan akan langsung ditampilkan di halaman tanpa harus melalui proses reload terlebih dulu.

* Cara saya mengimplementasikan checklist di atas adalah pada bagian AJAX GET saya membuat view baru, yaitu show_json yang mengembalikan data dalam bentuk JSON <br>
  lalu menambahkan url path ```/todolist/json``` yang menjalankan fungsi show_json dan nantinya akan menampilkan data dalam bentuk JSON. Pada pengambilan task, <br>
  todolist.html ditambahkan bagian script, lalu saya membuat fungsi refreshTask. Pada fungsi refreshTask pertama kita fetch data dari /todolist/json dengan bantuan <br>
  fungsi getTask yang fungsinya untuk mengambil data JSON, lalu pada bagian kode html yang tujuannya untuk menampilkan data ditambahkan id, <br>
  selanjutnya saya melakukan loop untuk setiap elemen di JSON lalu membuat kode htmlnya agar bisa ditampilkan dengan card.

* Pada bagian AJAX POST, saya membuat modal bootstrap dengan isinya form untuk penambahan task. Selanjutnya, saya membuat view baru add_task_item dengan isi membuat object task baru <br>
  lalu tambahkan url path ```/todolist/add``` di urls.py yang menjalankan fungsi add_task_item. Lalu, saya membuat fungsi addTask yang isinya menunjuk url path ```/todolist/add``` <br>
  dengan HTTP request method: "POST" dan body isinya FormData yang mau dibuat user, lalu fungsi addTask memanggil refreshTask diakhir agar tidak perlu refresh page setiap addTask.