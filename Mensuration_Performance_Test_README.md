# 🧮 Mensuration – Multiprocessing vs Multithreading Performance Test

## 📘 Description
This Python program compares the performance of **multiprocessing** and **multithreading** while performing **mensuration calculations** (area, perimeter, volume, surface area, etc.).  
The function `do_something()` performs repeated geometry computations, and the execution time is measured when running:
- Multiple **processes** (using the `multiprocessing` module)
- Multiple **threads** (using the `threading` module)

---

## ⚙️ How It Works
1. The user enters:
   - Number of **processes**
   - Number of **threads**
2. The program runs both multiprocessing and multithreading versions.
3. It measures the time taken for each approach.
4. Finally, you can compare which method was faster.

---

## 🧠 System Setup
- **Language:** Python 3  
- **Modules Used:**  
  ```python
  import math
  import time
  import multiprocessing
  import threading
  ```
- **Function:** `do_something(count, out_list)` performs complex mensuration operations.

---

## 🧪 Experimental Results

### 🔹 Case 1: 5 Processes & 5 Threads
> 📸 *Result Screenshot:*  
![Case 1 Screenshot](6afb1753-2d34-47c9-8620-bb0691d642e0.png)

**Multiprocessing Time:** `1.720735788345337 s`  
**Multithreading Time:** `7.349930286407471 s`  

---

### 🔹 Case 2: 10 Processes & 10 Threads
> 📸 *Result Screenshot:*  
![Case 2 Screenshot](698a7bcb-658d-4a1f-8f4c-07e129d5fcf0.png)

**Multiprocessing Time:** `3.2503035068511963 s`  
**Multithreading Time:** `9.445505857467651 s`

---

### 🔹 Case 3: 15 Processes & 15 Threads
> 📸 *Result Screenshot:*  
![Case 3 Screenshot](dbb60f59-020b-4fae-b1ce-bd31b9263fca.png)

**Multiprocessing Time:** `5.23498797416687 s`  
**Multithreading Time:** `13.821916580200195 s`

---

## 📊 Comparison Table

| No. of Processes/Threads | Multiprocessing Time (s) | Multithreading Time (s) |
|---------------------------|---------------------------|---------------------------|
| 5                         | 1.72                      | 7.35                      |
| 10                        | 3.25                      | 9.45                      |
| 15                        | 5.23                      | 13.82                     |

---

## 💡 Conclusion
- **Multiprocessing** was observed to be **faster and more efficient** for CPU-bound operations such as heavy mathematical calculations.  
- **Multithreading** performed slower because of Python’s **Global Interpreter Lock (GIL)**, which prevents true parallel execution of threads for CPU-heavy tasks.  
- Hence, **multiprocessing** is the better choice for tasks involving large numerical computations.

---

## 🧰 Example Output
```
===== MENSURATION PERFORMANCE TEST =====
Enter number of processes: 10
Enter number of threads: 10

List processing complete.
Multiprocessing time = 3.1546270847320557
List processing complete.
Multithreading time = 12.893417358398438
```
