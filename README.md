```python
# Path to libtbb.so.2
tbb_path = '/snap/blender/4300/lib'

# Add the path to LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = f"{tbb_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"
```

## Running the Program

1. **Navigate to the repository directory after downloading.**
```bash
cd [path/to/repository]
```
2. **Run the program.**
```bash
make all
```
3. **Results are displayed in the `log` file next to the Makefile.**

## Dependencies

When running the program (`make all`), it will check for the required dependencies and **automatically install them** if missing:
- python-sat
- python-constraint
- libopenblas-base
- libtbb-dev

