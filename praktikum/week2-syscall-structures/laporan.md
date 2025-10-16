
# Laporan Praktikum Minggu 2 
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
- Antarmuka antara program pengguna dan kernel sistem operasi (OS): System call adalah mekanisme terprogram yang memungkinkan aplikasi pengguna untuk meminta layanan dari kernel sistem operasi, yang mengelola dan mengendalikan sumber daya sistem.
- Perpindahan mode operasi: Ketika sebuah program memanggil system call, terjadi perubahan mode dari user mode (mode pengguna) ke kernel mode (mode kernel). Dalam user mode, program memiliki hak akses terbatas, sedangkan kernel mode memberikan hak istimewa untuk mengakses sumber daya sistem yang sensitif.
- Akses terkendali ke sumber daya: OS menggunakan system call sebagai satu-satunya titik masuk yang terkontrol untuk mengakses sumber daya perangkat keras dan kernel. Hal ini memastikan program pengguna tidak dapat merusak sistem atau mengakses sumber daya yang tidak seharusnya diakses secara langsung.

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
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil system call:


---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel?
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?
> jawab :
- system Call Penjelasan Fungsi Analisis Cara Kerja Kernel
- open("/etc/passwd", O_RDONLY) Membuka file /etc/passwd dalam mode read-only. Kernel memeriksa apakah file tersebut ada, apakah proses cat memiliki izin untuk membacanya, dan jika iya, kernel memberikan file descriptor (biasanya angka 3) kepada proses. Kernel berperan mengatur manajemen file descriptor dan keamanan akses file (melalui permission checking di sistem file).
- read(3, ... , 4096) Membaca isi file dari file descriptor 3 sebanyak maksimal 4096 byte (ukuran buffer standar). Kernel akan menyalin isi file dari sistem file ke buffer memori user-space program cat. Kernel mengatur transisi data dari storage (disk) ke memori, memastikan hanya bagian file yang diizinkan dapat diakses oleh proses.
- write(1, ... , 1582) Menulis data ke file descriptor 1 (stdout — layar terminal). Kernel akan menyalin isi buffer tadi ke output terminal pengguna. Kernel menangani output stream, memastikan data dikirim ke perangkat output (terminal) melalui buffer output standar.
close(3) Menutup file descriptor 3. Setelah ditutup, kernel membebaskan resource yang digunakan oleh file tersebut. Kernel membersihkan tabel file terbuka (file table) untuk proses cat, sehingga descriptor dapat digunakan kembali untuk file lain nanti.

[13.154095] systemd-journald[81]: Collecting audit messages is disabled. Kernel mencatat aktivitas dari proses systemd-journald, yaitu layanan yang menangani logging di sistem Linux. Pesan ini menunjukkan fitur audit sedang dimatikan.

[13.274579] systemd-journald[81]: Received client request to flush runtime journal. Kernel menerima permintaan untuk menyimpan log - sementara (runtime journal) ke disk.

[13.336252] systemd-journald[81]: File .../system.journal corrupted or uncleanly shut down... Kernel mendeteksi file log system.journal rusak atau tidak ditutup dengan benar (mungkin akibat shutdown mendadak), lalu membuat file pengganti.

[14.143751] ACPI: AC: AC Adapter [AC1] (on-line) Kernel mendeteksi adaptor daya (charger) aktif — ini adalah pesan dari subsistem ACPI (Advanced Configuration and Power Interface).

[14.144667] ACPI: battery: Slot [BAT1] (battery present) Kernel mendeteksi baterai laptop terpasang.

[17.482122] WSL (2 - init-systemd(Ubuntu)) ERROR: WaitForBootProcess... Kernel mencatat error pada Windows Subsystem for Linux (WSL2) karena proses inisialisasi systemd tidak selesai tepat waktu.

[27.582691] WSL (2 - Interop) ERROR: CreateLoginSession... Masih terkait WSL2 — kernel melaporkan gagal membuat sesi login karena waktu tung gu habis.

[30.018063] TCP: eth0: Driver has suspect GRO implementation... Kernel memberikan peringatan terkait driver jaringan (eth0), mungkin berpengaruh pada performa TCP.

[48.368303] hv_balloon: Max. dynamic memory size: 4034 MB Kernel Hyper-V (digunakan WSL2) melaporkan ukuran maksimum memori dinamis yang dialokasikan.

[600.986549] mini_init (175): drop_caches: 1 Kernel mencatat perintah pembersihan cache memori (drop_caches) oleh proses mini_init.

- perbedaan Dmesg (dari "display message") adalah perintah yang menampilkan pesan-pesan log dari kernel Linux. Ini mencakup informasi tentang aktivitas kernel, seperti deteksi hardware, pemasangan driver, error kernel, boot messages, dan event sistem lainnya. Output biasa adalah hasil dari perintah atau program yang dijalankan di user space (ruang pengguna), seperti perintah shell standar. Ini bisa berupa teks, data, atau hasil komputasi dari program seperti echo, ls, cat, atau aplikasi seperti Python script

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum system call

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi? 
   **Jawaban:**  fungsi utaman system call adalah sebagai antarmuka atau jembatan bagi program aplikasi untuk meminta pelayanan sistem operasi(OS)
 2. Sebutkan 4 kategori system call yang umum di gunkanan?
   **Jawaban:**  kategori system call yang umum digunakan adalah manajemen proses,manajemen berkas,manajemen perangkat dan komunikasi
3. Mengapa system call tidak bisa di panggil langsung oleh user program?
   **Jawaban:**  karena program pengguna berjalan di "user mode",sementara system call hanya bisa dijalankan di "kernel mode" yang lebih ori aman memiliki hak akses istimewa untuk beinteraksi langsung dengan perangkat keras dan memp

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  ada masalah pada laptop karena kurang suport pada aplikasi wsl linux
- Bagaimana cara Anda mengatasinya?  dengan membuka perlahan,maka wsl linux akan berjalan walapaun nunggu nya lumayan lama

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
