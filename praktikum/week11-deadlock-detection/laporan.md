
# Laporan Praktikum Minggu [X]
Topik: deaslock detection

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936  
- **Kelas** : 1IKRA

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. **Definisi Deadlock**
   Deadlock terjadi ketika sekelompok proses saling menunggu sumber daya yang dipegang oleh proses lain dalam kelompok tersebut, sehingga tidak ada proses yang dapat melanjutkan eksekusinya. Deadlock biasanya muncul pada sistem dengan sumber daya yang terbatas dan sharing yang kompleks.

2. **Kondisi Terjadinya Deadlock (Coffman Conditions)**
   Ada **empat kondisi** yang harus terpenuhi secara bersamaan agar deadlock terjadi:

   **Mutual exclusion**: Setiap sumber daya hanya dapat digunakan oleh satu proses pada satu waktu.
   **Hold and wait**: Proses yang memegang sumber daya bisa meminta sumber daya tambahan.
   **No preemption**: Sumber daya tidak dapat diambil paksa dari proses yang sedang menggunakannya.
   **Circular wait**: Terjadi rantai proses yang saling menunggu secara melingkar.

3. **Model Representasi Sumber Daya dan Proses**
   Deadlock detection menggunakan **resource-allocation graph (RAG)** atau tabel alokasi & permintaan sumber daya untuk merepresentasikan hubungan antara proses dan sumber daya. Siklus dalam grafik atau pola tertentu dalam tabel menandakan kemungkinan deadlock.

4. **Algoritma Deteksi Deadlock**
   Sistem operasi menggunakan algoritma untuk mendeteksi deadlock, misalnya:

   **Algoritma siklus pada RAG**: Mendeteksi apakah terdapat siklus yang menunjukkan deadlock.
   **Algoritma deteksi berbasis matriks**: Memeriksa status alokasi dan permintaan sumber daya untuk menemukan proses yang tidak dapat 

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```


---

## Kode / Perintah


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz dan Tugas
### Tugas
1. Buat program simulasi deteksi deadlock.  
2. Jalankan program dengan dataset uji.  
3. Sajikan hasil analisis dalam tabel dan narasi.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?

2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
-  semua sistem bisa mencegah deadlock: Beberapa sistem dengan permintaan sumber daya yang dinamis sulit menerapkan prevention atau avoidance.
- Overhead prevention/avoidance bisa tinggi: Mencegah deadlock kadang mengurangi efisiensi atau throughput sistem.
- Fleksibilitas: Dengan deteksi, sistem tetap berjalan normal, dan deadlock ditangani hanya ketika benar-benar terjadi.
- Sumber daya terbatas: Pada sistem real-time atau multi-user, terkadang lebih praktis mendeteksi dan memulihkan deadlock daripada membatasi alokasi secara ketat.
  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
Kelebihan:
- Lebih fleksibel dan efisien karena tidak membatasi alokasi sumber daya secara ketat.
- Cocok untuk sistem dengan sumber daya dinamis dan permintaan tak terprediksi.
- Sistem tetap bisa memproses sebagian besar proses tanpa hambatan.

Kekurangan:
- Deadlock sudah terjadi sebelum bisa ditangani → bisa menunda atau menghentikan proses.
- Perlu mekanisme pemulihan (recovery) seperti preemption atau killing proses, yang bisa kompleks.
- Algoritma deteksi bisa menimbulkan overhead tambahan jika dijalankan sering.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
