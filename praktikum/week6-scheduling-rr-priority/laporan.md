
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  
---

## Dasar Teori
- Konsep Dasar Scheduling:
CPU Scheduling adalah mekanisme untuk menentukan urutan eksekusi proses di dalam sistem agar penggunaan prosesor optimal. Tujuannya adalah meminimalkan waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time), serta meningkatkan efisiensi sistem.

- Algoritma Round Robin (RR):
Round Robin adalah algoritma penjadwalan preemptive yang memberikan setiap proses waktu eksekusi tetap yang disebut time quantum. Jika proses belum selesai dalam waktu tersebut, CPU akan berpindah ke proses berikutnya secara bergiliran. Algoritma ini adil dan cocok untuk sistem time-sharing.

- Algoritma Priority Scheduling:
Pada Priority Scheduling, setiap proses diberi tingkat prioritas. CPU akan dijalankan untuk proses dengan prioritas tertinggi terlebih dahulu. Jika menggunakan preemptive, proses baru dengan prioritas lebih tinggi dapat menghentikan proses yang sedang berjalan.

- Perbandingan Kedua Algoritma:

   - RR menekankan keadilan dan respon cepat, cocok untuk sistem interaktif.

   - Priority Scheduling menekankan tingkat kepentingan proses, tetapi dapat menimbulkan masalah starvation (proses prioritas rendah tidak pernah dieksekusi).
Kombinasi keduanya dapat menyeimbangkan antara keadilan dan efisiensi

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  

   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.
   
   | waktu | Brust | sisa waktu|
   |:-----:|:-----:|:---------:|
   | 0-3   | 5-3=0 | P1 sisa 2 |
   | 3-6   | 3-3=0 | 2 selesai |
   | 6-9   | 8-3=5 | P3 sisa 5 |
   | 9-12  | 6-3=3 | P4 sisa 3 |
   | 12-14 | 2 < 3 | P1 selesai|
   | 14-17 | 5-3=0 | P3 sisa 2 |
   | 17-20 | 3-3=0 | P4 selesai|
   | 20-22 | 2 < 3 | P3 selesai|
   

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]o
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  

Quantum 2
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	18 |  0 | 5 |	18 |  13|
|  P2  |	13 |	1 | 3 |	12 |	9 |
|  P3  |	24 |	2 | 8 |	22 |	14|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |   ||17.75|12.25|

Quantum 5
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	5  |  0 | 5 |	5  |  0 |
|  P2  |	8  |	1 | 3 |	7  |	4 |
|  P3  |	21 |	2 | 8 |	19 |	11|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |  || 12.5|  7 |




   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum 

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.  

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:

1.Apa perbedaan utama antara Round Robin dan Priority Scheduling?  

Perbedaan utama antara Round Robin (RR) dan Priority Scheduling 
-    Pada Round Robin, setiap proses diberi jatah waktu yang     sama (disebut time quantum). CPU menjalankan proses satu per satu secara bergiliran. Jika waktu jatah suatu proses habis dan proses itu belum selesai, maka proses tersebut dikembalikan ke antrean untuk menunggu giliran berikutnya. Metode ini dianggap paling adil, karena semua proses mendapat kesempatan yang sama untuk menggunakan CPU. Oleh karena itu, RR sangat cocok digunakan untuk sistem interaktif atau time-sharing, seperti sistem operasi multitasking.

Sedangkan 
- pada Priority Scheduling, CPU memilih proses berdasarkan tingkat prioritasnya. Proses dengan prioritas tertinggi akan dijalankan terlebih dahulu, sementara proses dengan prioritas lebih rendah harus menunggu. Metode ini cocok untuk sistem real-time atau batch, di mana beberapa tugas lebih penting daripada yang lain. Namun, kekurangannya adalah proses dengan prioritas rendah bisa menunggu terlalu lama, bahkan tidak sempat dijalankan (disebut starvation).

2.Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?

Jika time quantum terlalu kecil:

   - CPU akan sering berpindah dari satu proses ke proses lain (terjadi banyak context switch).

   - Akibatnya, waktu CPU banyak terbuang hanya untuk berpindah konteks, bukan menjalankan proses.

   - Sistem memang terasa responsif, tetapi efisiensinya menurun karena overhead meningkat.

Jika time quantum terlalu besar:

   - Proses akan berjalan lebih lama sebelum digantikan proses lain.

   - Sistem menjadi kurang responsif, terutama bagi pengguna yang menunggu giliran proses lain.

   - Penjadwalan cenderung menyerupai FCFS (First Come First Served), sehingga keadilan antar proses berkurang.


3.Mengapa algoritma Priority dapat menyebabkan *starvation*?  

Dalam algoritma ini, CPU selalu memilih proses dengan prioritas tertinggi untuk dijalankan terlebih dahulu. Jika terus-menerus ada proses baru dengan prioritas lebih tinggi yang masuk ke sistem, maka proses dengan prioritas rendah akan terus menunggu tanpa batas waktu. Kondisi inilah yang disebut starvation (kelaparan CPU time).

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
