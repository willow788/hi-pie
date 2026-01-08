# 🖥️ Developer Guide: hi-pie

## File Structure

- `Main Python code/hipi.py`: Visualization main script
- `Demonstration/message.txt`: Author’s personal note
- `README.md`: User documentation & overview
- `LICENSE`: MIT license

## How to Run & Modify

1. Install Python 3.x
2. Clone the repo
3. Run:
   ```bash
   python "Main Python code/hipi.py"
   ```
4. The code uses only built-in libraries (`turtle`, `math`, `cmath`)

## Customization

- **Modify formula**: Edit the core complex formula in `hipi.py`
- **Change drawing speed, color, or canvas size** by tweaking turtle API calls
- **Add saving/export features**—e.g., save screenshots with `turtle.getcanvas().postscript(...)`

## API Reference

The project is a script, but you can refactor it into functions/classes for:
```python
def generate_points(theta_max, step):
    # Generate list of complex points
    pass

def draw_pattern(points):
    # Use turtle graphics to draw
    pass
```
Feel free to add a full API and expose more customization options!

## Testing

Check visualization by running locally.
Visual output is primary—use screenshots or animated gifs for bug reports.

---

**Happy hacking & exploring!**
