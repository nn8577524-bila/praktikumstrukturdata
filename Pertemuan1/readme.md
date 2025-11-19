
# **Implementasi Stack dan Queue di Python**

Dokumentasi ini menjelaskan implementasi dasar struktur data **Stack** dan **Queue** menggunakan bahasa Python.
Keduanya menggunakan tipe data **list**, karena Python menyediakan operasi yang efisien seperti `append()`, `pop()`, dan indexing.
Implementasi struktur data Stack dan Queue menggunakan tipe data list Python sangat membantu dalam memahami prinsip dasarnya: LIFO (Last-In, First-Out) untuk Stack dan FIFO (First-In, First-Out) untuk Queue.

# STACK
Stack adalah struktur data linier yang menerapkan prinsip LIFO (Last-In, First-Out). 
Artinya elemen yang terakhir dimasukkan ke dalam tumpukan adalah elemen pertama yang akan dikeluarkan.

# Stack and stack operation
 ```stack = [] ```

# Push
```stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)
```

# Pop
```element = stack.pop()
print("Pop: ", element)
```

# Peek 
```topElement = stack[-1]
print("Peek: ", topElement)
```

# isEmpty
```isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)
```

# Size
```print("Size :", len(stack))```


# Penjelasan Stack

### 1. Inisialisasi Stack

Pertama saya membuat sebuah list kosong sebagai tempat tumpukan data:

```python
stack = []
```

### 2. Push (Menambahkan Elemen ke Atas Stack)

Data baru dimasukkan ke **bagian paling atas** stack menggunakan `append()`:

```python
stack.append('X')
stack.append('Y')
stack.append('Z')
```

Setelah proses ini, isi stack:
**['X', 'Y', 'Z']**

### 3. Pop (Mengambil Elemen Paling Atas)

Untuk mengambil elemen paling atas, saya memakai `pop()` tanpa indeks:

```python
topElement = stack.pop()
```

Yang keluar adalah `'Z'` karena dia dimasukkan terakhir.

### 4. Peek (Melihat Elemen Paling Atas)

Untuk mengecek data di bagian atas stack tanpa mengeluarkannya:

```python
peekElement = stack[-1]
```

### 5. isEmpty (Cek Stack Kosong atau Tidak)

Untuk memeriksa apakah stack sedang tidak berisi elemen apa pun:

```python
isEmpty = not bool(stack)
```

### 6. Size (Menghitung Jumlah Elemen)

Untuk mengetahui sisa elemen dalam stack:

```python
len(stack)
```


# Hasil Eksekusi
```Stack: ['X', 'Y', 'Z']
Pop: Z
Peek: Y
isEmpty: False
Size: 2
```




# QUEUE
Antrian adalah struktur data linier yang menerapkan prinsip FIFO (First-In, First-Out).
Artinya elemen yang pertama dimasukkan ke dalam antrian adalah elemen pertama yang akan dikeluarkan.

# Creating queue and Queue Operations
```queue = []```

# Enqueue
```queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)
```

# Dequeue
```element = queue.pop(0)
print("Dequeue: ", element)
```

# Peek
```frontElement = queue[0]
print("Peek: ", frontElement)
```

# isEmpty
```isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)
```

# Size
```print("Size: ", len(queue))```

# Penjelasan Queue

### 1. Inisialisasi Queue

Pertama, aku membuat sebuah list kosong sebagai tempat data antrian:

```python
queue = []
```

### 2. Enqueue (Menambah Data ke Antrian)

Elemen baru dimasukkan ke bagian **belakang** antrian menggunakan `append()`:

```python
queue.append('A')
queue.append('B')
queue.append('C')
```

Setelah langkah ini, isi antriannya adalah:
**['A', 'B', 'C']**

### 3. Dequeue (Menghapus Data Paling Depan)

Untuk mengambil elemen terdepan, digunakan `pop(0)`:

```python
element = queue.pop(0)
```

Elemen `'A'` keluar terlebih dahulu karena dialah yang masuk paling awal.

### 4. Peek (Melihat Data Terdepan Tanpa Mengambil)

Untuk sekadar melihat elemen yang berada di depan antrian:

```python
frontElement = queue[0]
```

### 5. isEmpty (Pengecekan Apakah Queue Kosong)

Digunakan untuk mengetahui apakah antrian berisi elemen atau tidak:

```python
isEmpty = not bool(queue)
```

### 6. Size (Menghitung Jumlah Elemen)

Untuk mengetahui sisa elemen yang ada:

```python
len(queue)
```

---

# Hasil Eksekusi

```
Queue: ['A', 'B', 'C']
Dequeue: A
Peek: B
isEmpty: False
Size: 2
```

---

##  **Struktur Data yang Digunakan**

* `append()` ➝ menambah elemen
* `pop()` ➝ menghapus elemen (terakhir / berdasarkan index)
* indexing `[0]` dan `[-1]` ➝ melihat elemen depan/teratas
* `len()` ➝ menghitung jumlah elemen
* `bool(list)` ➝ mengecek apakah list kosong
## **Kesimpulan**

Implementasi struktur data **Stack** dan **Queue** menggunakan tipe data **`list`** Python adalah metode yang sederhana untuk memahami prinsip dasar kedua struktur data tersebut, meskipun memiliki batasan kinerja yang signifikan pada Queue.
* **Stack** diimplementasikan secara **efisien** karena memanfaatkan operasi `append()` untuk **Push** dan `pop()` untuk **Pop**. 
* Kedua operasi ini memiliki kompleksitas waktu **konstan**, menjadikannya ideal karena interaksi Stack hanya terjadi di satu ujung (`tail` atau akhir list).
* **Queue** juga menggunakan `append()` untuk **Enqueue** tetapi mengandalkan `pop(0)` untuk operasi **Dequeue**.
* Operasi **Dequeue** ini memiliki kompleksitas waktu **linear** karena penghapusan elemen di awal list memerlukan pergeseran semua elemen yang tersisa di memori. 
* Hal ini membuat implementasi Queue dengan `list` **tidak efisien** untuk volume data besar atau aplikasi yang membutuhkan kinerja tinggi.
Untuk implementasi Queue yang optimal dalam konteks performa, **modul `collections.deque`** lebih disarankan karena dirancang untuk menjamin operasi Dequeue dan Enqueue di kedua ujung tetap berjalan dalam waktu **konstan**.


