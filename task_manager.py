#!/usr/bin/env python3
"""
Task Manager - Aplikasi Manajemen Daftar Tugas dengan Deadline dan Kategori
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Optional, Dict
from pathlib import Path
import sys

# Warna ANSI untuk terminal
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    ORANGE = '\033[38;5;208m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    
    # Background colors untuk highlight
    BG_RED = '\033[41m'
    BG_ORANGE = '\033[48;5;208m'
    BG_YELLOW = '\033[43m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_GRAY = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


class Task:
    """Kelas untuk merepresentasikan sebuah tugas"""
    
    def __init__(self, title: str, category: str, deadline: Optional[str] = None, description: str = ""):
        self.title = title
        self.category = category
        self.deadline = deadline  # Format: YYYY-MM-DD
        self.description = description
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict:
        """Konversi task ke dictionary untuk penyimpanan"""
        return {
            'title': self.title,
            'category': self.category,
            'deadline': self.deadline,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        """Buat Task dari dictionary"""
        task = Task(
            data['title'],
            data['category'],
            data.get('deadline'),
            data.get('description', '')
        )
        task.completed = data.get('completed', False)
        task.created_at = data.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return task
    
    def days_until_deadline(self) -> Optional[int]:
        """Hitung hari hingga deadline. Negatif jika sudah terlewat."""
        if not self.deadline:
            return None
        
        try:
            deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d").date()
            today = datetime.now().date()
            delta = (deadline_date - today).days
            return delta
        except ValueError:
            return None
    
    def get_color(self) -> tuple:
        """Dapatkan warna berdasarkan deadline"""
        if self.completed:
            return Colors.DARK_GRAY, Colors.RESET
        
        if not self.deadline:
            return Colors.GREEN, Colors.RESET
        
        days = self.days_until_deadline()
        
        if days is None:
            return Colors.BLUE, Colors.RESET
        
        # Sistem warna berdasarkan jarak deadline
        if days < 0:  # Terlewat
            return Colors.BG_RED + Colors.BOLD, Colors.RESET
        elif days == 0:  # Hari ini
            return Colors.BG_RED + Colors.BOLD + Colors.LIGHT_GRAY, Colors.RESET
        elif days == 1:  # Besok
            return Colors.BG_ORANGE + Colors.BOLD, Colors.RESET
        elif days <= 3:  # 2-3 hari lagi
            return Colors.ORANGE + Colors.BOLD, Colors.RESET
        elif days <= 7:  # 4-7 hari lagi
            return Colors.YELLOW + Colors.BOLD, Colors.RESET
        else:  # Lebih dari seminggu
            return Colors.GREEN, Colors.RESET


class TaskManager:
    """Kelas utama untuk mengelola daftar tugas"""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.categories: set = set()
        self.load_tasks()
    
    def load_tasks(self):
        """Muat tugas dari file JSON"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task) for task in data.get('tasks', [])]
                    self.categories = set(data.get('categories', []))
            except json.JSONDecodeError:
                print(f"{Colors.RED}Error membaca file {self.data_file}{Colors.RESET}")
                self.tasks = []
                self.categories = set()
        
        # Update categories dari tasks yang ada
        for task in self.tasks:
            self.categories.add(task.category)
    
    def save_tasks(self):
        """Simpan tugas ke file JSON"""
        data = {
            'tasks': [task.to_dict() for task in self.tasks],
            'categories': list(self.categories)
        }
        
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"{Colors.RED}Error menyimpan file: {e}{Colors.RESET}")
    
    def add_task(self, title: str, category: str, deadline: Optional[str] = None, description: str = ""):
        """Tambah tugas baru"""
        if not title or not category:
            print(f"{Colors.RED}Judul dan kategori tidak boleh kosong!{Colors.RESET}")
            return False
        
        # Validasi format deadline
        if deadline:
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
            except ValueError:
                print(f"{Colors.RED}Format deadline tidak valid. Gunakan YYYY-MM-DD{Colors.RESET}")
                return False
        
        task = Task(title, category, deadline, description)
        self.tasks.append(task)
        self.categories.add(category)
        self.save_tasks()
        
        print(f"{Colors.GREEN}✓ Tugas '{title}' berhasil ditambahkan!{Colors.RESET}")
        return True
    
    def delete_task(self, index: int):
        """Hapus tugas berdasarkan index"""
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.save_tasks()
            print(f"{Colors.GREEN}✓ Tugas '{task.title}' berhasil dihapus!{Colors.RESET}")
            return True
        else:
            print(f"{Colors.RED}Index tidak valid!{Colors.RESET}")
            return False
    
    def mark_complete(self, index: int):
        """Tandai tugas sebagai selesai"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            status = "selesai" if self.tasks[index].completed else "belum selesai"
            self.save_tasks()
            print(f"{Colors.GREEN}✓ Tugas ditandai {status}!{Colors.RESET}")
            return True
        else:
            print(f"{Colors.RED}Index tidak valid!{Colors.RESET}")
            return False
    
    def update_task(self, index: int, title: Optional[str] = None, category: Optional[str] = None,
                   deadline: Optional[str] = None, description: Optional[str] = None):
        """Update informasi tugas"""
        if not (0 <= index < len(self.tasks)):
            print(f"{Colors.RED}Index tidak valid!{Colors.RESET}")
            return False
        
        task = self.tasks[index]
        
        if title is not None:
            task.title = title
        if category is not None:
            task.category = category
            self.categories.add(category)
        if deadline is not None:
            if deadline == "":
                task.deadline = None
            else:
                try:
                    datetime.strptime(deadline, "%Y-%m-%d")
                    task.deadline = deadline
                except ValueError:
                    print(f"{Colors.RED}Format deadline tidak valid. Gunakan YYYY-MM-DD{Colors.RESET}")
                    return False
        if description is not None:
            task.description = description
        
        self.save_tasks()
        print(f"{Colors.GREEN}✓ Tugas berhasil diperbarui!{Colors.RESET}")
        return True
    
    def display_tasks(self, category: Optional[str] = None, show_completed: bool = True):
        """Tampilkan daftar tugas dengan format yang rapi"""
        if not self.tasks:
            print(f"\n{Colors.CYAN}Tidak ada tugas. Mulai dengan menambah tugas baru!{Colors.RESET}\n")
            return
        
        # Filter tasks
        filtered_tasks = self.tasks
        if category:
            filtered_tasks = [t for t in self.tasks if t.category == category]
        
        if not filtered_tasks:
            print(f"\n{Colors.CYAN}Tidak ada tugas di kategori '{category}'.{Colors.RESET}\n")
            return
        
        # Pisahkan completed dan incomplete
        incomplete_tasks = [t for t in filtered_tasks if not t.completed]
        completed_tasks = [t for t in filtered_tasks if t.completed]
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*120}{Colors.RESET}")
        
        # Tampilkan incomplete tasks
        if incomplete_tasks:
            print(f"{Colors.BOLD}{Colors.BLUE}📋 TUGAS BELUM SELESAI{Colors.RESET}")
            print(f"{Colors.CYAN}{'='*120}{Colors.RESET}")
            
            for idx, task in enumerate(incomplete_tasks, 1):
                actual_index = self.tasks.index(task)
                self._print_task(idx, task, actual_index)
        
        # Tampilkan completed tasks jika ada
        if completed_tasks and show_completed:
            print(f"\n{Colors.BOLD}{Colors.DARK_GRAY}✅ TUGAS SELESAI{Colors.RESET}")
            print(f"{Colors.CYAN}{'='*120}{Colors.RESET}")
            
            for idx, task in enumerate(completed_tasks, len(incomplete_tasks) + 1):
                actual_index = self.tasks.index(task)
                self._print_task(idx, task, actual_index)
        
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*120}{Colors.RESET}\n")
    
    def _print_task(self, display_idx: int, task: Task, actual_index: int):
        """Helper untuk mencetak satu task dengan formatnya"""
        color, reset = task.get_color()
        
        # Status icon
        if task.completed:
            status = "✅"
        else:
            status = "○"
        
        # Format deadline info
        if task.deadline:
            days = task.days_until_deadline()
            if days is None:
                deadline_str = f"[Invalid: {task.deadline}]"
            elif days < 0:
                deadline_str = f"[Terlewat {abs(days)} hari]"
            elif days == 0:
                deadline_str = "[Hari ini!]"
            else:
                deadline_str = f"[{days} hari lagi]"
        else:
            deadline_str = "[Tanpa deadline]"
        
        # Category badge
        category_colors = {
            'Pekerjaan': Colors.BLUE,
            'Pribadi': Colors.PURPLE,
            'Belanja': Colors.YELLOW,
            'Kesehatan': Colors.RED,
            'Pendidikan': Colors.CYAN,
            'Hiburan': Colors.MAGENTA if hasattr(Colors, 'MAGENTA') else Colors.PURPLE,
        }
        cat_color = category_colors.get(task.category, Colors.BLUE)
        
        # Print task info
        print(f"{Colors.BOLD}[{actual_index}]{Colors.RESET} {status} {color}{Colors.BOLD}{task.title}{reset}")
        print(f"    📂 {cat_color}{task.category}{Colors.RESET} | 📅 {deadline_str}")
        
        if task.deadline:
            print(f"    📌 Deadline: {task.deadline}")
        
        if task.description:
            print(f"    📝 {task.description}")
        
        print()
    
    def display_categories(self):
        """Tampilkan semua kategori yang tersedia"""
        if not self.categories:
            print(f"{Colors.CYAN}Tidak ada kategori.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}Kategori yang tersedia:{Colors.RESET}")
        for idx, category in enumerate(sorted(self.categories), 1):
            count = len([t for t in self.tasks if t.category == category and not t.completed])
            completed = len([t for t in self.tasks if t.category == category and t.completed])
            print(f"  {idx}. {category} ({count} aktif, {completed} selesai)")
        print()
    
    def display_statistics(self):
        """Tampilkan statistik tugas"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        incomplete = total - completed
        
        # Tugas dengan deadline
        with_deadline = len([t for t in self.tasks if t.deadline])
        without_deadline = total - with_deadline
        
        # Deadline yang terlewat
        overdue = len([t for t in self.tasks if not t.completed and t.deadline and t.days_until_deadline() is not None and t.days_until_deadline() < 0])
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}📊 STATISTIK TUGAS{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"  Total tugas: {Colors.BOLD}{total}{Colors.RESET}")
        print(f"  ✅ Selesai: {Colors.GREEN}{completed}{Colors.RESET} ({completed*100//total if total > 0 else 0}%)")
        print(f"  ○ Belum selesai: {Colors.YELLOW}{incomplete}{Colors.RESET} ({incomplete*100//total if total > 0 else 0}%)")
        print(f"  📅 Dengan deadline: {with_deadline}")
        print(f"  ∞ Tanpa deadline: {without_deadline}")
        if overdue > 0:
            print(f"  ⚠️  Terlewat: {Colors.RED}{overdue}{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*60}{Colors.RESET}\n")


def print_menu():
    """Tampilkan menu utama"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}📝 TASK MANAGER - MANAJEMEN DAFTAR TUGAS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"""
{Colors.BOLD}Pilihan Menu:{Colors.RESET}
  {Colors.GREEN}1.{Colors.RESET} Lihat semua tugas
  {Colors.GREEN}2.{Colors.RESET} Lihat tugas berdasarkan kategori
  {Colors.GREEN}3.{Colors.RESET} Tambah tugas baru
  {Colors.GREEN}4.{Colors.RESET} Update tugas
  {Colors.GREEN}5.{Colors.RESET} Tandai tugas selesai/belum selesai
  {Colors.GREEN}6.{Colors.RESET} Hapus tugas
  {Colors.GREEN}7.{Colors.RESET} Lihat kategori
  {Colors.GREEN}8.{Colors.RESET} Lihat statistik
  {Colors.GREEN}9.{Colors.RESET} Keluar
{Colors.CYAN}{'='*60}{Colors.RESET}
""")


def get_valid_date(prompt: str, allow_empty: bool = False) -> Optional[str]:
    """Dapatkan input tanggal yang valid"""
    while True:
        date_str = input(f"{Colors.BOLD}{prompt}{Colors.RESET}").strip()
        
        if not date_str and allow_empty:
            return None
        
        if not date_str:
            print(f"{Colors.RED}Tanggal tidak boleh kosong!{Colors.RESET}")
            continue
        
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print(f"{Colors.RED}Format tidak valid. Gunakan YYYY-MM-DD (contoh: 2026-02-15){Colors.RESET}")


def main():
    """Fungsi utama"""
    manager = TaskManager()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}Selamat datang di Task Manager!{Colors.RESET}\n")
    
    while True:
        print_menu()
        choice = input(f"{Colors.BOLD}Pilih menu (1-9): {Colors.RESET}").strip()
        
        if choice == '1':
            # Lihat semua tugas
            manager.display_tasks()
        
        elif choice == '2':
            # Lihat tugas berdasarkan kategori
            manager.display_categories()
            category = input(f"{Colors.BOLD}Masukkan nama kategori: {Colors.RESET}").strip()
            if category:
                manager.display_tasks(category=category)
        
        elif choice == '3':
            # Tambah tugas baru
            print(f"\n{Colors.BOLD}{Colors.CYAN}Tambah Tugas Baru{Colors.RESET}")
            title = input(f"{Colors.BOLD}Judul tugas: {Colors.RESET}").strip()
            
            if not title:
                print(f"{Colors.RED}Judul tidak boleh kosong!{Colors.RESET}")
                continue
            
            # Pilih kategori yang ada atau buat baru
            if manager.categories:
                print(f"\n{Colors.CYAN}Kategori yang tersedia: {', '.join(sorted(manager.categories))}{Colors.RESET}")
                print(f"{Colors.DIM}Ketik kategori yang ada atau masukkan nama baru{Colors.RESET}")
            
            category = input(f"{Colors.BOLD}Kategori: {Colors.RESET}").strip()
            
            if not category:
                print(f"{Colors.RED}Kategori tidak boleh kosong!{Colors.RESET}")
                continue
            
            # Tanyakan deadline
            has_deadline = input(f"{Colors.BOLD}Apakah tugas ini memiliki deadline? (y/n): {Colors.RESET}").strip().lower()
            
            deadline = None
            if has_deadline == 'y':
                deadline = get_valid_date("Masukkan deadline (YYYY-MM-DD): ")
            
            # Deskripsi opsional
            description = input(f"{Colors.BOLD}Deskripsi (opsional, tekan Enter untuk skip): {Colors.RESET}").strip()
            
            manager.add_task(title, category, deadline, description)
        
        elif choice == '4':
            # Update tugas
            manager.display_tasks()
            try:
                index = int(input(f"{Colors.BOLD}Masukkan nomor tugas yang akan diupdate: {Colors.RESET}"))
                
                if 0 <= index < len(manager.tasks):
                    task = manager.tasks[index]
                    print(f"\n{Colors.BOLD}Update Tugas: {task.title}{Colors.RESET}")
                    print(f"{Colors.DIM}(Tekan Enter untuk skip field){Colors.RESET}\n")
                    
                    new_title = input(f"{Colors.BOLD}Judul baru ({task.title}): {Colors.RESET}").strip() or None
                    new_category = input(f"{Colors.BOLD}Kategori baru ({task.category}): {Colors.RESET}").strip() or None
                    
                    new_deadline = None
                    change_deadline = input(f"{Colors.BOLD}Ubah deadline? (y/n): {Colors.RESET}").strip().lower()
                    if change_deadline == 'y':
                        has_deadline = input(f"{Colors.BOLD}Apakah ada deadline? (y/n): {Colors.RESET}").strip().lower()
                        if has_deadline == 'y':
                            new_deadline = get_valid_date("Masukkan deadline baru (YYYY-MM-DD): ")
                        else:
                            new_deadline = ""
                    
                    new_description = input(f"{Colors.BOLD}Deskripsi baru ({task.description}): {Colors.RESET}").strip() or None
                    
                    manager.update_task(index, new_title, new_category, new_deadline, new_description)
                else:
                    print(f"{Colors.RED}Nomor tidak valid!{Colors.RESET}")
            
            except ValueError:
                print(f"{Colors.RED}Input tidak valid!{Colors.RESET}")
        
        elif choice == '5':
            # Tandai selesai/belum selesai
            manager.display_tasks()
            try:
                index = int(input(f"{Colors.BOLD}Masukkan nomor tugas: {Colors.RESET}"))
                manager.mark_complete(index)
            except ValueError:
                print(f"{Colors.RED}Input tidak valid!{Colors.RESET}")
        
        elif choice == '6':
            # Hapus tugas
            manager.display_tasks()
            try:
                index = int(input(f"{Colors.BOLD}Masukkan nomor tugas yang akan dihapus: {Colors.RESET}"))
                confirm = input(f"{Colors.YELLOW}Apakah Anda yakin? (y/n): {Colors.RESET}").strip().lower()
                if confirm == 'y':
                    manager.delete_task(index)
            except ValueError:
                print(f"{Colors.RED}Input tidak valid!{Colors.RESET}")
        
        elif choice == '7':
            # Lihat kategori
            manager.display_categories()
        
        elif choice == '8':
            # Lihat statistik
            manager.display_statistics()
        
        elif choice == '9':
            # Keluar
            print(f"\n{Colors.GREEN}Terima kasih telah menggunakan Task Manager!{Colors.RESET}\n")
            break
        
        else:
            print(f"{Colors.RED}Pilihan tidak valid!{Colors.RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Program dihentikan oleh pengguna.{Colors.RESET}\n")
        sys.exit(0)
