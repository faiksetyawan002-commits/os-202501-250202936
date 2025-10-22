
# Laporan Praktikum Minggu III
Topik: linux fs permision
---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 2502020936  
- **Kelas** : 1IKRA

---

## Tujuan

Setelah menyelesaikan tugas ini, mahasiswa mampu:

Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
Menggunakan chmod dan chown untuk manajemen hak akses file.
Menjelaskan hasil output dari perintah Linux dasar.
Menyusun laporan praktikum dengan struktur yang benar.
Mengunggah dokumentasi hasil ke Git Repository tepat waktu.


---

## Dasar Teori

1. Tipe pengguna Setiap file atau direktori memiliki tiga jenis pengguna: owner (pemilik), group (grup), dan others (lainnya). Hak akses dapat berbeda untuk tiap kategori.

2. Tiga hak akses dasar:
   
- r (read) → baca isi file / list isi direktori
- w (write) → ubah isi file / tambah hapus file di direktori

3. Representasi permission:
   
- Secara simbolik: rwxr-xr-- (owner, group, others)
- Secara numerik (octal): 7=rwx, 6=rw-, 5=r-x, 4=r--, dst.

4. Perintah utama:
   
- chmod → ubah permission file/direktori
- chown → ubah pemilik dan/atau grup file

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1366" height="768" alt="Capture 7" src="https://github.com/user-attachments/assets/47eaac5e-37c1-47d2-af30-903bf4057d01" />


---

## Analisis
2. Jelaskan hasil tiap perintah.
- Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

**JAWAB:** 
- perintah pwd: Menampilkan direktori aktif (current working directory).
- perintah ls -l :Menampilkan daftar isi folder dengan format panjang (long listing), termasuk permission, pemilik, ukuran, dan tanggal modifikasi.
- perintah cd /tmp: indah direktori ke /tmp, folder sementara di Linux./tmp biasanya digunakan untuk file sementara yang bisa diakses oleh semua user.Setelah ini, direktori aktif (pwd) berubah menjadi /tmp.
- perintah ls -a : Menampilkan semua file di direktori, termasuk file tersembunyi (dimulai dengan titik .)

3. Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

**JAWAB**
- cat /etc/passwd menampilkan isi file /etc/passwd, yang berisi informasi semua user di sistem Linux.head -n 5 → menampilkan 5 baris pertama dari hasil cat.

struktur baris:
1. username	Nama user
2. password	Biasanya hanya x, berarti password disimpan di /etc/shadow
3. UID	User ID (angka unik untuk setiap user)
4. GID	Group ID utama user
5. GECOS	Informasi tambahan (nama lengkap, kontak, dsb)
6. home_directory	Lokasi folder home user
7. shell	Program shell default user (misal /bin/bash)

---

## Kesimpulan

Permission di Linux berfungsi sebagai mekanisme kontrol akses yang membatasi tindakan pengguna terhadap file dan direktori. Dengan pengaturan owner, group, dan others serta hak akses read, write, sistem dapat menjaga keamanan, mencegah perubahan tidak sah, dan memastikan integritas data. Perintah seperti chmod dan chown memudahkan administrator untuk mengelola hak akses secara fleksibel.

---

## Tugas 
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.
2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).
3. Analisis peran chmod dan chown dalam keamanan sistem Linux.
4. Upload hasil dan laporan ke repositori Git sebelum deadline.

**JAWAB**

1. 


| No | Perintah                                         | Hasil / Output                                                                                                                                                                                                     | Keterangan                                                                                     |
| -- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| 1  | `pwd`                                            | `/home/faik`                                                                                                                                                                                                       | Direktori aktif saat ini adalah `/home/faik`.                                                  |
| 2  | `ls -l`                                          | `total 0`                                                                                                                                                                                                          | Tidak ada file di direktori home saat ini.                                                     |
| 3  | `cd /tmp`                                        | -                                                                                                                                                                                                                  | Pindah ke direktori sementara `/tmp`.                                                          |
| 4  | `ls -a`                                          | `.  ..  .X11-unix  snap-private-tmp  systemd-private-9cc0e4d5f45a4aa0a66b501a35fb6b75-systemd-logind.service-MiTbZV ...`                                                                                           | Menampilkan semua file & folder termasuk **tersembunyi** (`.` dan `..`).                       |
| 5  | `cat /etc/passwd \| head -n 5`                   | `root:x:0:0:root:/root:/bin/bash`<br>`daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin`<br>`bin:x:2:2:bin:/bin:/usr/sbin/nologin`<br>`sys:x:3:3:sys:/dev:/usr/sbin/nologin`<br>`sync:x:4:65534:sync:/bin:/bin/sync` | Menampilkan **5 user pertama** di sistem; format: `username:password:UID:GID:GECOS:home:shell`. |
| 6  | `echo "Hello <Faik><250202936>" > percobaan.txt` | -                                                                                                                                                                                                                  | Membuat file `percobaan.txt` di `/tmp` berisi teks `Hello <Faik><250202936>`.                  |
| 7  | `ls -l percobaan.txt`                            | `-rw-r--r-- 1 faik faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | **Sebelum chmod:** Pemilik bisa baca/tulis; group & others hanya baca.                         |
| 8  | `chmod 600 percobaan.txt`                        | -                                                                                                                                                                                                                  | Mengubah permission file agar **hanya pemilik bisa baca & tulis**.                             |
| 9  | `ls -l percobaan.txt`                            | `-rw------- 1 faik faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | **Setelah chmod:** Group & others tidak punya akses.                                           |
| 10 | `sudo chown root percobaan.txt`                  | `[sudo] password for faik:`                                                                                                                                                                                        | Mengubah **pemilik file menjadi root**.                                                        |
| 11 | `ls -l percobaan.txt`                            | `-rw------- 1 root faik 24 Oct 21 17:32 percobaan.txt`                                                                                                                                                             | File sekarang **dimiliki root**, hanya root yang bisa baca/tulis karena permission `600`.      |

2.
- Owner	rwx	Bisa membaca, mengedit, dan menjalankan file
- Group	r-x	Bisa membaca & menjalankan, tapi tidak bisa mengedit
- Others	r--	Hanya bisa membaca file, tidak bisa mengubah atau menjalankan
- Jadi, rwxr-xr-- artinya Pemilik bisa baca, tulis, eksekusi, grup bisa baca & eksekusi, dan pengguna lain hanya bisa baca

3. chmod mengatur izin akses file atau direktori, menentukan siapa yang bisa membaca, menulis, atau mengeksekusi. Dengan chmod, file sensitif bisa dilindungi dari akses atau modifikasi oleh user yang tidak berwenang dan chown mengatur kepemilikan (user & group) file atau direktori. Dengan chown, hanya pemilik atau root yang bisa mengubah file, sehingga mencegah akses tidak sah dan menjaga tanggung jawab file.

   
## Quiz
1. Apa fungsi dari perintah chmod?
   **Jawaban:**  chmod digunakan untuk menentukan siapa yang bisa:membaca file (read / r),menulis atau mengubah file (write / w)dan menjalankan file (execute / x)
   
2. Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  Kode rwxr-xr-- adalah bentuk permission (izin akses) pada file atau direktori di sistem Linux (termasuk WSL).
   
3. Jelaskan perbedaan antara chown dan chmod?
   **Jawaban:**
- chmod (change mode) → mengubah izin akses file (baca, tulis, eksekusi).
- chown (change owner) → mengubah pemilik atau grup file.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  laptop kurang mendukung dalam pengerjaan tugas week 3
- Bagaimana cara Anda mengatasinya? meminjam laptop teman 
    

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
