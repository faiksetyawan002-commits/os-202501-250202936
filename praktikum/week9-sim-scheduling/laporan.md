
# Laporan Praktikum Minggu IX
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.
---

## Dasar Teori
Penjadwalan CPU (CPU Scheduling)
Penjadwalan CPU merupakan proses pengaturan urutan eksekusi beberapa proses oleh sistem operasi ketika CPU harus melayani lebih dari satu proses secara bersamaan.

Tujuan Penjadwalan
Tujuan utama penjadwalan CPU adalah meningkatkan efisiensi sistem, seperti mengurangi waktu tunggu proses (waiting time), mempercepat penyelesaian proses (turnaround time), serta menjaga agar CPU tidak menganggur.

Jenis Penjadwalan
Penjadwalan dibagi menjadi preemptive dan non-preemptive, di mana pada sistem preemptive proses dapat dihentikan sementara untuk memberi kesempatan pada proses lain yang memiliki prioritas lebih tinggi.

Parameter Penjadwalan
Dalam simulasi penjadwalan CPU, setiap proses memiliki parameter seperti waktu kedatangan (arrival time), lama eksekusi (burst time), dan prioritas, yang digunakan untuk menentukan urutan eksekusi proses.

Simulasi Algoritma Penjadwalan
Simulasi dilakukan untuk memahami cara kerja algoritma penjadwalan dan membandingkan kinerjanya, sehingga dapat diketahui algoritma mana yang paling efektif untuk kondisi tertentu.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
``

---

## Hasil Eksekusi
screenshot hasil 
![Screenshot hasil](screenshots/example.png)

---

## Analisis
   - Jelaskan alur program. 

   a. Inisialisasi Dataset

```processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]
```

processes → daftar proses

arrival_time → waktu kedatangan tiap proses

burst_time → lama eksekusi (CPU burst)

Jumlah proses disimpan dalam variabel n.

b. Inisialisasi Variabel Hasil
```
start_time = [0] * n
finish_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
````

Digunakan untuk menyimpan:

start_time → waktu proses mulai dieksekusi

finish_time → waktu proses selesai

waiting_time → waktu tunggu

turnaround_time → total waktu proses di sistem

c. Proses Penjadwalan FCFS
for i in range(n):


Loop digunakan untuk memproses setiap proses secara berurutan sesuai urutan kedatangan.

Proses pertama (P1)
```
start_time[i] = arrival_time[i]
```

Karena CPU masih kosong, proses langsung dieksekusi.

Proses berikutnya
```
start_time[i] = max(finish_time[i - 1], arrival_time[i])
```

Proses hanya bisa mulai jika:

CPU sudah selesai menjalankan proses sebelumnya

Proses tersebut sudah datang

d. Perhitungan Waktu
```
finish_time[i] = start_time[i] + burst_time[i]
waiting_time[i] = start_time[i] - arrival_time[i]
turnaround_time[i] = finish_time[i] - arrival_time[i]

```
Rumus:
```
Finish Time = Start Time + Burst Time

Waiting Time = Start Time − Arrival Time

Turnaround Time = Finish Time − Arrival Time
```
e. Perhitungan Rata-rata
```
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n
```

Digunakan untuk menilai kinerja algoritma FCFS.

   - Bandingkan hasil simulasi dengan perhitungan manual.  
   
   Hasil simulasi program sama dengan perhitungan manual, yang berarti algoritma diimplementasikan dengan benar.
Perbedaannya hanya pada cara pengerjaan:

Manual → lambat dan rawan kesalahan

Simulasi → cepat, konsisten, dan efisien

   - Jelaskan kelebihan dan keterbatasan simulasi.

Kelebihan Simulasi

1. Efisien untuk dataset besar
Tidak perlu menghitung satu per satu secara manual.

2. Akurasi tinggi
Mengurangi kesalahan manusia.

3. Mudah diuji ulang
Dataset bisa diganti tanpa mengubah logika.

4. Memudahkan perbandingan algoritma
Bisa langsung diterapkan ke FCFS, SJF, RR, dll.

Keterbatasan Simulasi

1. Tidak merepresentasikan kondisi sistem nyata sepenuhnya
Misalnya overhead context switching tidak dihitung.

2. Bergantung pada asumsi
Semua proses dianggap ideal (tidak ada I/O wait).

3. Membutuhkan pemahaman logika program
Kesalahan logika akan menghasilkan output yang salah.

---

## Kesimpulan
Simulasi algoritma penjadwalan CPU, khususnya FCFS, membantu memahami cara kerja penjadwalan proses secara sistematis berdasarkan waktu kedatangan.

Hasil simulasi yang diperoleh sesuai dengan perhitungan manual, sehingga dapat disimpulkan bahwa program yang dibuat telah berjalan dengan benar.

Penggunaan simulasi mempermudah analisis kinerja algoritma penjadwalan CPU, terutama dalam menghitung waiting time dan turnaround time secara efisien.

---

## Quiz dan Tugas
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.

## E. Tugas & Quiz
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  

Simulasi diperlukan karena algoritma scheduling bekerja dalam kondisi yang dinamis, seperti waktu kedatangan proses yang berbeda, variasi burst time, serta banyaknya proses yang berjalan bersamaan. Dengan simulasi, kita dapat meniru kondisi sistem operasi yang mendekati keadaan nyata tanpa harus menerapkannya langsung pada sistem sebenarnya. Simulasi juga membantu membandingkan kinerja beberapa algoritma (misalnya FCFS, SJF, Priority, Round Robin) berdasarkan metrik seperti waiting time, turnaround time, dan response time secara lebih objektif.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  


Pada dataset kecil, hasil simulasi dan perhitungan manual biasanya sama karena prosesnya masih mudah dilacak. Namun, jika dataset besar, perhitungan manual menjadi sangat kompleks, memakan waktu, dan rawan kesalahan manusia. Simulasi dengan bantuan program mampu mengolah data dalam jumlah besar secara cepat dan konsisten, sehingga hasilnya lebih akurat dan efisien dibandingkan perhitungan manual.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

Algoritma yang paling mudah diimplementasikan adalah First Come First Served (FCFS). Hal ini karena FCFS hanya membutuhkan satu antrian berdasarkan urutan kedatangan proses, tanpa perhitungan tambahan seperti prioritas atau time quantum. Logikanya sederhana dan mudah dipahami, sehingga sering digunakan sebagai algoritma dasar untuk pembelajaran, meskipun dari sisi performa tidak selalu optimal.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
