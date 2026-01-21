
# Laporan Praktikum Minggu [X]
Topik: Docker File 
---

## Identitas
- **Nama**  : Faik Setyawan   
- **NIM**   : 2502020936
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori

1. **Dockerfile sebagai Instruksi Pembuatan Image**
   Dockerfile merupakan berkas teks yang berisi kumpulan instruksi untuk membangun Docker image secara otomatis dan terstruktur.

2. **Otomatisasi dan Konsistensi Lingkungan**
   Dockerfile memungkinkan pembuatan lingkungan aplikasi yang konsisten pada berbagai sistem melalui proses build yang terstandarisasi.

3. **Konsep Layer pada Docker Image**
   Setiap instruksi dalam Dockerfile membentuk lapisan (*layer*) yang mendukung mekanisme cache, sehingga mempercepat proses build dan efisiensi penyimpanan.

4. **Kemudahan Reproduksi dan Deployment**
   Dockerfile memudahkan reproduksi lingkungan aplikasi serta mempercepat proses deployment karena konfigurasi telah terdokumentasi dengan jelas.

5. **Dukungan Kolaborasi dan Version Control**
   Dockerfile dapat dikelola menggunakan sistem kontrol versi, sehingga memudahkan kolaborasi dan pelacakan perubahan konfigurasi dalam pengembangan aplikasi.

---

## Langkah Praktikum
Langkah Pengerjaan
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bashs
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
---

## Kode / Perintah
```import time

data = [500]

print("=== UJI RESOURCE LIMIT DOCKER ===")

try:
    i = 0
    while True:
        i += 1

        # Bebani CPU
        x = i * i * i

        # Alokasi memori bertahap (1 MB)
        data.append("X" * 1024 * 1024)

        print(f"Iterasi: {i} | Memori terpakai: {len(data)} MB")
        time.sleep(0.1)

except MemoryError:
    print("ERROR: Memori tidak mencukupi!")

except Exception as e:
    print("Program dihentikan:", e)
```
dockerfile
```
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```
membuat dockerfile build 
```
docker build -t week13-resource-limit .
```
menjalankan container tanpa limir
``` 
docker run --rm week13-resource-limit .
```
menjalankan container dengan limit
```
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```

---

## Hasil Eksekusi
BUILD 
![HASIL](<screenshots/build container.png>)
TANPA LIMIT
![HASIL](<screenshots/container tanpa limit.png>)
DENGAN LIMIT
![HASIL](<screenshots/container dengan limit.png>) 
MONITORING SEDERHANA
![HASIL](<screenshots/monitoring sederhana.png>) 


---

##  Catatan output tanpa limit dan limit
tanpa limit
```
=== UJI RESOURCE LIMIT DOCKER ===
Iterasi: 1 | Memori terpakai: 1 MB
Iterasi: 2 | Memori terpakai: 2 MB
Iterasi: 3 | Memori terpakai: 3 MB
Iterasi: 4 | Memori terpakai: 4 MB
Iterasi: 5 | Memori terpakai: 5 MB
Iterasi: 6 | Memori terpakai: 6 MB
Iterasi: 7 | Memori terpakai: 7 MB
Iterasi: 8 | Memori terpakai: 8 MB
Iterasi: 120 | Memori terpakai: 120 MB
Iterasi: 121 | Memori terpakai: 121 MB
```
(Setiap iterasi menambah ±1 MB memori dan membebani CPU)

dengan limit



```
=== UJI RESOURCE LIMIT DOCKER ===
Iterasi: 1 | Memori terpakai: 1 MB
Iterasi: 2 | Memori terpakai: 2 MB
Iterasi: 3 | Memori terpakai: 3 MB
Iterasi: 4 | Memori terpakai: 4 MB
Iterasi: 5 | Memori terpakai: 5 MB
...
Iterasi: 120 | Memori terpakai: 120 MB
Iterasi: 256 | Memori terpakai: 256 MB
```

Setiap iterasi menambah ±1 MB memori.

Saat mendekati 256 MB, container dihentikan secara paksa oleh Docker.

Program tidak sempat menangkap MemoryError Python.



---

## Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Dockerfile berperan penting dalam mendefinisikan proses pembuatan image secara terstruktur dan konsisten. Dengan Dockerfile, aplikasi dapat dijalankan pada lingkungan yang sama tanpa bergantung pada sistem operasi host.

Pengujian menunjukkan bahwa container yang dijalankan **tanpa limit resource** dapat menggunakan CPU dan memori secara bebas hingga mengikuti kapasitas host, sehingga berpotensi mengganggu proses lain. Sebaliknya, penerapan **limit CPU dan memori** membuat eksekusi aplikasi menjadi lebih terkontrol. Program berjalan lebih lambat dan akan dihentikan secara paksa ketika penggunaan memori melebihi batas yang ditentukan.

Hal ini membuktikan bahwa pembatasan resource pada container sangat penting untuk menjaga stabilitas sistem, mencegah pemborosan resource, serta memastikan beberapa container dapat berjalan secara bersamaan dengan aman pada satu host.


---

## Tugas & Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
1. Mengapa container perlu dibatasi CPU dan memori?

Container perlu dibatasi CPU dan memori agar tidak menggunakan resource secara berlebihan yang dapat mengganggu container lain atau sistem host. Pembatasan ini membantu menjaga stabilitas sistem, meningkatkan efisiensi penggunaan resource, serta memastikan setiap aplikasi mendapatkan jatah resource yang sesuai.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

Virtual Machine (VM) memiliki isolasi resource yang lebih kuat karena setiap VM menjalankan sistem operasi sendiri di atas hypervisor, sehingga resource dialokasikan secara penuh. Sementara itu, container berbagi kernel sistem operasi host, sehingga isolasi resource lebih ringan dan efisien, namun bergantung pada mekanisme limit seperti CPU dan memori untuk menghindari konflik penggunaan resource.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?

Limit memori dapat menyebabkan aplikasi yang boros memori berjalan lebih lambat, mengalami error, atau bahkan dihentikan secara paksa (OOM Kill) oleh Docker ketika penggunaan memori melebihi batas yang ditentukan. Hal ini mendorong pengembang untuk membuat aplikasi yang lebih efisien dalam penggunaan memori.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
