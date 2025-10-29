
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
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---

## Hasil Eksekusi


---

## Analisis
2. eksperimen 2: Jelaskan setiap output dan fungsinya (whoami, id, groups)
3. eksperimen 3: Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND
4. eksperimen 4: Catat PID proses sleep
5. eksperimen 5: Amati hierarki proses dan identifikasi proses induk (init/systemd)

**jawaban**

2. `whoami`
- Fungsi:
Menampilkan nama user yang sedang aktif (login) di sistem saat ini.
Perintah ini sering digunakan untuk memastikan identitas user yang sedang menjalankan shell atau perintah.
- Contoh output:faik
- Penjelasan output:
Menunjukkan bahwa user yang sedang aktif atau menjalankan terminal adalah faik.

`id`

Fungsi:Menampilkan informasi identitas lengkap dari user, termasuk:
- UID (User ID)
- GID (Group ID)
- Kelompok tambahan (groups)

- Contoh output:uid=1000(faik) gid=1000(faik) groups=1000(faik),27(sudo)

- Penjelasan output:
   - uid=1000(faik) : ID unik user bernama faik adalah 1000.
   - gid=1000(faik) : ID grup utama user faik adalah 1000.
   - groups=1000(faik),27(sudo) : User faik termasuk dalam dua grup: faik dan sudo (berarti punya hak administratif).

`groups`
- Fungsi:Menampilkan daftar grup yang diikuti oleh user saat ini.
- Contoh output:faik sudo
- Penjelasan output:User faik adalah anggota dari dua grup: faik (grup utama) dan sudo (grup dengan hak akses administratif).

3. - PID (Process ID)
Artinya: Nomor unik yang diberikan oleh sistem untuk setiap proses yang sedang berjalan. Fungsinya Digunakan untuk mengidentifikasi dan mengontrol proses, misalnya ketika ingin menghentikan proses menggunakan kill PID.

- USER
Artinya: Nama pengguna (user) yang menjalankan proses tersebut.Fungsi nya Menunjukkan siapa pemilik proses, berguna untuk manajemen keamanan dan hak akses.

- %CPU
Artinya: Persentase penggunaan CPU oleh proses tersebut. Fungsi nya Menunjukkan seberapa besar beban prosesor yang digunakan proses itu, nilai tinggi berarti proses tersebut menggunakan banyak daya komputasi.

- %MEM
Artinya: Persentase penggunaan memori (RAM) oleh proses tersebut. Fungsi nya Memantau seberapa besar memori yang dikonsumsi, berguna untuk mengidentifikasi proses yang boros memori.

- COMMAND

Artinya: Nama atau perintah yang menjalankan proses. Fungsi nya menunjukkan program atau skrip apa yang sedang berjalan biasanya mencantumkan path atau argumen lengkap dari perintah tersebut.


4. - Analisis Hierarki:
Ini adalah proses pertama yang dijalankan oleh kernel saat sistem booting.
Fungsi systemd: Menginisialisasi seluruh sistem (mengganti peran lama init pada sistem modern).Menjalankan semua proses anak (child processes) seperti NetworkManager, sshd, cron, dan Mengatur lifecycle (start, stop, restart) layanan sistem.


## Kesimpulan
- Proses user merupakan proses yang dijalankan oleh pengguna di ruang pengguna (user space) dan berinteraksi dengan kernel melalui system call untuk menggunakan sumber daya sistem.
- Proses ini memastikan sistem dapat menjalankan banyak program secara terpisah, sehingga meningkatkan keamanan, stabilitas, dan efisiensi sistem operasi.


---
## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.

<img width="2082" height="882" alt="Untitled diagram-2025-10-28-115837" src="https://github.com/user-attachments/assets/1bd79a88-85c1-4416-a7b6-d96fce5ba810" />

 
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
  - User management berfungsi sebagai lapisan pengendali akses dan perlindungan data, yang secara langsung berkontribusi pada keamanan sistem Linux dengan memastikan bahwa hanya pengguna yang berwenang dapat melakukan tindakan tertentu di dalam sistem.
4. Upload laporan ke repositori Git tepat waktu.

## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
- Menjalankan proses awal setelah kernel aktif
Setelah kernel Linux selesai di-load, ia memanggil proses pertama — dulu init, sekarang umumnya systemd.
- Mengatur urutan booting sistem
systemd menjalankan layanan (service) seperti network, ssh, cron, dan lainnya sesuai dependensi dan urutan yang benar.
-Mengelola proses dan service
Dapat memulai, menghentikan, me-restart, dan memantau status service.


2. Apa perbedaan antara `kill` dan `killall`?
  - kill menargetkan proses tertentu berdasarkan PID.
  - killall menargetkan semua proses berdasarkan nama program. 
  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
   User root memiliki hak istimewa karena berperan sebagai superuser yang memiliki kendali penuh terhadap sistem Linux.



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
