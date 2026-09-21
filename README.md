Nama : Lavida Yuthiana Faizah
NPM : 2506605941
Kelas : PBP E
Dosen : Daya Adianto

### Tugas 1
1. Saya menggunakan elemen semantik HTML seperti 'header', 'main', 'section' dengan id berbeda setiap section, dan 'footer'. Saya sempat memakai 'div' untuk tabel dan ternyata layoutnya berantakan karena untuk tabel seharusnya 'table', 'tbody', 'tr', 'td', setelah saya benarkan, kolomnya baru terlihat. Saya menyadari bahwa elemen semantik membantu dalam membuat konten terlihat rapi dan sesuai jenisnya.

2. Tantangan terbesar saya ada di tabel yang bisa berantakan jika di buka di layar sempit seperti hp, karena kontennya butuh ruang horizontal. Jadi saya memakai 'overflow-x:auto' agar bisa discroll ke samping.

3. Batasan yang paling terasa adalah saat semua data itu di hardcode jadi kalau ada perubahan harus di edit HTMl nya CSS nya lalu di deploy lagi. Maka dari itu, selanjutnya saya ingin data disimpan di database yang dapat diambil tanpa harus mengedit HTML

# AI DISCLOSURE
Saya menggunakan Google Gemini untuk bantu debugging error saat gambar tidak terlihat, melakukan validasi, mencari tahu beberapa tag di HTML dan CSS
Link Google Gemini: https://share.gemini.google/jOTQ6nPlBraj

### Tugas 2
1. Ketika saya membuka halaman education, browser mengirim request ke urls.py. File ini mengecek URL tersebut, karena URL bukan admin maka request diteruskan ke urls.py milik main. Di sana, django menemukan bahwa education menggunakan route show_education, lalu menjalankan fungsi tersebut di views.py. Fungsi ini mengambil semua data dengan Education.objects.all() dari database, lalu memasukannya ke context. Lalu, context dikirim ke template education.html. Di template, django menggunakan {% for education in education_list %} untuk menampilkan setiap data. Setelah itu, HTML yang sudah jadi dikirim ke browser dan ditampilkan sebagai halaman education.

2. Karena kalau hardcode di template, setiap perubahan data harus diedit di HTML dan deploy ulang. Setelah saya pindahkan ke model dan hardcodenya dihapus, saya bisa nambahin/ngubah data lewat admin, ini juga bikin data lebih konsisten karena sumbernya cuma database, tidak tersebar di banyak file.

3. 'makemigrations' membaca semua perubahan yang saya buat di models.py lalu genereate file migration, perubahan ini belum diterapkan ke database. 'migrate' mengeksekusi file migration tersebut ke database. Saya menerapkan migration ini saat menambahkan model baru seperti education dan volunteer. Saya juga menambahkan field 'description' ke model 'education' setelah model awalnya dibuat, saya harus menjalankkan migration lagi.

# AI DISCLOSURE
Saya menggunakan Google Gemini untuk bantu mengerti syntax-syntax, debugging error dan validasi pengerjaan saya.
Link Google Gemini: https://share.gemini.google/LeLWnFAB3297

### Tugas 3
1. Saya menggunakan ModelForm agar konfigurasi form, seperti tipe data dan aturan validasi, bisa diturunkan langsung dari model secara otomatis. Hal ini menghemat banyak waktu karena kita tidak perlu menulis ulang input HTML atau membuat validasi manual di view setiap kali ada perubahan struktur data. Selain itu, fitur bawaannya sangat praktis: form.is_valid() menangani validasi, field.errors menyediakan pesan kesalahan, dan form.save() langsung berinteraksi dengan database (bahkan bisa dipakai untuk edit data dengan parameter instance=).

Untuk keamanannya, tag {% csrf_token %} mutlak diperlukan pada method POST guna mencegah serangan CSRF yang bisa dimanfaatkan pihak luar untuk mengirim request berbahaya atas nama pengguna yang sedang login. Django mengamankan proses ini dengan menyematkan token unik berbasis sesi yang wajib dicocokkan saat data dikirim; jika gagal, request otomatis ditolak dengan error 403.

2. JSON lebih populer daripada XML karena formatnya lebih ringkas, ringan, dan mudah dibaca. Berbeda dengan XML yang memerlukan tag pembuka dan penutup pada setiap elemen sehingga ukurannya lebih besar, JSON menggunakan struktur key-value, objek, dan array yang jauh lebih sederhana. Selain itu, JSON sangat mudah diintegrasikan karena strukturnya mirip dengan objek JavaScript (bisa langsung dibaca lewat JSON.parse()) serta selaras dengan tipe data dictionary dan list di berbagai bahasa pemrograman. Hal inilah yang membuat JSON menjadi standar di banyak API modern, sehingga lebih mudah dikonsumsi oleh aplikasi frontend maupun mobile.

3. Saat pengguna mengakses /education/api/, Django mencocokkan request melalui urls.py ke view get_education_json yang menyaring data Education berdasarkan parameter pencarian. Queryset tersebut diubah menjadi teks JSON menggunakan serializers.serialize() lalu dikembalikan melalui HttpResponse berformat application/json. Sementara itu, halaman /education/ memanggil data tersebut, melakukan deserialisasi, dan meneruskannya ke templat education.html.

Proses serialization ini wajib dilakukan karena objek Python di memori server harus diubah menjadi format teks standar yang dapat dikirim lewat protokol HTTP ke klien (seperti UUID dan Decimal yang dikonversi menjadi string).

# AI DISCLOSURE
Saya menggunakan Google Gemini untuk bantu mengerti syntax-syntax, debugging error dan validasi pengerjaan saya.
Link Google Gemini: https://share.gemini.google/APVJqKyUOZvw