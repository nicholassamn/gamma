#!/usr/bin/env python3
"""
Script testing untuk Task Manager tanpa input interaktif
"""

import os
import json
from task_manager import TaskManager, Task
from datetime import datetime, timedelta


def test_basic_operations():
    """Test operasi dasar"""
    print("\n" + "="*60)
    print("TEST 1: Operasi Dasar")
    print("="*60)
    
    # Bersihkan file lama
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")
    
    manager = TaskManager("test_tasks.json")
    
    # Test add task
    assert manager.add_task("Test Task 1", "Testing", "2026-02-15") == True
    assert len(manager.tasks) == 1
    print("✓ Add task berhasil")
    
    # Test kategori
    assert "Testing" in manager.categories
    print("✓ Kategori terdeteksi")
    
    # Test load dari file
    manager2 = TaskManager("test_tasks.json")
    assert len(manager2.tasks) == 1
    assert manager2.tasks[0].title == "Test Task 1"
    print("✓ Save dan load dari JSON berhasil")
    
    # Cleanup
    os.remove("test_tasks.json")


def test_deadline_system():
    """Test sistem deadline"""
    print("\n" + "="*60)
    print("TEST 2: Sistem Deadline")
    print("="*60)
    
    if os.path.exists("test_deadline.json"):
        os.remove("test_deadline.json")
    
    manager = TaskManager("test_deadline.json")
    
    today = datetime.now().date()
    
    # Test deadline calculation
    task1 = Task("Task terlewat", "Test", (today - timedelta(days=2)).strftime("%Y-%m-%d"))
    assert task1.days_until_deadline() == -2
    print("✓ Deadline terlewat dihitung dengan benar")
    
    task2 = Task("Task hari ini", "Test", today.strftime("%Y-%m-%d"))
    assert task2.days_until_deadline() == 0
    print("✓ Deadline hari ini dihitung dengan benar")
    
    task3 = Task("Task 5 hari", "Test", (today + timedelta(days=5)).strftime("%Y-%m-%d"))
    assert task3.days_until_deadline() == 5
    print("✓ Deadline di masa depan dihitung dengan benar")
    
    task4 = Task("Task tanpa deadline", "Test", None)
    assert task4.days_until_deadline() is None
    print("✓ Task tanpa deadline ditangani dengan benar")
    
    # Cleanup
    if os.path.exists("test_deadline.json"):
        os.remove("test_deadline.json")


def test_color_system():
    """Test sistem warna"""
    print("\n" + "="*60)
    print("TEST 3: Sistem Warna")
    print("="*60)
    
    from task_manager import Colors
    
    today = datetime.now().date()
    
    # Test berbagai kondisi deadline
    task_overdue = Task("Overdue", "Test", (today - timedelta(days=1)).strftime("%Y-%m-%d"))
    color1, _ = task_overdue.get_color()
    assert color1 != ""
    print("✓ Warna untuk task terlewat ditentukan")
    
    task_no_deadline = Task("No deadline", "Test", None)
    color2, _ = task_no_deadline.get_color()
    assert color2 != ""
    print("✓ Warna untuk task tanpa deadline ditentukan")
    
    task_completed = Task("Completed", "Test", "2026-02-15")
    task_completed.completed = True
    color3, _ = task_completed.get_color()
    assert color3 != ""
    print("✓ Warna untuk task selesai ditentukan")


def test_task_completion():
    """Test menandai task selesai"""
    print("\n" + "="*60)
    print("TEST 4: Task Completion")
    print("="*60)
    
    if os.path.exists("test_completion.json"):
        os.remove("test_completion.json")
    
    manager = TaskManager("test_completion.json")
    manager.add_task("Test Task", "Testing")
    
    # Test mark complete
    assert manager.tasks[0].completed == False
    manager.mark_complete(0)
    assert manager.tasks[0].completed == True
    print("✓ Mark task selesai berhasil")
    
    # Toggle back
    manager.mark_complete(0)
    assert manager.tasks[0].completed == False
    print("✓ Toggle task status berhasil")
    
    # Cleanup
    os.remove("test_completion.json")


def test_update_task():
    """Test update task"""
    print("\n" + "="*60)
    print("TEST 5: Update Task")
    print("="*60)
    
    if os.path.exists("test_update.json"):
        os.remove("test_update.json")
    
    manager = TaskManager("test_update.json")
    manager.add_task("Original Title", "Category1", "2026-02-15", "Original desc")
    
    # Test update title
    manager.update_task(0, title="Updated Title")
    assert manager.tasks[0].title == "Updated Title"
    print("✓ Update title berhasil")
    
    # Test update category
    manager.update_task(0, category="Category2")
    assert manager.tasks[0].category == "Category2"
    print("✓ Update kategori berhasil")
    
    # Test update deadline
    manager.update_task(0, deadline="2026-03-20")
    assert manager.tasks[0].deadline == "2026-03-20"
    print("✓ Update deadline berhasil")
    
    # Test update description
    manager.update_task(0, description="Updated desc")
    assert manager.tasks[0].description == "Updated desc"
    print("✓ Update deskripsi berhasil")
    
    # Cleanup
    os.remove("test_update.json")


def test_deletion():
    """Test delete task"""
    print("\n" + "="*60)
    print("TEST 6: Delete Task")
    print("="*60)
    
    if os.path.exists("test_delete.json"):
        os.remove("test_delete.json")
    
    manager = TaskManager("test_delete.json")
    manager.add_task("Task 1", "Testing")
    manager.add_task("Task 2", "Testing")
    manager.add_task("Task 3", "Testing")
    
    assert len(manager.tasks) == 3
    manager.delete_task(1)
    assert len(manager.tasks) == 2
    assert manager.tasks[1].title == "Task 3"
    print("✓ Delete task berhasil")
    
    # Cleanup
    os.remove("test_delete.json")


def test_categorization():
    """Test sistem kategori"""
    print("\n" + "="*60)
    print("TEST 7: Kategorisasi")
    print("="*60)
    
    if os.path.exists("test_category.json"):
        os.remove("test_category.json")
    
    manager = TaskManager("test_category.json")
    manager.add_task("Task 1", "Work")
    manager.add_task("Task 2", "Personal")
    manager.add_task("Task 3", "Work")
    
    assert len(manager.categories) == 2
    assert "Work" in manager.categories
    assert "Personal" in manager.categories
    print("✓ Kategori tercatat dengan benar")
    
    # Count tasks per category
    work_tasks = [t for t in manager.tasks if t.category == "Work"]
    assert len(work_tasks) == 2
    print("✓ Filter kategori bekerja dengan baik")
    
    # Cleanup
    os.remove("test_category.json")


def test_data_persistence():
    """Test persistensi data"""
    print("\n" + "="*60)
    print("TEST 8: Data Persistence")
    print("="*60)
    
    if os.path.exists("test_persist.json"):
        os.remove("test_persist.json")
    
    # Create and save
    manager1 = TaskManager("test_persist.json")
    manager1.add_task("Task 1", "Category1", "2026-02-15", "Description 1")
    manager1.add_task("Task 2", "Category2", None, "Description 2")
    manager1.tasks[0].completed = True
    manager1.save_tasks()
    
    # Load from file
    manager2 = TaskManager("test_persist.json")
    assert len(manager2.tasks) == 2
    assert manager2.tasks[0].completed == True
    assert manager2.tasks[1].deadline is None
    assert "Category1" in manager2.categories
    assert "Category2" in manager2.categories
    print("✓ Data berhasil disimpan dan dimuat")
    
    # Verify JSON format
    with open("test_persist.json", "r") as f:
        data = json.load(f)
        assert "tasks" in data
        assert "categories" in data
        assert len(data["tasks"]) == 2
    print("✓ Format JSON valid")
    
    # Cleanup
    os.remove("test_persist.json")


def main():
    """Jalankan semua test"""
    print("\n" + "="*60)
    print("TASK MANAGER - AUTOMATED TESTING")
    print("="*60)
    
    try:
        test_basic_operations()
        test_deadline_system()
        test_color_system()
        test_task_completion()
        test_update_task()
        test_deletion()
        test_categorization()
        test_data_persistence()
        
        print("\n" + "="*60)
        print("✓ SEMUA TEST BERHASIL!")
        print("="*60 + "\n")
        
    except AssertionError as e:
        print(f"\n✗ TEST GAGAL: {e}\n")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
