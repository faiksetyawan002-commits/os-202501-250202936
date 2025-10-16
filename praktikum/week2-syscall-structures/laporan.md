
# Laporan Praktikum Minggu [X]
Topik: system call

---

## Identitas
- **Nama**  :Faik Setyawan
- **NIM**   : 250202936  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
> jawab
1. 1.Konsep system call yaitu
- Jembatan antara dua mode: Aplikasi berjalan di mode pengguna dengan hak akses terbatas, sementara kernel berada di mode kernel yang memiliki hak akses penuh ke perangkat keras. System call adalah cara aplikasi beralih sementara ke mode kernel untuk meminta layanan yang tidak bisa dilakukannya sendiri, dan kemudian kembali ke mode pengguna setelah tugas selesai. 
- Permintaan layanan: Ketika sebuah program perlu melakukan sesuatu yang memerlukan hak akses lebih tinggi, seperti membaca dari file, alokasi memori, atau berkomunikasi dengan program lain, program tersebut akan memanggil system call yang sesuai. 
- Pengendalian oleh OS: Setelah system call dieksekusi, kernel mengambil alih kontrol untuk melakukan tugas yang diminta. Setelah selesai, kernel mengembalikan kontrol kepada aplikasi, dan program dapat melanjutkan eksekusinya.
1. 2.fungsi system call adalah Manajemen proses,Manajemen file,Manajemen perangkat,Komunikasi,Manipulasi memori dan Pengambilan informasi
   
2.jenis jenis system call dan fungsinya :
- Kontrol Proses fungsinya Mengelola eksekusi proses di dalam sistem operasi, termasuk membuat, mengakhiri, dan mengawasi proses.
- Manajemen Berkas fungsinya Melakukan operasi pada berkas atau file, seperti membaca, menulis, membuka, dan menutup. 
- Manajemen Perangkat fungsinya Mengelola akses ke perangkat keras seperti disk, keyboard, atau printer.
- Pemeliharaan Informasi fungsinya Melakukan operasi yang berkaitan dengan informasi, seperti mendapatkan atau mengatur waktu, tanggal, atau informasi sistem lainnya
- Komunikasi fungsinya mengelola komunikasi antar proses (IPC - Inter-Process Communication) untuk pertukaran data dan informasi.

3. Ketika sebuah program yang berjalan dalam mode pengguna (user mode) membutuhkan akses ke sumber daya yang dilindungi, seperti perangkat keras atau memori yang dikelola sistem operasi, program tersebut harus melakukan system call. System call ini memicu transisi ke mode kernel (kernel mode) agar permintaan tersebut dapat diproses dengan hak istimewa yang lebih tinggi.
   
4. Untuk menampilkan dan menganalisis system call di Linux, kita dapat menggunakan beberapa perintah, yang paling umum adalah strace, ltrace


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari system call: 

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
