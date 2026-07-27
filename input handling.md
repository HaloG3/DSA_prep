

### 📚 Problem Example:

> The first line contains a single integer `N`.



```python
N = int(input())
```

### 💡 Intuition:

* Simple single input → Just convert the string to int.

---

## ✅ 2️⃣. **Multiple Space-separated Integers on One Line**



> The first line contains two integers `N` and `K`.



```python
N, K = map(int, input().split())
```

### 💡 Intuition:

* `input().split()` → splits input by spaces → returns a list of strings.
* `map(int, ...)` converts each to integer.

---

## ✅ 3️⃣. **Array Input on a Single Line**



> Next line contains `N` integers.



```python
arr = list(map(int, input().split()))
```

### 💡 Intuition:

* **Use when an array of elements is given in space-separated format.**
* List stores the array for further use.

---

## ✅ 4️⃣. **Multiple Lines of Input (Fixed Number of Lines)**



> Next `M` lines contain two space-separated integers.


```python
pairs = []
for _ in range(M):
    a, b = map(int, input().split())
    pairs.append((a, b))
```

### 💡 Intuition:

* Loop runs `M` times.
* Each line has two numbers → map them and store as tuples (or lists).

---

## ✅ 5️⃣. **Matrix Input (2D Array)**



> Next `N` lines contain `M` integers each.



```python
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
```

### 💡 Intuition:

* Build the matrix row by row.
* You get a list of lists.

---

## ✅ 6️⃣. **Single String Input**



> A single line contains a string.



```python
s = input()
```

### 💡 Intuition:

* No extra processing unless otherwise specified (e.g., remove whitespace).

---

## ✅ 7️⃣. **Multiple Strings on One Line**



> Two strings separated by space.


```python
str1, str2 = input().split()
```

---

## ✅ 8️⃣. **Reading Until EOF (End of Input)**

### ✅ Code Pattern:

```python
import sys

for line in sys.stdin:
    # process line
    data = line.strip()
```

### 💡 Intuition:

* Useful when input size isn’t specified.
* Read lines until no input is left.

---

## ✅ 9️⃣. **Handling Large Inputs Faster (Use sys.stdin)**

```python
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
```

💡 **Why use this?**
For large inputs, `sys.stdin.readline()` is much faster than regular `input()`.

---

## ✅ 🔟. **Example Combining Multiple Concepts**

> Problem:
> The first line contains two integers `N` and `K`.
> Next line contains `N` space-separated integers.
> Then `M` lines follow, each with two integers `a` and `b`.

### ✅ Full Parsing Code:

```python
N, K = map(int, input().split())
arr = list(map(int, input().split()))

M = int(input())  # If M is specified as next line
pairs = []
for _ in range(M):
    a, b = map(int, input().split())
    pairs.append((a, b))
```

---

## ✅ Key Intuition Summary:

| Pattern                           | When to Use                       | Example           |
| --------------------------------- | --------------------------------- | ----------------- |
| `int(input())`                    | Single integer input              | `5`               |
| `map(int, input().split())`       | Multiple integers in one line     | `3 5`             |
| `list(map(int, input().split()))` | Array of numbers                  | `1 2 3 4 5`       |
| Loop + `input().split()`          | Multiple lines of inputs          | `1 2`, `3 4`, ... |
| `sys.stdin.readline()`            | Faster input for large test cases | Big inputs        |

---

## ✅ ⚡ Pro Tips:

1. **Always check constraints** — Avoid TLE by using `sys.stdin.readline()` for big inputs.
2. **Avoid extra conversions** — If only strings are needed, don’t convert to `int`.
3. **Initialize containers properly** — Lists for arrays, tuples for pairs.
4. **Be careful about trailing spaces or empty lines** — Use `.strip()` if needed.

---


