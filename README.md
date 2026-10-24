# LeetCode — Add Two Numbers

A focused Python implementation of **LeetCode's Add Two Numbers (Medium)** that **adds two non-negative integers stored as reversed digit lists** by converting each list to an integer, adding them, and converting the sum back to a reversed digit list. Clean, short, and correct — this solution is the entry point to understanding digit-by-digit representation, place value (`10**i`), and the difference between the **arithmetic shortcut** and the **carry-based linked-list solution** that interviewers actually expect.

🔗 **Problem link:** [leetcode.com/problems/add-two-numbers](https://leetcode.com/problems/add-two-numbers/)

---

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

**Example Input:**
```
l1 = [2,4,3]
l2 = [5,6,4]
```

**Example Output:**
```
[7,0,8]
```

**Explanation:** `342 + 465 = 807`

**Official Constraints:**
- The number of nodes in each list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- The list represents a number with no leading zeros

---

## The Code

```python
"""
Add Two Numbers :
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
nl1 = int(input("Enter the number of elements in the first list: "))
l1 = []
for i in range(nl1):
    l1.append(int(input(f"Enter element {i+1}: ")))

nl2 = int(input("Enter the number of elements in the second list: "))
l2 = []
for i in range(nl2):
    l2.append(int(input(f"Enter element {i+1}: ")))

sl1=0
for i in range(nl1):
    sl1 += l1[i] * (10 ** i)

sl2=0
for i in range(nl2):
    sl2 += l2[i] * (10 ** i)

result = sl1 + sl2

output = list(map(int, str(result)))
output.reverse()
print(output)
```

---

## The Critical Idea — Reversed Digits Are Already in Place-Value Order

This is the most important thing to understand about this solution.

Because the digits are stored **in reverse**, the element at index `i` always has place value `10**i`. The ones digit is at index 0, the tens digit at index 1, and so on. That means no reversing is needed to *read* the number — a simple weighted sum rebuilds it.

```
l1 = [2, 4, 3]
      ↓  ↓  ↓
     2×1 + 4×10 + 3×100 = 342

l2 = [5, 6, 4]
      ↓  ↓  ↓
     5×1 + 6×10 + 4×100 = 465

342 + 465 = 807  →  "807"  →  [8,0,7]  →  reverse  →  [7,0,8]
```

The final **reverse** is needed only because `str(result)` produces the most-significant digit first, while the answer must again be least-significant first.

| Stage | What happens | Code |
|-------|--------------|------|
| 1. Read | Collect digits into Python lists | `l1`, `l2` |
| 2. Decode | Weighted sum with `10**i` | `sl1`, `sl2` |
| 3. Add | Ordinary integer addition | `result = sl1 + sl2` |
| 4. Encode | Digits of the sum, then reversed | `list(map(int, str(result)))` + `reverse()` |

---

## How the Decode Loop Works

```python
sl1 = 0
for i in range(nl1):
    sl1 += l1[i] * (10 ** i)
```

- **Start:** `sl1 = 0` — accumulator for the rebuilt number
- **Range:** `i` runs `0 … nl1-1` — every digit exactly once
- **Weight:** `10 ** i` — place value of the digit at index `i`
- **Body:** adds `digit × place value` to the running total

For `l1 = [2,4,3]`, the loop runs 3 times: `i = 0, 1, 2` contributing `2`, `40`, `300`.

> **Python advantage:** Python integers have **arbitrary precision**, so there is no overflow no matter how long the lists are. In C++ or Java, a 100-digit number would overflow `long long`, which is exactly why the "convert to integer" trick does not carry over to those languages.

---

## Algorithm (Pseudocode)

```
read l1, l2

sl1 = sum of l1[i] * 10^i      for every index i
sl2 = sum of l2[i] * 10^i      for every index i

result = sl1 + sl2

digits = digits of result, most-significant first
reverse digits
print digits
```

---

## Dry Run

**Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`

**Decode `l1`:**

| `i` | `l1[i]` | `10**i` | Contribution | `sl1` so far |
|-----|---------|---------|--------------|--------------|
| 0   | 2       | 1       | 2            | 2            |
| 1   | 4       | 10      | 40           | 42           |
| 2   | 3       | 100     | 300          | 342          |

**Decode `l2`:**

| `i` | `l2[i]` | `10**i` | Contribution | `sl2` so far |
|-----|---------|---------|--------------|--------------|
| 0   | 5       | 1       | 5            | 5            |
| 1   | 6       | 10      | 60           | 65           |
| 2   | 4       | 100     | 400          | 465          |

**Add and encode:**

| Step | Value |
|------|-------|
| `result = 342 + 465` | `807` |
| `str(result)` → digits | `[8, 0, 7]` |
| After `reverse()` | `[7, 0, 8]` |

**Output:** `[7, 0, 8]` ✅

---

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | **O(n²)** worst case in the number of digits — each `10 ** i` and each addition operates on a big integer that itself grows with `i`; for LeetCode's limit of 100 digits this is instantaneous |
| Space  | **O(n + m)** — the two input lists plus the big integers and the output list |

For comparison, the carry-based linked-list solution (below) is **O(max(n, m))** time and **O(1)** auxiliary space.

---

## Edge Cases

| Scenario | Behavior |
|----------|----------|
| `l1 = [0]`, `l2 = [0]` | `0 + 0 = 0` → `str` gives `"0"` → output `[0]` ✅ |
| Different lengths `[9,9,9,9,9,9,9]` + `[9,9,9,9]` | `9999999 + 9999 = 10009998` → output `[8,9,9,9,0,0,0,1]` ✅ |
| Final carry creates a new digit `[9,9]` + `[1]` | `99 + 1 = 100` → output `[0,0,1]` ✅ |
| One list much longer than the other | Handled — each list is decoded independently ✅ |
| Sum has trailing zeros after reversing `[5]` + `[5]` | `10` → `[1,0]` → reversed `[0,1]` ✅ |
| Very long lists (> 4300 digits) | `str(result)` raises `ValueError` on Python 3.11+ due to the int-to-string digit limit ⚠️ |
| Empty list (`n = 0`) | Decodes to `0`, so it runs, but it violates the "non-empty" guarantee in the problem ⚠️ |

---

## Important Note — This Is Not a Direct LeetCode Submission

On LeetCode, the input is **not** a Python list. It is the head of a singly linked list:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

and the function signature is:

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```

The code in this repository reads plain lists from the keyboard with `input()`, so it demonstrates the **idea** and the **arithmetic**, but it will not run in the LeetCode editor as-is. The version below is the one to submit.

---

## The Natural Extension — Carry-Based Linked-List Solution

This is the standard accepted solution. It walks both lists at once, adds digit by digit, and carries — exactly like pencil-and-paper addition, with no big integers.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next
```

**Trace for `[2,4,3]` + `[5,6,4]`:**

| Step | `l1.val` | `l2.val` | `carry` in | `total` | digit | `carry` out |
|------|----------|----------|------------|---------|-------|-------------|
| 1    | 2        | 5        | 0          | 7       | 7     | 0           |
| 2    | 4        | 6        | 0          | 10      | 0     | 1           |
| 3    | 3        | 4        | 1          | 8       | 8     | 0           |

**Result:** `7 → 0 → 8` ✅

| Property | This repo's solution | Carry-based linked list |
|----------|----------------------|-------------------------|
| Works on `ListNode` input | ❌ No (plain lists) | ✅ Yes |
| Needs big integers | ✅ Yes | ❌ No |
| Portable to C++ / Java | ❌ Overflows | ✅ Yes |
| Time | O(n²) worst case | O(max(n, m)) |
| Auxiliary space | O(n + m) | O(1) |
| When to use | Understanding the idea in Python | Interviews and LeetCode submission |

> **Why `while l1 or l2 or carry`?** The `or carry` is what handles a leftover carry after both lists end, such as `99 + 1 = 100`. Dropping it loses the final `1`.

---

## Repository Structure

```
LeetCode-Add-Two-Numbers/
│
├── add_two_numbers.py    # Main Python implementation
└── README.md             # Project documentation
```

---

## How to Compile and Run

**Prerequisites:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/rishita-ops/LeetCode-Add-Two-Numbers.git
cd LeetCode-Add-Two-Numbers

# Run
python3 add_two_numbers.py
```

**On Windows:**
```bash
python add_two_numbers.py
```

**Sample session:**
```
Enter the number of elements in the first list: 3
Enter element 1: 2
Enter element 2: 4
Enter element 3: 3
Enter the number of elements in the second list: 3
Enter element 1: 5
Enter element 2: 6
Enter element 3: 4
[7, 0, 8]
```

---

## Key Concepts Covered

- **Reversed-digit representation** — index `i` carries place value `10**i`
- **Place-value decoding** — rebuilding an integer from digits with a weighted sum
- **Arbitrary-precision integers** — Python's built-in big ints remove overflow concerns
- **`str()` → digits → `reverse()`** — encoding an integer back into a reversed digit list
- **Carry propagation** — the core idea behind the linked-list solution
- **Dummy-head technique** — simplifies building a result linked list
- **Int-to-string limit** — Python 3.11+ caps `str(int)` at 4300 digits by default

---

## Why This Problem Matters in DSA

The digit-by-digit addition with carry pattern appears across a broad family of problems:

| Problem / Concept | Connection |
|-------------------|------------|
| **Add Two Numbers II** (LeetCode #445) | Same problem, but digits are stored most-significant first — needs a stack or list reversal |
| **Add Binary** (LeetCode #67) | Same carry loop with base 2 instead of base 10 |
| **Add Strings** (LeetCode #415) | Same carry loop on strings, without converting to integers |
| **Plus One** (LeetCode #66) | Carry propagation in its simplest form |
| **Multiply Strings** (LeetCode #43) | Repeated digit-by-digit arithmetic with carries |
| **Reverse Linked List** (LeetCode #206) | The pointer manipulation needed for the "II" variant |
| **Merge Two Sorted Lists** (LeetCode #21) | Same two-pointer walk over two linked lists with a dummy head |

Every problem that simulates arithmetic on digits, strings, or lists traces back to the carry loop introduced here.

---

## Contributing

Contributions are welcome. Consider adding:
- The **carry-based `ListNode` solution** as a separate, submittable file
- A **helper that builds a linked list from a Python list** (and prints one) for local testing
- A version using **recursion** with the carry as a parameter
- Input validation for empty lists and digits outside `0–9`
- Implementations in C++, Java, or JavaScript

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# Then open a Pull Request
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

*Part of a structured LeetCode practice series — fundamentals, done right.*
