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

### AI DISCLOSURE Tugas 4
Saya menggunakan Claude untuk mendapat panduan step by step Tugas 4. Bagian yang dibantu: pengecekan peran di views, menyembunyikan tombol di template, fitur star, dan pengamanan endpoint JSON. AI awalnya menyarankan membuat file permissions.py terpisah, tapi saya memilih cara yang lebih sederhana sesuai petunjuk soal (cek grup langsung di view). Saya juga sempat mengalami error import karena sisa kode lama, lalu memperbaikinya sendiri.

### Tugas 5
1. Debouncing adalah teknik untuk menunda fungsi agar tidak langsung dijalankan setiap kali pengguna melakukan event. Di proyek ini, fungsi akan dijalankan setelah pengguna berhenti mengetik selama 300 ms. Kalau tidak menggunakan debouncing, setiap tombol yang ditekan akan mengirim request. Contohnya, saat mengetik “universitas”, bisa terjadi 11 request. Hal ini bisa membuat server lebih terbebani, penggunaan kuota jadi lebih banyak, dan response dari request sebelumnya bisa datang terlambat lalu menggantikan hasil yang lebih baru. Dengan debouncing, request hanya dikirim setelah pengguna selesai mengetik.

2. fetch() menghasilkan Promise, jadi data tidak langsung didapatkan await digunakan untuk menunggu sampai Promise selesai, sehingga kita bisa mendapatkan objek Response. Setelah itu, await response.json() digunakan untuk mengambil data dari response tersebut. Kalau tidak memakai await, variabel masih berisi Promise yang belum selesai (pending), sehingga response.ok bisa menjadi undefined dan data.length atau forEach bisa mengalami error. Selain itu, error dari jaringan juga tidak bisa ditangani dengan baik menggunakan try ... catch

3. XSS adalah serangan ketika seseorang memasukakn script berbahaya, misalnya <img src=x onerror=...>, ke dalam data yang kemudian dijalankan di browser pengguna lain. Hal ini bisa digunakan untuk mencuri cookie atau sesi, bahkan melakukan tindakan atas nama korban. Pada Django, {{ variabel }} secara default sudah melakukan auto-escaping. Namun, kalau data ditampilkan menggunakan JS seperti innerHtml dan template literal, perlindungan tersebut tidak berlaku karena data dari JSON langsung dianggap sebagai HTML. Oleh karena itu, data perllu di-escape secara manual menggunakan escapeHtml atau textContent di sisi client. Selain itu, input juga bisa dibersihkan dengan strip_tags di server sebagai perlindungan tambahan.

# AI Disclosure Tugas 5
Saya menggunakan Claude sebagai pemandu step by step dengan memberikan instruksi soal. Ai tidak mengubah kode saya secara langsung, saya mengerjakan setiap langkah sendiri lalu mengirim hasilnya untuk dicek sebelum commit. Bagian yang dibantu meliputi endpoint JSON manual dengan info star, view POST AJAX, modal form, pencarian dengan debouncing, toast, refactor 'escapeHtml' dan 'getCookie' ke 'utils.js' dan 'strip_tags' di form. Pola Education kemudian saya terapkan sendiri ke Volunteer. Lewat review, ditemukan beberapa kesalahan saya yang kemudian saya perbaiki: class dan 'id' modal yang salah sehingga JavaScript tidak menemukan form, 'volunteer.html' yang lupa di-commit, dan template yang dihapus tanpa 'git rm'. Keterbatasan AI yang saya catat: AI tidak bisa menguji tampilan di browser saya, sehingga pengujian UI saya lakukan sendiri; AI juga hanya melihat kode yang saya kirim; dan 'strip_tags' hanya membuang tag, bukan isinya, sehingga '<b>halo</b><script>a()</script> tersimpan sebagai 'haloa()'.