# 🤓 Deep Dive: The Mathematics of hi-pie

## Core Formula

The visual pattern is traced by:
```python
z(θ) = e^(iθ) + e^(iπθ)
```
where:
- `e` is Euler's number (~2.71828)
- `i` is the imaginary unit (√-1)
- `π` is pi (≈ 3.14159...)
- `θ` is an angle parameter (in radians)

## Why the Pattern Never Repeats

π is irrational: it cannot be written as a simple fraction.  
As θ increments, `e^(iπθ)` cycles through all possible values on the complex plane, never landing on the same spot twice — producing beautiful, infinite spirals.

### Mathematical Concepts Involved

- **Complex Numbers**: Each point has real and imaginary parts.
- **Euler’s Formula**: `e^(ix) = cos(x) + i·sin(x)`
- **Irrationality**: π means the second term zig-zags unpredictably.
- **Visualization**: Connecting each point gives a continuous, infinitely-evolving curve.

## Explore More

Try changing the formula in `hipi.py`!  
Experiment with:
- Other irrational multiples (`e^(i√2θ)`)
- Additional terms
- Color gradients tied to theta or speed

**Learn and play—mathematics is art!**
