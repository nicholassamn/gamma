# 📝 Task Manager - Aplikasi Manajemen Daftar Tugas

**Task Manager** adalah aplikasi baris perintah (CLI) yang powerful untuk mengelola daftar tugas harian Anda dengan mudah. Aplikasi ini dilengkapi dengan sistem deadline, kategori, dan interface yang user-friendly dengan warna-warna yang menarik.

---

## ✨ Fitur Utama

### 1. **Tambah Tugas Baru**
   - Membuat tugas dengan judul, kategori, dan deskripsi
   - Mendukung penambahan deadline (format: YYYY-MM-DD)
   - Kategori dapat dibuat secara fleksibel (Pekerjaan, Pribadi, Belanja, dll)

### 2. **Kelola Tugas**
   - ✅ **Tandai Selesai/Belum Selesai**: Toggle status tugas dengan mudah
   - 📝 **Update Tugas**: Edit judul, kategori, deadline, atau deskripsi
   - 🗑️ **Hapus Tugas**: Menghapus tugas yang tidak diperlukan
   - 📋 **Lihat Semua Tugas**: Menampilkan seluruh daftar tugas dengan format rapi

### 3. **Organisasi Berdasarkan Kategori**
   - Kelompokkan tugas berdasarkan kategori
   - Tampilkan tugas per kategori
   - Otomatis melacak kategori yang digunakan

### 4. **Sistem Deadline Cerdas**
   - Warna-kode visual berdasarkan urgensi:
     - 🔴 **Merah**: Deadline hari ini atau sudah terlewat
     - 🟠 **Oranye**: Deadline besok
     - 🟡 **Kuning**: 2-7 hari lagi
     - 🟢 **Hijau**: Lebih dari 7 hari atau tanpa deadline
   - Tampilkan sisa hari hingga deadline
   - Peringatan untuk tugas yang terlewat

### 5. **Statistik dan Analitik**
   - Total tugas, jumlah selesai, dan belum selesai
   - Persentase penyelesaian
   - Jumlah tugas dengan/tanpa deadline
   - Penghitung tugas yang terlewat

### 6. **Penyimpanan Data Otomatis**
   - Data disimpan dalam format JSON (`tasks.json`)
   - Semua perubahan disimpan secara otomatis
   - Data persisten antara session

---

## 🚀 Cara Penggunaan

### Menjalankan Aplikasi

```bash
python3 task_manager.py
```

Atau jika file executable:

```bash
./task_manager.py
```

### Menu Utama

Setelah menjalankan aplikasi, Anda akan melihat menu dengan 9 pilihan:

```
1. Lihat semua tugas
2. Lihat tugas berdasarkan kategori
3. Tambah tugas baru
4. Update tugas
5. Tandai tugas selesai/belum selesai
6. Hapus tugas
7. Lihat kategori
8. Lihat statistik
9. Keluar
```

---

## 📖 Panduan Penggunaan Setiap Menu

### 1️⃣ Lihat Semua Tugas

Menampilkan semua tugas yang Anda buat, dipisahkan menjadi dua bagian:
- **Tugas Belum Selesai**: Ditampilkan di atas dengan warna aktif
- **Tugas Selesai**: Ditampilkan di bawah dengan warna abu-abu

Setiap tugas menampilkan:
- Status (○ atau ✅)
- Judul tugas
- Kategori
- Informasi deadline
- Deskripsi (jika ada)

### 2️⃣ Lihat Tugas Berdasarkan Kategori

Untuk melihat tugas dalam kategori tertentu:
1. Sistem akan menampilkan semua kategori yang tersedia
2. Masukkan nama kategori yang ingin dilihat
3. Hanya tugas dalam kategori tersebut yang akan ditampilkan

### 3️⃣ Tambah Tugas Baru

Langkah-langkah menambah tugas:

1. Masukkan **judul tugas**
   ```
   Judul tugas: Selesaikan laporan
   ```

2. Masukkan **kategori** (baru atau yang sudah ada)
   ```
   Kategori: Pekerjaan
   ```

3. Tentukan apakah ada **deadline** (y/n)
   ```
   Apakah tugas ini memiliki deadline? (y/n): y
   ```

4. Jika ya, masukkan **deadline** dalam format YYYY-MM-DD
   ```
   Masukkan deadline (YYYY-MM-DD): 2026-02-15
   ```

5. Masukkan **deskripsi** (opsional)
   ```
   Deskripsi: Persiapkan data penjualan kuartal pertama
   ```

### 4️⃣ Update Tugas

Untuk mengubah informasi tugas yang sudah ada:

1. Sistem menampilkan semua tugas
2. Masukkan **nomor tugas** yang ingin diupdate
3. Untuk setiap field (judul, kategori, deadline, deskripsi):
   - Tekan **Enter** untuk melewati (tidak diubah)
   - Ketik nilai baru untuk mengubah

**Tips**: Tekan Enter kosong untuk menghapus deadline

### 5️⃣ Tandai Tugas Selesai/Belum Selesai

Untuk menandai status tugas:

1. Sistem menampilkan semua tugas
2. Masukkan **nomor tugas** yang statusnya akan diubah
3. Status akan otomatis berganti (selesai ↔ belum selesai)

### 6️⃣ Hapus Tugas

Untuk menghapus tugas:

1. Sistem menampilkan semua tugas
2. Masukkan **nomor tugas** yang akan dihapus
3. Konfirmasi penghapusan (y/n)
4. Tugas akan dihapus secara permanen

### 7️⃣ Lihat Kategori

Menampilkan semua kategori yang ada dengan statistik:
- Jumlah tugas aktif (belum selesai)
- Jumlah tugas selesai

### 8️⃣ Lihat Statistik

Menampilkan ringkasan statistik:
- Total tugas
- Jumlah dan persentase tugas selesai
- Jumlah dan persentase tugas belum selesai
- Tugas dengan deadline vs tanpa deadline
- Jumlah tugas yang terlewat

### 9️⃣ Keluar

Keluar dari aplikasi. Semua data akan disimpan otomatis.

---

## 📊 Format Data

Data tugas disimpan dalam file `tasks.json` dengan struktur:

```json
{
  "tasks": [
    {
      "title": "Selesaikan laporan",
      "category": "Pekerjaan",
      "deadline": "2026-02-15",
      "description": "Persiapkan data penjualan",
      "completed": false,
      "created_at": "2026-01-28 14:30:00"
    }
  ],
  "categories": ["Pekerjaan", "Pribadi"]
}
```

---

## 💡 Tips dan Trik

### Format Deadline
- Selalu gunakan format **YYYY-MM-DD** (contoh: 2026-02-15)
- Anda dapat menggunakan deadline di masa depan
- Sistem akan otomatis menghitung hari hingga deadline

### Kategori
- Gunakan kategori standar seperti: Pekerjaan, Pribadi, Belanja, Kesehatan, Pendidikan, Hiburan
- Anda dapat membuat kategori kustom sesuai kebutuhan
- Kategori bersifat case-sensitive (Pekerjaan ≠ pekerjaan)

### Warna Status
- Perhatikan warna latar belakang untuk mengetahui urgensi tugas
- Tugas merah memerlukan perhatian segera
- Gunakan statistik untuk memantau produktivitas

### Workflow Optimal
1. Mulai dengan membuat kategori umum
2. Tambahkan tugas dengan deadline yang realistis
3. Periksa tugas secara rutin
4. Tandai tugas yang selesai
5. Monitor statistik untuk motivasi

---

## 🛠️ Persyaratan

- **Python 3.6+**
- Tidak ada dependensi eksternal (menggunakan library bawaan Python)

---

## 📝 Lisensi

Aplikasi ini bebas digunakan dan dimodifikasi.

---

## ❓ Troubleshooting

### Masalah: File `tasks.json` tidak ditemukan
- **Solusi**: File akan dibuat otomatis saat Anda menambah tugas pertama

### Masalah: Format deadline tidak valid
- **Solusi**: Pastikan menggunakan format YYYY-MM-DD (contoh: 2026-02-15)

### Masalah: Data hilang
- **Solusi**: Pastikan file `tasks.json` ada di direktori yang sama dengan script
- Backup file secara berkala jika data sangat penting

---

Selamat menggunakan **Task Manager**! 🎉
