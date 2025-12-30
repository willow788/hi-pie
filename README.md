<div align="center">

# 🥧 hi-pie

### *A Mesmerizing Journey Through the Irrationality of π*

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Math](https://img.shields.io/badge/Math-Complex%20Numbers-purple.svg)]()

---

**[Features](#-features)** • 
**[Installation](#-installation)** • 
**[How It Works](#-how-it-works)** • 
**[Math Behind It](#-the-mathematics)** • 
**[License](#-license)**

---

</div>

## 🎨 What is hi-pie?

**hi-pie** is a stunning Python visualization that brings mathematics to life!  Using turtle graphics and complex number theory, this project creates an infinite, never-repeating pattern that beautifully demonstrates why π is irrational.

Watch as mathematical elegance unfolds before your eyes through animated curves drawn in real-time!  ✨

---

## ✨ Features

🎯 **Real-time Animation** - Watch the pattern emerge stroke by stroke  
🌌 **Beautiful Visualization** - White curves on black background for maximum contrast  
🔢 **Complex Mathematics** - Combines Euler's number, imaginary units, and π  
♾️ **Infinite Pattern** - Never repeats due to π's irrational nature  
⚡ **Optimized Performance** - Maximum drawing speed for smooth animation  

---

## 🚀 Installation

### Prerequisites

- Python 3.x (comes with all required libraries!)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/willow788/hi-pie.git

# Navigate to the project
cd hi-pie

# Run the visualization
python "Main Python code/hipi.py"
```

> **Tip:** Press `Ctrl+C` to stop the animation at any time

---

## 🎬 How It Works

The program generates points using a fascinating complex function and plots them on a coordinate plane: 

```python
z(θ) = e^(iθ) + e^(iπθ)
```

As θ (theta) increases incrementally, each new point is connected to the previous one, creating an intricate, flowing pattern that evolves infinitely! 

### The Drawing Process

1. 🎯 Initialize a black canvas with white pen
2. 📐 Calculate complex coordinates using the function above
3. 🖊️ Plot points and connect them in real-time
4. 🔄 Repeat infinitely, revealing new patterns continuously

---

## 🧮 The Mathematics

This visualization is built on three fundamental mathematical constants:

| Symbol | Name | Value | Role |
|--------|------|-------|------|
| **e** | Euler's Number | ≈ 2.71828... | Exponential growth |
| **i** | Imaginary Unit | √-1 | Complex rotation |
| **π** | Pi | ≈ 3.14159... | Irrational ratio |

### Why This Demonstrates Irrationality

Because π is **irrational** (cannot be expressed as a fraction), the term `e^(iπθ)` creates a pattern that **never exactly repeats**. The interplay between the two exponential terms generates the mesmerizing, non-periodic curves you see! 

<div align="center">

```
Complex Plane Visualization
          
    Imaginary ↑
         Axis |
              |     • ───→ Each point:  z(θ)
    ──────────┼────────→ Real Axis
              |
              |
```

</div>

---

## 🛠️ Technical Details

- **Language:** Python 3.x
- **Graphics Library:** turtle
- **Math Libraries:** math, cmath
- **Scaling Factor:** 120x (optimized for screen display)
- **Step Size:** 0.01 radians per iteration
- **Pen Speed:** Maximum (0)

---

## 📸 What You'll See

Expect to see elegant, flowing curves that: 
- Start from a central point
- Spiral and weave in complex patterns
- Create flower-like or orbital shapes
- Continue evolving infinitely without repetition

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Feel free to use, modify, and share!  🎉

---

## 👤 Author

**Created with ❤️ by [willow788](https://github.com/willow788)**

---

<div align="center">

### ⭐ Star this repo if you enjoy mathematical art! ⭐

**Happy visualizing! 🥧✨**

</div>
