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
