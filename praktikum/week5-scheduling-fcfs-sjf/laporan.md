
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

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

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

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

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
