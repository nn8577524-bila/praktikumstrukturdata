**Penjelasan fungsi dari masing-masing bagian kode Linked List** :

---

## 1. `class Node`

```python
class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer
```

**Fungsi:**

* `Node` adalah **unit terkecil** dari Linked List.
* `data` menyimpan nilai/data.
* `next` (pointer) menyimpan alamat node berikutnya.

Ibarat gerbong kereta:

* `data` = penumpang/barang di gerbong
* `next` = sambungan ke gerbong selanjutnya

---

## 2. `class Linkedlist`

```python
class Linkedlist:
   def __init__(self):
        self.head = None
```

**Fungsi:**

* `head` adalah **titik awal** Linked List.
* Awalnya `None` karena list masih kosong.

---

## 3. `insert_at_first(self, data)`

```python
def insert_at_first(self, data):
    node = Node(data,self.head)
    self.head = node
```

**Fungsi:**

* Menambahkan data di **awal** linked list.
* Node baru menunjuk ke `head` lama.
* `head` diperbarui ke node baru.

Contoh:
Sebelum: `A -> B -> C`
Sesudah insert `"X"`: `X -> A -> B -> C`

---

## 4. `insert_at_last(self, data)`

```python
def insert_at_last(self, data):
      if self.head is None:
         self.head = Node(data)
      else:
         node_sekarang = self.head
         while node_sekarang.next: 
             node_sekarang = node_sekarang.next

         node = Node(data)
         node_sekarang.next = node
```

**Fungsi:**

* Menambahkan data di **akhir** linked list.
* Jika list kosong → langsung jadi `head`.
* Jika tidak kosong → berjalan sampai node terakhir → tambah node baru.

---

## 5. `insert_at(self, index, data)`

```python
def insert_at(self, index, data):
```

**Fungsi:**

* Menyisipkan data di **posisi tertentu (index)**.

Tahapan:

1. Cek apakah `index` valid
2. Jika `index == 0` → pakai `insert_at_first`
3. Jika bukan → jalan ke node sebelum posisi tujuan
4. Sisipkan node baru di tengah dengan:

   ```python
   node = Node(data, node_sekarang.next)
   node_sekarang.next = node
   ```

Contoh:
Sebelum: `A -> B -> C`
Insert index 1 `"X"` → `A -> X -> B -> C`

---

## 6. `print(self)`

```python
def print(self):
```

**Fungsi:**

* Menampilkan seluruh isi linked list dalam bentuk teks.

Jika kosong → cetak `"data kosong"`
Jika ada → tampilkan dengan format:

```
data1->data2->data3->
```

---

## 7. `length(self)`

```python
def length(self):
```

**Fungsi:**

* Menghitung jumlah node di dalam linked list.
* Berjalan dari `head` sampai `None` sambil menghitung.

---

## 8. Bagian Penggunaan Kode

```python
LL = Linkedlist()
```

Membuat objek linked list.

### Insert data:

```python
LL.insert_at_first("jeruk")
LL.insert_at_first("mangga")
LL.insert_at_first("manggis")
LL.insert_at_last("apel")
LL.insert_at(2, "anggur")
```

Urutan hasil akhirnya:

```
manggis -> mangga -> anggur -> jeruk -> apel
```

### Print dan length:

```python
LL.print() 
print(LL.length())
```

Hasil output:

```
manggis->mangga->anggur->jeruk->apel->
5
```

---


