# Task Manager - Aplikasi Manajemen Daftar Tugas

Aplikasi Python untuk mengelola daftar tugas dengan fitur deadline, kategori, dan sistem warna yang dinamis berdasarkan urgency.

## 🎯 Fitur Utama

### 1. **Manajemen Tugas Fleksibel**
- ✅ Tambah tugas dengan atau tanpa deadline
- ✅ Edit dan perbarui tugas yang sudah ada
- ✅ Hapus tugas
- ✅ Tandai tugas sebagai selesai/belum selesai
- ✅ Tambahkan deskripsi detail untuk setiap tugas

### 2. **Sistem Kategori**
- 📂 Otomatis membuat kategori baru saat memasukkan tugas
- 📂 Filter dan lihat tugas berdasarkan kategori
- 📂 Cocok untuk mengelompokkan tugas:
  - Pekerjaan
  - Pribadi
  - Belanja
  - Kesehatan
  - Pendidikan
  - Hiburan
  - Dan kategori kustom lainnya

### 3. **Sistem Warna Dinamis Berdasarkan Deadline**
Warna berubah otomatis sesuai kedekatan deadline:

| Kondisi | Warna | Deskripsi |
|---------|-------|-----------|
| Terlewat | 🔴 Merah Bold | Deadline sudah lewat |
| Hari ini | 🔴 Merah Bold | Deadline hari ini |
| Besok | 🟠 Orange Bold | Deadline besok |
| 2-3 hari | 🟠 Orange | Deadline dalam 2-3 hari |
| 4-7 hari | 🟡 Kuning Bold | Deadline dalam 4-7 hari |
| >7 hari | 🟢 Hijau | Deadline lebih dari seminggu |
| Tanpa deadline | 🟢 Hijau | Tugas tanpa deadline |
| Selesai | ⚫ Abu-abu | Tugas yang sudah ditandai selesai |

### 4. **Statistik dan Analitik**
- 📊 Total tugas
- ✅ Jumlah tugas selesai dan persentase
- ○ Jumlah tugas belum selesai
- 📅 Tugas dengan/tanpa deadline
- ⚠️ Jumlah tugas yang terlewat deadline

### 5. **Penyimpanan Data Persisten**
- 💾 Otomatis menyimpan ke file JSON (`tasks.json`)
- 💾 Data tetap tersimpan saat program ditutup
- 💾 Mudah di-backup dan transfer

## 🚀 Cara Menggunakan

### Instalasi
```bash
# Tidak ada dependency eksternal! Hanya menggunakan library bawaan Python
cd /workspaces/gamma

# Jalankan program
python3 task_manager.py
```

### Menu Utama
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

### Contoh Penggunaan

#### Menambah Tugas dengan Deadline
```
Pilih menu (1-9): 3

Judul tugas: Selesaikan laporan project
Kategori: Pekerjaan
Apakah tugas ini memiliki deadline? (y/n): y
Masukkan deadline (YYYY-MM-DD): 2026-02-15
Deskripsi: Laporan harus lengkap dengan visualisasi data
```

#### Menambah Tugas tanpa Deadline
```
Pilih menu (1-9): 3

Judul tugas: Membaca buku Python
Kategori: Pendidikan
Apakah tugas ini memiliki deadline? (y/n): n
Deskripsi: Baca chapter 5-8
```

#### Melihat Tugas Berdasarkan Kategori
```
Pilih menu (1-9): 2

Kategori yang tersedia:
  1. Pekerjaan (3 aktif, 1 selesai)
  2. Pendidikan (2 aktif, 0 selesai)
  3. Belanja (1 aktif, 0 selesai)
```

## 📋 Format Data

Data disimpan dalam file `tasks.json` dengan format:

```json
{
  "tasks": [
    {
      "title": "Selesaikan laporan",
      "category": "Pekerjaan",
      "deadline": "2026-02-15",
      "description": "Laporan project quarterly",
      "completed": false,
      "created_at": "2026-01-28 10:30:45"
    }
  ],
  "categories": ["Pekerjaan", "Pendidikan", "Belanja"]
}
```

## 🎨 Fitur Visual

- **Warna Terminal**: Menggunakan ANSI color codes untuk tampilan yang menarik
- **Icons**: Menggunakan emoji untuk visual clarity
  - ✅ = Tugas selesai
  - ○ = Tugas belum selesai
  - 📋 = Daftar tugas
  - 📂 = Kategori
  - 📅 = Deadline
  - 📝 = Deskripsi
  - 📊 = Statistik

## 💡 Tips Penggunaan

1. **Gunakan Kategori Konsisten**: Gunakan nama kategori yang sama untuk tugas serupa agar lebih mudah dikelompokkan.

2. **Format Deadline**: Selalu gunakan format `YYYY-MM-DD` (contoh: `2026-02-15` untuk 15 Februari 2026)

3. **Deskripsi Detail**: Gunakan deskripsi untuk mencatat detail penting tugas Anda.

4. **Check Statistik Rutin**: Buka menu statistik secara berkala untuk monitor progress.

5. **Backup Data**: File `tasks.json` dapat di-backup dengan `cp tasks.json tasks_backup.json`

## 🔧 Struktur File

```
/workspaces/gamma/
├── task_manager.py           # Program utama
├── tasks.json                # File penyimpanan data (dibuat otomatis)
└── README_TASKMANAGER.md     # Dokumentasi ini
```

## 📝 Class dan Method

### Class `Colors`
Mendefinisikan ANSI color codes untuk terminal output.

### Class `Task`
Merepresentasikan satu tugas dengan atribut:
- `title`: Judul tugas
- `category`: Kategori tugas
- `deadline`: Tanggal deadline (opsional)
- `description`: Deskripsi detail
- `completed`: Status selesai/belum
- `created_at`: Waktu pembuatan

**Method penting:**
- `days_until_deadline()`: Hitung hari hingga deadline
- `get_color()`: Tentukan warna berdasarkan deadline
- `to_dict()` / `from_dict()`: Konversi untuk JSON

### Class `TaskManager`
Mengelola semua operasi tugas:
- `add_task()`: Tambah tugas baru
- `delete_task()`: Hapus tugas
- `mark_complete()`: Tandai selesai
- `update_task()`: Update tugas
- `display_tasks()`: Tampilkan tugas
- `load_tasks()` / `save_tasks()`: Manajemen file

## 🐛 Troubleshooting

### Program tidak berjalan
```bash
# Pastikan Python 3 terinstall
python3 --version

# Jalankan dengan Python 3 explicitly
python3 task_manager.py
```

### Warna tidak muncul
- Gunakan terminal yang support ANSI colors (sebagian besar terminal modern sudah support)
- Di Windows, gunakan Windows Terminal atau Git Bash

### File tasks.json corrupt
- Delete file `tasks.json`
- Program akan membuat file baru otomatis saat menambah tugas pertama

## 📦 Requirements

- **Python**: 3.6 atau lebih baru
- **Sistem Operasi**: Linux, macOS, Windows (dengan terminal yang support ANSI)
- **Dependencies**: Tidak ada! Hanya menggunakan library bawaan Python

## 📄 Lisensi

MIT License - Bebas digunakan untuk keperluan apapun.

## 👨‍💻 Pengembang

Dibuat dengan ❤️ menggunakan Python

---

**Catatan**: Program ini menggunakan library bawaan Python saja, tidak memerlukan instalasi package eksternal. Sempurna untuk pembelajaran dan penggunaan sehari-hari!
