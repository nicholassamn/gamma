#!/usr/bin/env python3
"""
Demo dan Testing untuk Task Manager
Jalankan: python3 demo_task_manager.py
"""

import json
import os
import shutil
from task_manager import TaskManager, Task, Colors
from datetime import datetime, timedelta


def print_header(title):
    """Print header dengan gaya"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}▶ {title}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.RESET}\n")


def demo_basic_operations():
    """Demo operasi dasar"""
    print_header("DEMO 1: Operasi Dasar - Menambah dan Menampilkan Tugas")
    
    # Gunakan file demo terpisah agar tidak mengganggu data asli
    manager = TaskManager("demo_tasks.json")
    
    # Hapus file lama jika ada
    if os.path.exists("demo_tasks.json"):
        os.remove("demo_tasks.json")
    
    manager = TaskManager("demo_tasks.json")
    
    # Tambah beberapa tugas
    print(f"{Colors.GREEN}✓ Menambahkan tugas-tugas baru...{Colors.RESET}\n")
    
    manager.add_task(
        "Selesaikan presentasi",
        "Pekerjaan",
        (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "Presentasi untuk meeting dengan CEO"
    )
    
    manager.add_task(
        "Belajar Python async",
        "Pendidikan",
        (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
        "Pelajari asyncio dan concurrent programming"
    )
    
    manager.add_task(
        "Belanja kebutuhan rumah",
        "Pribadi",
        None,  # Tanpa deadline
        "Bersihkan rumah setiap minggu"
    )
    
    manager.add_task(
        "Jalan-jalan ke taman",
        "Kesehatan",
        (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "Olahraga santai untuk kesehatan"
    )
    
    # Tampilkan semua tugas
    print(f"{Colors.CYAN}Semua tugas yang telah ditambahkan:{Colors.RESET}")
    manager.display_tasks()


def demo_categorization():
    """Demo sistem kategori"""
    print_header("DEMO 2: Sistem Kategori - Filter dan Menampilkan")
    
    manager = TaskManager("demo_tasks.json")
    
    print(f"{Colors.CYAN}Kategori yang tersedia:{Colors.RESET}")
    manager.display_categories()
    
    print(f"\n{Colors.CYAN}Tugas kategori 'Pekerjaan':{Colors.RESET}")
    manager.display_tasks(category="Pekerjaan")
    
    print(f"{Colors.CYAN}Tugas kategori 'Pendidikan':{Colors.RESET}")
    manager.display_tasks(category="Pendidikan")


def demo_color_system():
    """Demo sistem warna berdasarkan deadline"""
    print_header("DEMO 3: Sistem Warna - Urgency Visualization")
    
    manager = TaskManager("demo_tasks.json")
    
    # Buat tugas dengan berbagai deadline untuk demo warna
    test_manager = TaskManager("color_test.json")
    if os.path.exists("color_test.json"):
        os.remove("color_test.json")
    
    test_manager = TaskManager("color_test.json")
    
    today = datetime.now().date()
    
    tasks_with_dates = [
        ("Deadline terlewat 2 hari lalu", "Demo", (today - timedelta(days=2)).strftime("%Y-%m-%d")),
        ("Deadline hari ini", "Demo", today.strftime("%Y-%m-%d")),
        ("Deadline besok", "Demo", (today + timedelta(days=1)).strftime("%Y-%m-%d")),
        ("Deadline 2 hari lagi", "Demo", (today + timedelta(days=2)).strftime("%Y-%m-%d")),
        ("Deadline 3 hari lagi", "Demo", (today + timedelta(days=3)).strftime("%Y-%m-%d")),
        ("Deadline 5 hari lagi", "Demo", (today + timedelta(days=5)).strftime("%Y-%m-%d")),
        ("Deadline 10 hari lagi", "Demo", (today + timedelta(days=10)).strftime("%Y-%m-%d")),
        ("Tugas tanpa deadline", "Demo", None),
    ]
    
    for title, category, deadline in tasks_with_dates:
        test_manager.add_task(title, category, deadline)
    
    print(f"{Colors.BOLD}{Colors.BLUE}Sistem Warna berdasarkan Deadline:{Colors.RESET}\n")
    print("Perhatikan warna text yang berbeda-beda sesuai kedekatan deadline:\n")
    
    test_manager.display_tasks()
    
    # Cleanup
    if os.path.exists("color_test.json"):
        os.remove("color_test.json")


def demo_task_completion():
    """Demo menandai tugas selesai"""
    print_header("DEMO 4: Menandai Tugas Selesai/Belum Selesai")
    
    manager = TaskManager("demo_tasks.json")
    
    print(f"{Colors.CYAN}Status awal - Semua tugas belum selesai:{Colors.RESET}")
    manager.display_tasks()
    
    print(f"\n{Colors.YELLOW}Menandai tugas pertama sebagai selesai...{Colors.RESET}\n")
    manager.mark_complete(0)
    
    print(f"{Colors.CYAN}Status setelah ditandai selesai:{Colors.RESET}")
    manager.display_tasks()
    
    print(f"\n{Colors.YELLOW}Menandai kembali ke belum selesai...{Colors.RESET}\n")
    manager.mark_complete(0)
    
    print(f"{Colors.CYAN}Status akhir:{Colors.RESET}")
    manager.display_tasks()


def demo_update_task():
    """Demo update tugas"""
    print_header("DEMO 5: Memperbarui Informasi Tugas")
    
    manager = TaskManager("demo_tasks.json")
    
    print(f"{Colors.CYAN}Tugas sebelum update:{Colors.RESET}")
    manager.display_tasks()
    
    print(f"\n{Colors.YELLOW}Update tugas pertama - mengubah judul dan deadline...{Colors.RESET}\n")
    manager.update_task(
        0,
        title="Selesaikan presentasi + dokumentasi",
        deadline=(datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    )
    
    print(f"\n{Colors.CYAN}Tugas setelah update:{Colors.RESET}")
    manager.display_tasks()


def demo_statistics():
    """Demo statistik"""
    print_header("DEMO 6: Statistik Tugas")
    
    manager = TaskManager("demo_tasks.json")
    
    # Tandai beberapa tugas selesai
    manager.mark_complete(1)
    manager.mark_complete(2)
    
    manager.display_statistics()


def demo_deletion():
    """Demo menghapus tugas"""
    print_header("DEMO 7: Menghapus Tugas")
    
    manager = TaskManager("demo_tasks.json")
    
    print(f"{Colors.CYAN}Tugas sebelum dihapus:{Colors.RESET}")
    manager.display_tasks()
    
    print(f"\n{Colors.YELLOW}Menghapus tugas dengan index 0...{Colors.RESET}\n")
    manager.delete_task(0)
    
    print(f"\n{Colors.CYAN}Tugas setelah dihapus:{Colors.RESET}")
    manager.display_tasks()


def demo_load_sample_data():
    """Demo memuat data sample"""
    print_header("DEMO 8: Memuat Data Sample dari JSON")
    
    print(f"{Colors.CYAN}Memuat contoh data dari tasks_example.json...{Colors.RESET}\n")
    
    # Copy sample data untuk demo
    if os.path.exists("tasks_example.json"):
        shutil.copy("tasks_example.json", "sample_demo.json")
        manager = TaskManager("sample_demo.json")
        
        print(f"{Colors.BLUE}Data sample yang dimuat:{Colors.RESET}\n")
        manager.display_tasks()
        
        print(f"{Colors.BLUE}Statistik data sample:{Colors.RESET}")
        manager.display_statistics()
        
        # Cleanup
        os.remove("sample_demo.json")
    else:
        print(f"{Colors.RED}File tasks_example.json tidak ditemukan!{Colors.RESET}")


def cleanup_demo_files():
    """Bersihkan file-file demo"""
    for file in ["demo_tasks.json", "color_test.json", "sample_demo.json"]:
        if os.path.exists(file):
            os.remove(file)


def main():
    """Jalankan semua demo"""
    print(f"\n{Colors.BOLD}{Colors.GREEN}")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║         TASK MANAGER - DEMO DAN TESTING PROGRAM              ║")
    print("║                                                               ║")
    print("║  Demo ini menunjukkan semua fitur utama dari Task Manager    ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print(Colors.RESET)
    
    try:
        # Jalankan semua demo
        demo_basic_operations()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_categorization()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_color_system()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_task_completion()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_update_task()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_statistics()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_deletion()
        input(f"\n{Colors.YELLOW}Tekan Enter untuk lanjut ke demo berikutnya...{Colors.RESET}")
        
        demo_load_sample_data()
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                    DEMO SELESAI!                             ║")
        print("║                                                               ║")
        print("║  Anda telah melihat semua fitur Task Manager                 ║")
        print("║  Sekarang jalankan: python3 task_manager.py                  ║")
        print("║  untuk menggunakan aplikasi secara interaktif!              ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print(Colors.RESET + "\n")
        
    finally:
        # Bersihkan file demo
        cleanup_demo_files()


if __name__ == "__main__":
    main()
