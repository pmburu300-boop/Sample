# Python Learning Journey for C++ Developers

> **Estimated Total Duration:** 4–6 months (at ~10 hrs/week)  
> **Starting Point:** Proficient in C++ (OOP, memory management, STL, templates)

---

## Phase 1 — Python Foundations & C++ Mental Model Shift
**Duration:** 3–4 weeks

### Prerequisites
- Solid understanding of C++ fundamentals (variables, loops, functions, OOP)
- A working Python installation (3.10+) and a code editor (VS Code recommended)

### Learning Steps

**1. Syntax & Type System**  
Learn Python's dynamic typing, indentation-based blocks, and how it contrasts with C++'s explicit typing. Cover variables, control flow (`if/elif/else`, `for`, `while`), and basic I/O. Focus on the "no braces, no semicolons" philosophy.

**2. Functions & Pythonic Idioms**  
Explore default arguments, `*args`/`**kwargs`, and multiple return values. Learn comprehensions (`[x*2 for x in lst]`), f-strings, and how Python replaces many C++ patterns (e.g., range-based for loops become simply `for item in collection`).

**3. Core Data Structures**  
Master the four built-in types: `list` (≈ `std::vector`), `tuple` (immutable), `dict` (≈ `std::unordered_map`), and `set`. Understand how Python handles memory automatically — no `new`/`delete`, no destructors.

**4. Modules & the Standard Library**  
Learn to import modules, understand `__name__ == "__main__"`, and explore key stdlib modules: `os`, `sys`, `math`, `datetime`, and `random`. Get comfortable with `pip` and virtual environments (`venv`).

**5. Error Handling**  
Understand Python exceptions vs. C++ exceptions: `try/except/finally`, raising exceptions, and creating custom exception classes. Learn why Python favors EAFP ("Easier to Ask Forgiveness than Permission") over LBYL.

### Verification Activities
- Rewrite 2–3 small C++ programs (e.g., a calculator, a linked list, a sorting algorithm) in Python and compare the line counts and readability.
- Complete 10 beginner problems on [Exercism.io](https://exercism.org/tracks/python) (Python track).
- Write a script that reads a CSV file, processes data, and writes results to a new file — using only stdlib.

---

## Phase 2 — Object-Oriented Python & Intermediate Patterns
**Duration:** 4–5 weeks

### Prerequisites
- Comfortable writing Python scripts from Phase 1
- Understanding of Python's dynamic nature and basic data structures

### Learning Steps

**1. Classes & OOP in Python**  
Learn Python's class syntax, `__init__`, `self`, inheritance, and method resolution order (MRO). Compare with C++: no header files, no access specifiers (`public`/`private`), and how Python uses naming conventions (single underscore `_`) instead of enforcement.

**2. Magic/Dunder Methods**  
Master `__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, and others. This is Python's way of operator overloading — similar to C++ `operator+` but more uniform and readable.

**3. Iterators, Generators & Lazy Evaluation**  
Understand the iterator protocol (`__iter__`/`__next__`), then move to `yield` and generator functions. This is a powerful Python feature with no direct C++ equivalent — generators produce values on demand without building entire data structures in memory.

**4. Decorators & Functional Tools**  
Learn how decorators work (`@property`, `@staticmethod`, `@classmethod`, and custom ones). Explore `functools` (`partial`, `lru_cache`, `reduce`) and `itertools`. These replace many C++ template patterns with elegant, readable solutions.

**5. File I/O, Context Managers & the `with` Statement**  
Understand `with open(...) as f` — Python's RAII equivalent. Learn to work with binary files, JSON (`json` module), and understand how to write your own context managers using `__enter__`/`__exit__` or `contextlib`.

### Verification Activities
- Build a small object-oriented project: a simple bank account system or a card game with at least 3 classes, inheritance, and dunder methods.
- Implement a custom iterator class and an equivalent generator function for the same task, then compare them.
- Solve 10 intermediate problems on [Exercism.io](https://exercism.org/tracks/python) or [LeetCode](https://leetcode.com) using Python-idiomatic solutions.

---

## Phase 3 — Ecosystem Deep Dive: Libraries & Tooling
**Duration:** 5–6 weeks

### Prerequisites
- Solid grasp of Python OOP and intermediate features from Phase 2
- Familiarity with virtual environments and `pip`

### Learning Steps

**1. NumPy & Array Computing**  
Learn NumPy's `ndarray`, vectorized operations, broadcasting, and slicing. As a C++ developer, you'll appreciate the performance story: NumPy operations call compiled C under the hood, giving you Python's syntax with near-C speed for numerical work.

**2. Data Wrangling with Pandas**  
Master `DataFrame` and `Series`, reading/writing CSV and JSON, filtering, grouping, merging, and handling missing data. Pandas is the backbone of data analysis in Python and directly applicable to any data-intensive work.

**3. Testing with pytest**  
Learn to write unit tests with `pytest`, use fixtures, parametrize tests, and mock dependencies with `unittest.mock`. Coming from C++, you'll find pytest far more ergonomic than most C++ testing frameworks.

**4. Packaging, Dependency Management & Project Structure**  
Learn how to structure a Python project, write a `pyproject.toml`, publish to PyPI, and use tools like `poetry` or `uv`. Understand how this differs from C++ build systems (CMake, Make).

**5. Concurrency: Threading, Multiprocessing & Asyncio**  
Understand the GIL (Global Interpreter Lock) and why Python threading differs fundamentally from C++ threading. Learn when to use `threading` vs. `multiprocessing` vs. `asyncio`, and how `async/await` enables non-blocking I/O.

### Verification Activities
- Perform a data analysis task end-to-end: load a real dataset (e.g., from Kaggle), clean it with Pandas, compute statistics with NumPy, and produce a summary report.
- Write a fully tested Python module with at least 90% test coverage using `pytest`.
- Build a small async web scraper using `asyncio` and `aiohttp` (or a simple REST API with `FastAPI`) and deploy it locally.

---

## Phase 4 — Advanced Python & Real-World Applications
**Duration:** 5–6 weeks

### Prerequisites
- Comfortable with the Python ecosystem (Phase 3 libraries)
- Experience writing tested, structured Python code

### Learning Steps

**1. Type Hints & Static Analysis**  
Add type annotations to your Python code (`int`, `str`, `list[int]`, `Optional`, `Union`, `TypeVar`). Use `mypy` for static type checking. As a C++ developer, this will feel familiar — and it drastically improves code maintainability.

**2. Advanced OOP: Dataclasses, ABCs & Protocols**  
Learn `@dataclass` (Python's answer to simple structs), Abstract Base Classes (`abc` module), and `Protocol` (structural subtyping, similar to C++ concepts). Understand when to prefer composition over inheritance.

**3. Performance Profiling & Optimization**  
Learn to profile Python code with `cProfile` and `line_profiler`. Understand when to reach for Cython, `ctypes`, or C extensions. As a C++ developer, you're well-positioned to write Python extensions in C++ using `pybind11` — a powerful skill for performance-critical work.

**4. Design Patterns in Python**  
Revisit classic patterns (Singleton, Factory, Observer, Strategy) and see how Python idioms simplify or replace them. Explore Python-specific patterns like metaclasses, descriptors, and `__slots__` for memory optimization.

**5. Choose a Specialization Track**  
Pick one area to go deeper: **Web Development** (FastAPI, Django), **Data Science/ML** (scikit-learn, PyTorch), **DevOps/Automation** (Ansible, scripting), or **Systems** (pybind11, Cython, extending C++ with Python). Build a substantial project in your chosen domain.

### Verification Activities
- Take an existing Phase 2 or 3 project and add full type hints, then validate with `mypy --strict`.
- Profile a slow Python function, identify the bottleneck, and optimize it — either algorithmically or by calling into C++ via `pybind11` or `ctypes`.
- Build and complete a capstone project in your chosen specialization track: a REST API, a trained ML model, an automation pipeline, or a Python-wrapped C++ library. Document it in a README and push it to GitHub.

---

## Key Mindset Shifts: C++ → Python

| C++ Concept | Python Equivalent |
|---|---|
| `std::vector<int>` | `list` |
| `std::unordered_map` | `dict` |
| Templates | Duck typing + Generics/Protocols |
| RAII / destructors | Context managers (`with`) |
| `operator+` overload | Dunder methods (`__add__`) |
| Header files | Modules (`.py` files) |
| `nullptr` checks | `if obj is None` |
| Compile-time errors | `mypy` static analysis |
| `std::thread` + mutex | `threading` / `asyncio` |

---

## Recommended Resources

- **Official Docs:** [docs.python.org](https://docs.python.org) — always authoritative
- **Book:** *Fluent Python* by Luciano Ramalho (best intermediate-to-advanced Python book)
- **Book:** *Python Crash Course* by Eric Matthes (quick Phase 1 companion)
- **Practice:** [Exercism.io Python track](https://exercism.org/tracks/python), [LeetCode](https://leetcode.com)
- **C++ Bridge:** [pybind11 docs](https://pybind11.readthedocs.io) for leveraging your C++ skills
