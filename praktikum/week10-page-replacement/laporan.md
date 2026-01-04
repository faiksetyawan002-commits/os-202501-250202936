
# Laporan Praktikum Minggu X
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Faik Setyawan
- **NIM**   : 250202936  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. Page Replacement
Page replacement adalah mekanisme dalam sistem operasi yang digunakan untuk menentukan halaman (page) mana yang harus diganti ketika memori utama (RAM) telah penuh dan terjadi permintaan halaman baru. Tujuan utama dari page replacement adalah meminimalkan jumlah page fault agar kinerja sistem tetap optimal.

2. Page Fault dan Page Hit
Page fault terjadi ketika halaman yang dibutuhkan oleh proses tidak tersedia di memori utama sehingga sistem harus mengambilnya dari media penyimpanan sekunder (disk). Sebaliknya, page hit terjadi ketika halaman yang diminta sudah tersedia di memori. Semakin sedikit page fault, semakin baik performa sistem.

3. Algoritma FIFO (First In First Out)
FIFO merupakan algoritma page replacement yang mengganti halaman berdasarkan urutan kedatangan ke memori. Halaman yang pertama kali masuk akan menjadi halaman pertama yang diganti, tanpa mempertimbangkan apakah halaman tersebut masih sering digunakan atau tidak.

4. Algoritma LRU (Least Recently Used)
LRU adalah algoritma page replacement yang mengganti halaman yang paling lama tidak digunakan. Algoritma ini memanfaatkan riwayat penggunaan halaman dan bekerja berdasarkan prinsip locality of reference, yaitu halaman yang baru digunakan cenderung akan digunakan kembali dalam waktu dekat.

5. Belady’s Anomaly
Belady’s Anomaly adalah kondisi di mana penambahan jumlah frame memori justru dapat meningkatkan jumlah page fault. Fenomena ini dapat terjadi pada algoritma FIFO, namun tidak terjadi pada algoritma berbasis stack seperti LRU.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
FIFO
```
def fifo (pages, frames):
    memory = []
    recent = []
    page_faults = 0
    page_hits = 0

    print("FIFO Page Replacement\n")

    for page in pages:
        if page in memory:
            page_hits += 1
            print(f"Page", page ,": HIT   =",memory)
        else:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            print(f"Page", page ,": FAULT =",memory)

lanjutan ada di code
```
LRU 
```
def lru(pages, frames):
    memory = []
    recent = []
    page_faults = 0
    page_hits = 0

    print("\nLRU Page Replacement\n")

    for page in pages:
        if page in memory:
            page_hits += 1
            recent.remove(page)
            recent.append(page)
            print(f"Page", page ,": HIT   =",memory)
        else:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory[memory.index(lru_page)] = page
            recent.append(page)
            print(f"Page", page ,": FAULT =",memory)

lanjutan ada di code
```

---

## Hasil Eksekusi
code
<img width="1019" height="699" alt="code LRU" src="https://github.com/user-attachments/assets/f154d70d-375a-4204-a0ff-503632eae195" />
output
<img width="251" height="317" alt="output LRU" src="https://github.com/user-attachments/assets/748103f0-cd81-4a43-bd46-9a8068d1dd57" />
code
<img width="1022" height="664" alt="code FIFO" src="https://github.com/user-attachments/assets/b9771746-0bdc-4794-a808-ca973b4c4152" />
output
<img width="271" height="309" alt="output FIFO" src="https://github.com/user-attachments/assets/c9753be0-47fd-4e32-a30e-10c8651e1cc5" />



---

## Analisis
Buat tabel perbandingan seperti berikut:

| Algoritma | Jumlah Page Fault | Keterangan |
| --------- | ----------------- | ---------- |
| FIFO  | 0 | Mengganti halaman berdasarkan urutan masuk pertama, tanpa memperhatikan apakah halaman masih sering digunakan |
| LRU   | 9 | Mengganti halaman yang paling lama tidak digunakan, berdasarkan riwayat akses |

Jelaskan mengapa jumlah page fault bisa berbeda.

Perbedaan jumlah page fault terjadi karena cara masing-masing algoritma memilih halaman yang akan diganti berbeda:

FIFO (First In First Out)
Algoritma ini hanya melihat urutan kedatangan halaman, bukan frekuensi atau waktu penggunaan terakhir.
Akibatnya, halaman yang masih sering digunakan bisa ikut terhapus hanya karena masuk lebih awal.

LRU (Least Recently Used)
Algoritma ini mempertimbangkan riwayat penggunaan halaman.
Halaman yang jarang atau sudah lama tidak diakses akan diganti terlebih dahulu, sehingga halaman penting tetap berada di memori lebih lama

Analisis algoritma mana yang lebih efisien dan alasannya.

Algoritma yang lebih efisien pada simulasi ini adalah LRU (Least Recently Used). Hal ini dibuktikan dengan jumlah page fault yang lebih sedikit dibandingkan FIFO, yaitu 9 page fault pada LRU dan 10 page fault pada FIFO. Selain itu, LRU lebih sesuai dengan pola akses program pada sistem nyata, di mana halaman yang baru saja digunakan memiliki kemungkinan besar untuk digunakan kembali dalam waktu dekat. Dengan mempertahankan halaman yang sering diakses lebih lama di dalam memori, LRU mampu mengurangi frekuensi akses ke media penyimpanan sekunder, sehingga kinerja sistem secara keseluruhan menjadi lebih optimal.

---

## Kesimpulan
- Algoritma page replacement FIFO dan LRU berhasil diimplementasikan dan disimulasikan menggunakan dataset yang telah ditentukan dengan jumlah frame memori sebanyak tiga frame.

- Hasil simulasi menunjukkan bahwa algoritma LRU menghasilkan jumlah page fault yang lebih sedikit dibandingkan FIFO, sehingga LRU memiliki performa yang lebih baik dalam pengelolaan memori.

- LRU lebih efisien karena mempertimbangkan riwayat penggunaan halaman dan sesuai dengan pola akses program nyata, sehingga mampu mengurangi frekuensi akses ke media penyimpanan sekunder dan meningkatkan kinerja sistem secara keseluruhan..

---

## E. Tugas & Quiz
### Tugas
1. Buat program simulasi page replacement FIFO dan LRU.
2. Jalankan simulasi dengan dataset uji.
3. Sajikan hasil simulasi dalam tabel atau grafik.
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan utama FIFO dan LRU?

Perbedaan utama antara algoritma FIFO (First In First Out) dan LRU (Least Recently Used) terletak pada cara menentukan halaman yang akan diganti. FIFO mengganti halaman berdasarkan urutan kedatangan ke memori, tanpa memperhatikan apakah halaman tersebut masih sering digunakan atau tidak. Sebaliknya, LRU mengganti halaman yang paling lama tidak digunakan dengan mempertimbangkan riwayat akses halaman. Dengan demikian, LRU lebih adaptif terhadap pola penggunaan halaman pada program yang sedang berjalan.

2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?

FIFO dapat menghasilkan Belady’s Anomaly karena algoritma ini tidak mempertimbangkan frekuensi atau waktu penggunaan halaman. Pada kondisi tertentu, penambahan jumlah frame memori justru dapat menyebabkan jumlah page fault meningkat, karena halaman yang seharusnya masih dibutuhkan terhapus hanya berdasarkan urutan masuknya. Fenomena ini dikenal sebagai Belady’s Anomaly dan umumnya terjadi pada algoritma FIFO, tetapi tidak pada algoritma yang bersifat stack seperti LRU.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO? 

LRU umumnya menghasilkan performa yang lebih baik dibanding FIFO karena algoritma ini memanfaatkan prinsip locality of reference, yaitu kecenderungan program untuk mengakses kembali halaman yang baru saja digunakan. Dengan mempertahankan halaman yang sering diakses dan mengganti halaman yang jarang digunakan, LRU mampu mengurangi jumlah page fault. Hal ini berdampak langsung pada peningkatan kinerja sistem karena akses ke media penyimpanan sekunder dapat diminimalkan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
