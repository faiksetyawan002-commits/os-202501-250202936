
# Laporan Praktikum Minggu III
Topik: linux fs permision
---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 2502020936  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas 
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.
2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).
3. Analisis peran chmod dan chown dalam keamanan sistem Linux.
4. Upload hasil dan laporan ke repositori Git sebelum deadline.

**JAWAB**




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
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
