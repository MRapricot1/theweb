Link aplikasi: 
1. Data delivery dalam implementasi platform merupakan peran yang penting karena platform bisa melakukan pertukaran data antar sistem. Jika tidak ada data delivery, platform tidak dapat mengirim data dan informasi yang dibutuhkan sehingga informasi dan data yang kita butuhkan tidak sampai kepa a kita.

2. Menurut saya pribadi, json lebih baik dari pada xml karena json memiliki struktur yang mudah dibaca dan tampilan sederhana bahkan untuk pemula sekalipun. Sedangkan xml menggunakan tag yang lebih panjang dan lebih kompleks dibandingkan dengan json, Sehingga mesin lebih cepat memroses dan memahami. Selain itu, json juga memiliki ukuran file yang lebih kecil dibandingkan dengan xml jadi dari sisi efisien, json lebih unggul dan disukai banyak orang. Sedangkan xml memiliki ukuran file yang lebih besar sehingga dapat memperlambat proses pengiriman data. Dengan itu, banyak orang yang memilih menggunakan json karena keunggulannya tersebut.

3. Fungsi is_valid() pada pada form Django adalah untuk melakukan pemeriksaan terhadap data yang kita masukkan apakah valid atau tidak dengan yang kita inginkan. Method ini penting dan kita butuhkan karena jika ada data yang tidak cocok dengan kriteria kita, maka hal itu dapat menimbulkan potensi adanya virus atau hal-hal yang tidak kita inginkan.

4. Kita membutuhkan csrf_token saat membuat form di Django karena csrf_token dapat kita gunakan untuk mencegah CSRF atau Cross-Site Request Forgery yang dimana ini merupakan serangan yang menggunakan otentikasi user untuk mengirim permintaan yang tidak resmi. Serangan ini dapat membahayakan situs kita maupun situs lain.

5. Cara saya implementasi setiap check list diatas dimulai dengan me-review ulang dari  tutorial 2 dan memahami kembali. Pada saat pengerjaan terdapat kendala yaitu auto save pada vscode saya tidak aktif yang mengakibatkan kode-kode saya tidak ter-update sehingga kode saya tidak muncul di local host. Karena mengikuti tutorial 2, banyak penamaan variabel bahkan function yang salah (harusnya products menjadi news). Untungnya asdos sangat membantu dengan fast respon.

6. Asdos sudah bekerja dengan baik

7. ![json](json.png)
    ![xml](xml.png)
    ![json_by_id](json_by_id.png)
    ![xml_by_id](xml_by_id.png)





















Link aplikasi: https://theo-samuel-toko-football.pbp.cs.ui.ac.id/
1. Cara saya implementasi setiap checklist diatas, yang pertama adalah dengan membuat framework seperti: membuat folder baru, mengaktifkan environtment (python -m venv env), serta melakukan instalasi depedensi awal. Langkah kedua adalah dengan membuat struktur ptojek dengan cara menaruh file settings, manage.py, dan lain-lain di root django-admin start ptoject. Setelah itu, kita mendefinisikan model (membuat file models.py) yang berisi atribute yang akan kita gunakan aplikasi seperti nama, harga, deskirpsi, thumbnail, kategori, dan is_featured, lalu diikuti dengan tipe data masing-masing. Lalu, kita bisa membuat dan menjalankan migrasi. Jangan lupa untuk kita melakukan routing URL agar link yang kita buat bisa diakses oleh orang lain dan django akan mencocokkan URL dengan pola yang ada di file urls.py. Langkah selanjutnya kita bisa memulai untuk membuat isi dari aplikasi kita dengan html. Langkah terakhir, jangan lupa push ke Github dan PWS. 

2. ![alt text](URL_diagram.drawio.png)
Kaitan antara urls.py, views.py, models.py, dan berkas html adalah urls.py merupakan file yang membuat arah URL ke file view.py sedangkan, views.py adalah logika request yang berfungsi mengambil atau mengubah data melalui models.py berbeda dengan models.py, models.py sendiri merupakan definisi struktur dan query data. Sedangkan, html sendiri adalah file tampilan yang diproses oleh view.py menggunakan cariable dari context.

3. Peran settings pada proyek django adalah sebagai panel kontrol atau pusat konfigurasi pada seluruh projek django. Django memuatnya pada saat start melalui variable environment DJANGO_SETTINGS_MODULE.

SECRET_KEY = os.environ.get("SECRET_KEY")  # simpan di env, JANGAN commit
DEBUG = os.environ.get("DEBUG", "0") == "1"
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "example.com"]

kode di atas merupakan contoh mengapa settings.py ppenting pada projek django. Pada bagian SECRET_KEY, lalu dilanjutkan pada DEBUG yang berisi True pada lokal dan di produksi wajib bernilai FALSE. Selanjutnya ada ALLOWED_HOSTS yang berisi daftar domain yang diizinkan melayani request.

4. Cara kerja migrasi pada database django dimulai dengan mengubah model terlebih dahulu di model.py. Setelah itu kita bisa menjalankan python manage.py makemigrations yang berfungsi untuk menciptakan file yang dimana isinya merupakan perubahan model yang belum teraplikasi ke dalam basis data. Lalu kita jalankan python manage.py migrate untuk migrasi yang berfungsi untuk mengaplikasi perubahan model yang ada dalam file ke basis data. Setiap kita perubahan pada model, kita wajib melakukan migrasi untuk merefleksikan perubahan tersebut. Setelah itu django akan menyimpan perubahan yang sudah diterapkan.

5. Django dijadikan permulaan untuk pembelajaran pengembangan perangkat lunak karena django sudah terdapat template bawaan seperti: routing, template engine, ORM, form dan validasi, dan masih banyak lagi sehingga memudahkan kita untuk belajar. Tidak hanya itu, dokumentasi dan ekosistem yang django miliki sudah bagus. Dokumentasi jelas dan banyak komunitas yang menyediakan berbagai tutorial sehingga belajar menjadi lebih mudah karena akses sudah ada dimana-mana. Selain itu django sudah berbasis python yang memudahkan untuk dibaca.

6. Sejauh ini asisten dosen sudah melakukan tugas dengan baik dan ketika saya mengalami kesulitas, asdos menjelaskan dengan senang hati sampai saya bisa mengerjakannya
