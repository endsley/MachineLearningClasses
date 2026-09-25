# 3D demos for the linear-algebra lectures

Animations of vectors, rotations, projections and point clouds, drawn with
[Panda3D](https://www.panda3d.org/). Each script is standalone — run it and a
3D window opens.

## Running a demo

```bash
python space.py          # or rotate_cloud.py, projection_Orthogonal.py, ...
```

That is the whole setup. The first run installs Panda3D, imageio and NumPy
automatically, into whichever Python you just used, and takes a minute or two.
After that it starts immediately.

If you would rather install them yourself first:

```bash
python -m pip install -r requirements.txt
```

## Run these on your own computer

The demos open a real 3D window, so they need a normal desktop session. They
will **not** work in Google Colab, in a Docker container, or over a plain
`ssh` login — there is no screen to draw on. Pre-rendered animations of every
demo are in [`imgs/`](imgs/) if you only want to see the result.

## If something goes wrong

| What you see | What it means |
|---|---|
| `ModuleNotFoundError: No module named 'direct'` | Panda3D is not installed. `direct` is **part of Panda3D** — `pip install direct` installs an unrelated package and will not fix it. Install `panda3d`. |
| "I installed it and it still says it's missing" | It went into a different Python than the one running the file. VS Code, PyCharm, conda and Jupyter each use their own interpreter. Run `python -m pip install panda3d` with the *same* `python` you run the demo with, or just let `space.py` do it for you. |
| Missing in a Jupyter notebook | Use `%pip install panda3d imageio` (not `!pip` — `%pip` installs into the kernel you are actually running), then restart the kernel. |
| `No matching distribution found for panda3d` | Usually an old pip that cannot see the current wheels: `python -m pip install --upgrade pip`, then try again. Panda3D supports Python 3.14 from version 1.10.15 onward. |
| `ModuleNotFoundError: No module named 'space'` | Run the script from inside this folder — the demos import `space.py`, which must sit next to them. |
| `NameError: name 'X̂' is not defined` in `perspective_shift_rotation_practice.py` | Expected — that file is the practice version with the line left blank for you to fill in. `perspective_shift_rotation.py` is the worked solution. |
| The window never appears, or an OpenGL error | You are on a machine with no display (see above), or your graphics driver is too old. |

To turn the automatic install off, set `PANDA3D_AUTO_INSTALL=0`.

## What is in here

`space.py` is the shared library — the coordinate axes, the camera controls,
the point-cloud helper and the GIF recorder. Every other script imports it, so
keep it in the same folder. The rest are the individual demos: rotations
(`rotate_cloud.py`, `rotating_vector.py`), projections
(`projection_Orthogonal.py`, `projection_nonOrthogonal.py`), moving meshes
(`mv_Luffy.py`, `load_house.py`, `airplane_fly_rotating.py`) and a homework
starter (`hw3_q4.py`).

### Keys inside a demo

| Input | Action |
|---|---|
| drag with left mouse button | orbit the camera |
| scroll wheel | zoom in / out |
| `f` | toggle fullscreen |
| `r` | start recording; press again to stop and write `record.gif` |
| `F9` | save `screenshot.png` |

Both files are written into the folder you ran the script from.
