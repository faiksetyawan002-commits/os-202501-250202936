
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936
- **Kelas** : 1IKRA
---

## Tujuan
MahasiSetelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan. swa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
1. Pengertian Scheduling

Scheduling (penjadwalan) adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses di CPU agar sumber daya digunakan secara efisien.

Tujuannya meliputi peningkatan throughput, utilisasi CPU, serta respons time yang optimal.

2. FCFS (First Come First Served)

Proses dijalankan berdasarkan urutan kedatangan di antrian.

Bersifat non-preemptive, artinya proses yang sedang berjalan tidak dapat dihentikan sebelum selesai.

Kelebihan: sederhana dan mudah diimplementasikan.

Kelemahan: dapat menyebabkan convoy effect (proses cepat menunggu proses lambat).

3. SJF (Shortest Job First)

Memilih proses dengan waktu eksekusi paling pendek terlebih dahulu.

Dapat bersifat non-preemptive atau preemptive (Shortest Remaining Time First).

Kelebihan: menghasilkan waktu tunggu rata-rata paling rendah.

Kelemahan: sulit mengetahui waktu proses secara akurat dan bisa menimbulkan starvation bagi proses panjang.

4. Perbandingan Umum

FCFS: adil dalam urutan, tetapi tidak efisien.

SJF: efisien secara waktu rata-rata, namun kurang adil terhadap proses besar.

5. Tujuan Akhir Scheduling

Menyeimbangkan antara efisiensi CPU, respons cepat, dan keadilan antar proses, tergantung pada kebijakan dan kebutuhan sistem.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P1 | 6 | 0 | 0 | 6 | 0 | 6 |
   | P2 | 8 | 1 | 6 | 14 | 5 | 13 |
   | P3 | 7 | 2 | 14 | 21 | 12 | 19 |
   | P4 | 3 | 3 | 21 | 24 | 18 | 21 |

   rata-rata Waiting Time (WT) = 8,75

   rata-rata Turnaround Time (TAT) = 14,75

   Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    14   21   24

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P4 | 3 | 3 | 3 | 6 | 0 | 3 |
   | P1 | 6 | 0 | 6  | 12  | 6  |  12 |
   | P3 | 7 | 2 | 12 | 19 | 10 | 17 |
   | P2 | 8 | 1 | 19  | 27 | 18  | 26 |
   
   rata-rata Waiting Time (WT) = 8,5
   rata-rata Turnaround Time (TAT) = 14,5

Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    12   19   27

   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |



4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan. 

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Hasil Eksekusi


---

## Analisis
- Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
- Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
- Tambahkan kesimpulan singkat di akhir laporan. 

**JAWABAN**

RATA RATA  FCFS 
- rata-rata Waiting Time (WT) = 8,75
- rata-rata Turnaround Time (TAT) = 14,75

RATA RATA FJS
- rata-rata Waiting Time (WT) = 8,5
- rata-rata Turnaround Time (TAT) = 14,5


SJF lebih unggul dari FCFS ketika:

- Waktu eksekusi (burst time) setiap proses sudah diketahui atau dapat diperkirakan dengan baik.
Karena SJF memilih proses dengan waktu terpendek, algoritma ini dapat meminimalkan waktu tunggu rata-rata dan meningkatkan efisiensi CPU.

- Proses-proses yang datang memiliki variasi burst time yang besar.
Dalam kondisi ini, SJF mampu menyelesaikan proses-proses kecil dengan cepat, sehingga total waktu tunggu keseluruhan menjadi jauh lebih kecil dibanding FCFS.

- Lingkungan sistem bersifat batch (non-interaktif).
Pada sistem batch, semua proses sudah diketahui di awal, sehingga mudah menentukan urutan yang paling efisien dengan SJF.


FCFS lebih unggul dari SJF ketika:

- Waktu kedatangan proses tidak dapat diprediksi dan burst time sulit diketahui.
FCFS tidak memerlukan perkiraan waktu eksekusi, jadi lebih sederhana dan mudah diterapkan dalam kondisi nyata.

- Lingkungan sistem bersifat interaktif atau multitasking.
Dalam sistem seperti ini, FCFS lebih adil karena setiap proses dilayani berdasarkan urutan datangnya, tanpa menunda proses panjang terlalu lama.

- Tujuan utama adalah keadilan, bukan efisiensi.
FCFS memastikan semua proses mendapat giliran secara berurutan, sehingga tidak terjadi starvation seperti pada SJF.








---

## Kesimpulan
- FCFS (First Come First Served) menjalankan proses berdasarkan urutan kedatangan — proses yang datang lebih dulu akan dijalankan lebih dulu. Metode ini sederhana namun dapat menyebabkan waktu tunggu tinggi bagi proses yang datang belakangan (efek convoy).

- SJF (Shortest Job First) memprioritaskan proses dengan waktu eksekusi terpendek, sehingga menghasilkan rata-rata waktu tunggu paling kecil dibanding FCFS.


---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

**JAWABAN**

1. 
![Screenshot hasil](<screenshots/FCFS dan SJF.png>)

2.    
 Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |
3. 
   
(1.) FCFS (First Come First Served)

Kelebihan:

- Sederhana dan mudah diimplementasikan.
- Adil dalam urutan kedatangan (tidak ada proses yang dilewati).
- Cocok untuk sistem batch (pekerjaan datang berurutan).

Kelemahan:

- Dapat menyebabkan waktu tunggu lama untuk proses pendek yang datang setelah proses panjang (convoy effect).
- Tidak efisien untuk sistem interaktif.
- Tidak mempertimbangkan prioritas atau waktu eksekusi proses.
 
 (2.) SJF (Shortest Job First)

Kelebihan:

- Memberikan rata-rata waktu tunggu dan waktu tinggal paling rendah.
- Efisien untuk sistem dengan banyak proses pendek.
- Mengoptimalkan pemanfaatan CPU.

Kelemahan:

- Sulit diterapkan karena lama burst time harus diketahui terlebih dahulu.
- Dapat menyebabkan starvation untuk proses yang panjang.
- Tidak cocok untuk sistem waktu nyata (real-time) yang memerlukan respon cepat untuk semua proses.



### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  

**jawaban**

(1). Berikut perbedaan utama antara FCFS dan SJF dalam teori CPU Scheduling:

1. Cara Penjadwalan

- FCFS (First Come First Served): Proses dijalankan berdasarkan urutan kedatangan — siapa datang dulu, dia dilayani dulu.

- SJF (Shortest Job First): Proses dengan waktu eksekusi (burst time) paling pendek dijalankan lebih dulu.

2. Kriteria Utama

- FCFS: Berdasarkan waktu kedatangan (arrival time).

- SJF: Berdasarkan durasi eksekusi (burst time).

3. Kinerja Sistem

- FCFS: Sederhana tetapi dapat menyebabkan convoy effect (proses pendek menunggu proses panjang).

- SJF: Lebih efisien, menghasilkan waktu tunggu rata-rata (average waiting time) lebih kecil.

4. Jenis Scheduling

- FCFS: Non-preemptive (tidak bisa dihentikan sebelum selesai).

- SJF: Bisa non-preemptive atau preemptive (versi preemptive disebut SRTF – Shortest Remaining Time First).

5. Kebutuhan Informasi

- FCFS: Tidak perlu tahu waktu eksekusi sebelumnya.

- SJF: Harus mengetahui atau memperkirakan waktu eksekusi proses terlebih dahulu.


(2). SJF: Harus mengetahui atau memperkirakan waktu eksekusi proses terlebih dahulu.SJF (Shortest Job First) menghasilkan rata-rata waktu tunggu paling minimum karena selalu mengeksekusi proses dengan waktu eksekusi terpendek terlebih dahulu. Dengan cara ini, proses-proses pendek tidak tertahan oleh proses panjang, sehingga total waktu tunggu seluruh proses menjadi lebih efisien dan sistem bekerja lebih cepat secara keseluruhan.

(3). Kelemahan SJF pada sistem interaktif:

- Sulit memperkirakan waktu eksekusi proses
SJF memerlukan informasi tentang burst time (lama proses berjalan), yang biasanya tidak diketahui sebelumnya pada sistem interaktif karena input pengguna dan proses bisa berubah-ubah.

- Proses panjang bisa terus tertunda (starvation)
Jika banyak proses pendek datang terus-menerus, proses yang lebih panjang bisa tidak pernah mendapat giliran menjalankan CPU.

- Tidak responsif untuk pengguna
Sistem interaktif memerlukan respons cepat. Karena SJF fokus pada efisiensi waktu tunggu rata-rata, bukan respons real-time, pengguna bisa merasa sistem lambat atau tidak responsif.

- Overhead dalam perhitungan dan penjadwalan
Untuk menentukan proses terpendek setiap saat, sistem harus memonitor dan memperkirakan waktu eksekusi secara terus-menerus, menambah beban kerja CPU (scheduling overhead).

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
