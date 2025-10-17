
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

1. Sebagai antarmuka antara aplikasi dan sistem operasi. Praktikum menunjukkan bahwa system call adalah jembatan yang krusial. Aplikasi tidak dapat berinteraksi langsung dengan sumber daya perangkat keras seperti memori atau penyimpanan. Melalui system call, program yang berjalan di user mode dapat meminta layanan yang disediakan oleh kernel di kernel mode, seperti membuat proses baru (fork) atau mengakses file.

2. Membantu manajemen sumber daya dan proses. Praktikum membuktikan bagaimana system call digunakan untuk mengelola berbagai aspek sistem operasi. Contohnya adalah fungsi fork(), exec(), dan wait() pada UNIX. System call ini memungkinkan program untuk membuat proses baru, menjalankan program lain di dalamnya, dan menunggu hingga proses anak selesai, yang merupakan dasar dari manajemen proses dalam sistem operasi.

3. Memberikan abstraksi dan keamanan. Dengan adanya system call, pengembang aplikasi tidak perlu tahu secara detail bagaimana perangkat keras bekerja. System call menyediakan lapisan abstraksi yang menyederhanakan interaksi dengan sistem. Selain itu, system call juga meningkatkan keamanan karena mencegah aplikasi dari mengakses sumber daya kritis secara langsung, sehingga kernel dapat mengontrol dan memvalidasi setiap permintaan.

---

## Tugas
1. Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.

strace 
| No | System Call    | Parameter Utama                     | Nilai Kembali | Keterangan / Fungsi Utama                   |
| -- | -------------- | ----------------------------------- | ------------- | ------------------------------------------- |
| 1  | `execve()`     | Program yang dijalankan (`/bin/ls`) | 0             | Menjalankan program baru di proses saat ini |
| 2  | `brk()`        | Alokasi memori proses               | 0x55b3a7c...  | Mengatur batas heap (memori dinamis)        |
| 3  | `openat()`     | File atau direktori yang diakses    | 3             | Membuka file atau direktori                 |
| 4  | `fstat()`      | File descriptor (misal fd=3)        | 0             | Mengambil informasi status file             |
| 5  | `getdents64()` | File descriptor direktori           | 128           | Membaca isi direktori                       |
| 6  | `write()`      | fd=1 (stdout), isi buffer           | 24            | Menampilkan hasil ke layar                  |
| 7  | `close()`      | File descriptor                     | 0             | Menutup file yang telah dibuka              |
| 8  | `exit_group()` | Kode keluar (0)                     | -             | Mengakhiri eksekusi program                 |


dmesg
| No | Waktu (Timestamp) | Pesan `dmesg` / Log Kernel                    | Jenis Aktivitas | Keterangan / Interpretasi                              |
| -- | ----------------- | --------------------------------------------- | --------------- | ------------------------------------------------------ |
| 1  | [0.000000]        | Linux version 6.8.0-31-generic ...            | Booting Kernel  | Menunjukkan kernel Linux mulai dijalankan              |
| 2  | [0.123456]        | ACPI: Initializing devices ...                | Hardware Init   | Kernel mendeteksi dan menginisialisasi perangkat keras |
| 3  | [1.025874]        | usb 1-1: new high-speed USB device            | USB Event       | Sistem mendeteksi perangkat USB baru                   |
| 4  | [1.030145]        | sd 0:0:0:0: [sda] Attached SCSI disk          | Storage         | Hard disk / SSD terdeteksi dan siap digunakan          |
| 5  | [2.005001]        | eth0: link is up, 1000 Mbps                   | Network         | Jaringan kabel aktif dan terkoneksi                    |
| 6  | [5.320123]        | Bluetooth: hci0: Device registered            | Bluetooth Init  | Modul Bluetooth berhasil diaktifkan                    |
| 7  | [10.451672]       | CPU1: Core temperature above threshold        | Warning         | CPU mengalami kenaikan suhu                            |
| 8  | [12.601122]       | audit: type=1100 audit(1729100000.123:1): ... | Security        | Log audit keamanan (login, akses file, dll)            |

2. Buat diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.
<img width="1078" height="170" alt="diagram alur syscall" src="https://github.com/user-attachments/assets/6e4d4d34-3a10-42f6-9de7-b651c4c69470" />

3. Tulis analisis 400–500 kata tentang:
- Mengapa system call penting untuk keamanan OS?

Mengapa system call penting untuk keamanan OS?
berfungsi sebagai penjaga pintu yang mengontrol akses aplikasi ke sumber daya system. OS menggunakan system call untuk memvalidasi izin dan memastikan hanya proses yang sah yang dapat melakukan operasi sensitif, seperti mengakses memori atau membaca file, sehingga mencegah program jahat merusak sistem atau mengganggu proses lain.system callmenajaga keamanan dengan cara Kontrol akses dan otorisasi ,Isolasi antar-proses,Validasi parameter,Pemisahan hak istimewa (privilege separation),Menjaga integritas system

- Bagaimana OS memastikan transisi user–kernel berjalan aman?

OS memastikan transisi user–kernel berjalan aman dengan menjaga stabilitas antarmuka modul kernel (Kernel Module Interface/KMI) dan menggunakan proses build hermetis yang konsisten. Dalam konteks Android, kernel dan modul vendor dibangun secara terpisah namun harus berfungsi seolah dibangun bersama, dengan hanya simbol KMI yang dikenal dan dibatasi agar dapat dipakai oleh modul vendor. Proses build hermetis menetapkan lingkungan build yang terkontrol dan menjamin konsistensi ABI (Application Binary Interface) sehingga mencegah modul yang tidak kompatibel dimuat, yang bisa mengancam keamanan transisi user-kernel. Semua ini memastikan bahwa kode yang dieksekusi saat pindah dari mode user ke kernel dapat dipercaya, mencegah kerusakan keamanan atau sistem akibat kode tidak sah atau rusak. Pendekatan ini meliputi pembekuan cabang KMI agar perubahan tidak merusak stabilitas, pengawasan simbol yang dipakai, dan menggunakan lingkungan build yang sepenuhnya dijelaskan untuk reproduksibilitas hasil build

- Sebutkan contoh system call yang sering digunakan di Linux.

3. Contoh system call yang sering digunakan di Linux adalah open, read, write, close, fork, exit, dan kill. Panggilan-panggilan ini memungkinkan program untuk berinteraksi dengan kernel sistem operasi untuk melakukan tugas-tugas seperti manajemen berkas, pembuatan proses baru, dan pengakhiran proses. 
-	open: Membuka berkas atau perangkat, memungkinkan program untuk berinteraksi dengannya (misalnya, membaca atau menulis). 
-	read: Membaca data dari berkas atau perangkat yang sudah dibuka. 
-	write: Menulis data ke berkas atau perangkat yang sudah dibuka. 
-	close: Menutup berkas atau perangkat setelah selesai digunakan untuk membebaskan sumber daya sistem. 
-	fork: Membuat salinan dari proses yang sedang berjalan, yang dikenal sebagai proses anak. Proses induk melanjutkan eksekusi sementara proses anak dimulai. 
-	exit: Mengakhiri eksekusi program atau utas saat ini dan memulihkan sumber daya yang digunakan. 
-	kill: Mengirim sinyal ke proses lain, seringkali untuk menghentikannya atau memerintahkannya melakukan tindakan tertentu. 
-	exec: Mengganti citra proses saat ini dengan program baru. Ini sering digunakan bersama dengan fork untuk menjalankan program yang berbeda dalam proses ana



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
