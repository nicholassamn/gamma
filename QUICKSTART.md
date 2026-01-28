# 🚀 Quick Start - Task Manager

Panduan cepat untuk memulai menggunakan Task Manager dalam 5 menit!

## ⚡ Instalasi (30 detik)

```bash
cd /workspaces/gamma
# Selesai! Tidak perlu install package lagi.
```

## 🎯 Jalankan Program Utama

```bash
python3 task_manager.py
```

Anda akan melihat menu seperti ini:

```
============================================================
📝 TASK MANAGER - MANAJEMEN DAFTAR TUGAS
============================================================

Pilihan Menu:
  1. Lihat semua tugas
  2. Lihat tugas berdasarkan kategori
  3. Tambah tugas baru
  4. Update tugas
  5. Tandai tugas selesai/belum selesai
  6. Hapus tugas
  7. Lihat kategori
  8. Lihat statistik
  9. Keluar
============================================================
```

## 📝 Contoh Penggunaan Cepat

### Menambah Tugas Baru (Menu 3)

```
Pilih menu (1-9): 3

Judul tugas: Belajar Python
Kategori: Pendidikan
Apakah tugas ini memiliki deadline? (y/n): y
Masukkan deadline (YYYY-MM-DD): 2026-02-15
Deskripsi (opsional): Pelajari async/await dan OOP
```

### Menambah Tugas Tanpa Deadline

```
Pilih menu (1-9): 3

Judul tugas: Membersihkan rumah
Kategori: Pribadi
Apakah tugas ini memiliki deadline? (y/n): n
Deskripsi: Bersihkan seluruh rumah setiap weekend
```

### Lihat Semua Tugas (Menu 1)

```
Pilih menu (1-9): 1

[Akan menampilkan daftar tugas dengan warna yang berbeda-beda]
```

### Lihat Tugas Berdasarkan Kategori (Menu 2)

```
Pilih menu (1-9): 2

Kategori yang tersedia:
  1. Pekerjaan (3 aktif, 2 selesai)
  2. Pendidikan (2 aktif, 0 selesai)
  3. Pribadi (1 aktif, 0 selesai)
  
Masukkan nama kategori: Pekerjaan

[Akan menampilkan hanya tugas kategori Pekerjaan]
```

### Tandai Tugas Selesai (Menu 5)

```
Pilih menu (1-9): 5

[Daftar tugas akan ditampilkan]

Masukkan nomor tugas: 0

✓ Tugas ditandai selesai!
```

### Lihat Statistik (Menu 8)

```
Pilih menu (1-9): 8

============================================================
📊 STATISTIK TUGAS
============================================================
  Total tugas: 10
  ✅ Selesai: 3 (30%)
  ○ Belum selesai: 7 (70%)
  📅 Dengan deadline: 8
  ∞ Tanpa deadline: 2
  ⚠️  Terlewat: 1
============================================================
```

## 🌈 Sistem Warna (Penting!)

Setiap tugas ditampilkan dengan warna yang berbeda tergantung deadline:

| Deadline | Warna | Arti |
|----------|-------|------|
| Sudah terlewat | 🔴 MERAH TEBAL | URGENT! Segera dikerjakan |
| Hari ini | 🔴 MERAH TEBAL | Deadline hari ini |
| Besok | 🟠 ORANGE TEBAL | Sangat mendekati |
| 2-3 hari | 🟠 ORANGE | Mendekati |
| 4-7 hari | 🟡 KUNING | Cukup waktu |
| >7 hari | 🟢 HIJAU | Masih lama |
| Tanpa deadline | 🟢 HIJAU | Fleksibel |
| Selesai | ⚫ ABU-ABU | Sudah dikerjakan |

## 💾 Data Disimpan Otomatis

Data Anda otomatis disimpan ke file `tasks.json` setiap kali:
- Menambah tugas
- Menghapus tugas
- Memperbarui tugas
- Menandai selesai

File ini dapat dibuka dengan text editor atau di-backup kapan saja.

## 🎓 Jalankan Demo (Opsional)

Untuk melihat semua fitur dalam aksi:

```bash
python3 demo_task_manager.py
```

Demo ini akan:
- ✅ Menunjukkan semua fitur utama
- ✅ Membuat data sample
- ✅ Menampilkan sistem warna
- ✅ Bersihkan file saat selesai

## 🧪 Jalankan Test (Opsional)

Untuk memverifikasi semua fungsi berjalan dengan baik:

```bash
python3 test_task_manager.py
```

Output yang sukses akan menunjukkan:
```
✓ SEMUA TEST BERHASIL!
```

## 📋 Format Tanggal

Selalu gunakan format: **YYYY-MM-DD**

Contoh:
- 2026-02-15 = 15 Februari 2026
- 2026-12-31 = 31 Desember 2026

## 🔄 Workflow Tipikal

```
1. Jalankan: python3 task_manager.py
2. Pilih menu 3: Tambah tugas
3. Isi detail tugas (judul, kategori, deadline)
4. Pilih menu 1: Lihat semua tugas untuk verifikasi
5. Pilih menu 8: Lihat statistik
6. Saat tugas selesai, pilih menu 5: Tandai selesai
7. Pilih menu 9: Keluar (data otomatis tersimpan)
```

## 🆘 Bantuan

### File tasks.json hilang?
Tidak apa-apa! File akan dibuat otomatis saat Anda menambah tugas pertama.

### Warna tidak muncul di terminal?
Gunakan terminal yang support ANSI colors:
- Linux/macOS: Gunakan terminal bawaan
- Windows: Gunakan Windows Terminal atau Git Bash

### Lupa format deadline?
Gunakan format: `YYYY-MM-DD`
Contoh: `2026-02-15`

## 📞 Tips

1. **Kategorisasi**: Gunakan kategori yang konsisten untuk easier filtering
2. **Deskripsi**: Catat detail penting di deskripsi
3. **Regular Check**: Buka statistik secara berkala untuk monitor progress
4. **Backup**: Salin `tasks.json` untuk backup manual

---

**Siap mulai?** Ketik `python3 task_manager.py` dan mulai mengelola tugas Anda!
