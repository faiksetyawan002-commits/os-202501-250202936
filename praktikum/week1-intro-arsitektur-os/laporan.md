
# Laporan Praktikum Minggu [X]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
Fungsi Utama Sistem Operasi
Sistem operasi (Operating System / OS) adalah perangkat lunak yang menjadi penghubung antara pengguna dan perangkat keras komputer.
Fungsi utamanya antara lain:
Manajemen Proses (Process Management)
Mengatur jalannya proses (program yang sedang berjalan).
Menangani pembuatan, penjadwalan, dan penghentian proses.
Manajemen Memori (Memory Management)
Mengalokasikan dan mengatur penggunaan memori utama (RAM).
Memastikan tiap proses mendapat memori tanpa saling mengganggu.
Manajemen Penyimpanan (File Management)
Mengatur penyimpanan data dalam bentuk file dan direktori.
Menyediakan sistem file untuk membaca, menulis, atau menghapus data
Manajemen Perangkat Input/Output Management
Mengontrol interaksi antara sistem dan perangkat keras 
Menggunakan driver agar OS bisa berkomunikasi dengan perangkat
Manajemen Keamanan dan Proteksi (Security & Protection)
Melindungi data dan sumber daya sistem dari akses tidak sah
Mengatur hak akses pengguna.
User Interface (Antarmuka Pengguna)
Menyediakan cara bagi pengguna untuk berinteraksi (CLI seperti terminal, atau GUI seperti Windows).

Peran Kernel
Kernel adalah inti dari sistem operasi — bagian terpenting yang selalu aktif di memori.
Fungsinya:
Mengatur komunikasi antara software dan hardware.
Mengelola sumber daya sistem (CPU, memori, perangkat I/O).
Melaksanakan system call dari aplikasi pengguna.
Menangani interupsi perangkat keras.

Jenis kernel:
Monolithic Kernel → seluruh layanan sistem dijalankan dalam satu ruang kernel (misal: Linux).
Microkernel → hanya fungsi dasar di kernel, layanan lain dijalankan di ruang pengguna (misal: Minix, QNX).

Peran System Call
System call adalah jembatan antara program pengguna (user space) dan kernel (kernel space).
Ketika aplikasi ingin menggunakan sumber daya sistem, ia tidak bisa langsung mengakses hardware, jadi harus meminta layanan ke kernel melalui system call.

Contoh system call:
read() → membaca data dari file atau perangkat.
write() → menulis data ke file atau perangkat.
fork() → membuat proses baru.
exec() → menjalankan program baru.
exit() → mengakhiri proses.
---

## Dasar Teori
Teori ini didasarkan pada konsep dasar ilmu komputer, khususnya manajemen sumber daya dan abstraksi hardware, untuk memahami bagaimana OS bekerja secara praktis (misalnya, melalui simulasi proses atau pemanggilan system call di lingkungan lab seperti Linux).

Abstraksi dan Manajemen Sumber Daya: Sistem operasi berfungsi sebagai lapisan abstraksi antara perangkat lunak pengguna dan hardware, mengelola sumber daya seperti CPU, memori, dan I/O untuk efisiensi dan keamanan. Teori ini (dari model von Neumann) memungkinkan multiprogramming, di mana percobaan dapat mendemonstrasikan penjadwalan proses untuk menghindari konflik sumber daya.

Peran Kernel sebagai Pengontrol Inti: Kernel adalah modul privileged yang menangani operasi rendah-level seperti interrupt dan context switching, berdasarkan teori mode eksekusi (user mode vs. kernel mode). Dalam percobaan, ini mendasari pengamatan bagaimana kernel mencegah akses langsung hardware oleh aplikasi, memastikan stabilitas sistem (contoh: kernel panic jika ada kesalahan).

System Call sebagai Interface Komunikasi: System call merupakan mekanisme trap-based untuk transisi dari user space ke kernel space, didasarkan pada teori isolasi proses (process isolation) untuk keamanan. Percobaan dapat menguji ini melalui pemanggilan fungsi seperti fork() atau read(), menunjukkan bagaimana library (e.g., POSIX API) membungkus permintaan kernel tanpa membahayakan sistem.

Prinsip Keamanan dan Portabilitas: Teori hak akses (access control) dan virtualisasi memastikan OS portabel antar hardware, dengan kernel menyediakan layanan standar. Ini mendasari percobaan evaluasi performa, seperti mengukur overhead system call, untuk memverifikasi bagaimana OS melindungi dari kegagalan (fault tolerance) dan mendukung skalabilitas.

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
 hasil screenshot percobaan atau diagram:


--<img width="1364" height="767" alt="screenshot wsl" src="https://github.com/user-attachments/assets/60200375-2d88-4ca6-9ecb-c4a5d8db1c4e" />
-

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
1. Makna Hasil Percobaan

Pada gambar terlihat beberapa perintah Linux dijalankan di terminal WSL2 (Windows Subsystem for Linux):
-whoami
Output: faik
→ Menampilkan nama pengguna aktif yang sedang menjalankan shell.
Ini menunjukkan kamu masuk sebagai user biasa, bukan root.

-lsmod
Menampilkan daftar modul kernel (kernel modules) yang sedang dimuat oleh sistem Linux.
Modul adalah komponen tambahan kernel yang bisa dimuat atau dilepaskan sesuai kebutuhan.

Contoh modul yang muncul:
intel_rapl_msr, crc32c_intel → modul yang mengelola fitur prosesor Intel.
bridge, br_netfilter → modul jaringan (bridge/virtual network).
autofs4 → modul untuk sistem file otomatis.
Makna: kernel sedang memuat berbagai modul untuk mengelola hardware dan fitur sistem tertentu tanpa harus memodifikasi kernel utama.

lsmod | head
Menampilkan beberapa baris awal dari daftar modul kernel.Gunanya untuk melihat ringkasan saja (misal 10 modul teratas).

dmesg | head
Menampilkan log pesan kernel saat proses booting (awal sistem hidup).
Baris awal menunjukkan:
Versi kernel: Linux version 6.6.87.2-microsoft-standard-WSL2
Compiler: gcc (GCC) 11.2.0
Arsitektur CPU: Intel/AMD
Peta memori fisik (RAM map)
Makna: ini adalah hasil output dari kernel log buffer, yaitu pesan yang dihasilkan kernel ketika mendeteksi perangkat keras dan menginisialisasi sistem.

2. Hubungan dengan Teori
Fungsi Kernel
Kernel adalah inti sistem operasi yang mengatur:
Manajemen perangkat keras (CPU, memori, I/O)
Pengaturan modul (seperti yang ditampilkan lsmod)
Penanganan interupsi, manajemen proses, dan file system
Perintah lsmod dan dmesg langsung berinteraksi dengan kernel space — keduanya memanfaatkan system call untuk meminta data dari kernel.

Peran System Call
System call digunakan untuk berkomunikasi antara user space (program aplikasi) dengan kernel space.
Contohnya:
Saat lsmod dijalankan, program melakukan system call seperti open(), read(), dan ioctl() untuk membaca data dari /proc/modules (yang dikelola oleh kernel).


---

## Kesimpulan
Sekali lagi, kernel adalah jantung sistem operasi; sistem operasi elementer memberi izin komunikasi antara komponen ssistem operasi dan perangkat keras. Ini juga diperlihatkan oleh kenyataan bahwa perintah lsmod dan dmesg memberikan daftar modul utama dan logger boot-up sistem, masing-masing. Sistem-sistem panggilan adalah petugas penghubung antara user space dan kernel space, sehingga yang membalas hingga aktivitas termina l. Sistemplet user-space ikut meminta jasa dari kernel tanpa harus meributkan ke perangkat kerasnya sehabis itu. WSL2 Linux Environment salah satunya kernel asli linux, karena itu ia menunjukkan informasiwayar modul dan logger sistemnya tanpa melaluicara cara lain – sesuatu yang benar-benar tidak bisa dijumpai di Windows, asalkarena mereka gunakan katajalur kernel dan API sistem yang berbeda.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:** Manajemen Sumber Daya, Manajemen Proses dan File, serta Penyediaan Antarmuka Pengguna  
2. [Pertanyaan 2]  
   **Jawaban:**  mode kernel memiliki akses penuh ke perangkat keras dan memori sistem, sementara mode pengguna memiliki akses yang dibatasi dan harus melalui system calls untuk meminta layanan dari kernel.
3. [Pertanyaan 3]  
   **Jawaban:**  Linux dan Windows

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  
1.terkendala di laptop karena laptop nya ngelag
2.dengan meminjam laptop teman
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
