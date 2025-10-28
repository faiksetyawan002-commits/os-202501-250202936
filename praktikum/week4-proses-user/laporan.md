
# Laporan Praktikum Minggu IV
Topik: Proses user
---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.
3. Menggunakan perintah untuk membuat dan mengelola user.
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori
- Konsep User (Pengguna):
User adalah individu atau entitas yang berinteraksi dengan sistem komputer untuk menjalankan perintah, mengakses data, dan menggunakan sumber daya sistem.

- Identitas dan Autentikasi:
Setiap user memiliki identitas unik (username) dan kredensial (password atau token) untuk memastikan keamanan serta mencegah akses tidak sah ke sistem.

- Hak Akses dan Otorisasi:
Sistem memberikan hak akses tertentu (read, write, execute) kepada user sesuai perannya. Ini diatur melalui permission atau access control list.

- Manajemen Proses User:
Saat user menjalankan program, sistem membuat process atas nama user tersebut. Proses ini membawa identitas dan hak akses user untuk mengontrol apa yang dapat dilakukan di sistem.

- Isolasi dan Keamanan:
Setiap user dan prosesnya diisolasi untuk mencegah gangguan atau penyalahgunaan antar pengguna, mendukung stabilitas dan keamanan sist

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


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan ke repositori Git tepat waktu.

## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
