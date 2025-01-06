```python
# Path to libtbb.so.2
tbb_path = '/snap/blender/4300/lib'

# Add the path to LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = f"{tbb_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"
```

Run the program.
```bash
make all
```
Les résultats seront affichés dans le fichier log
