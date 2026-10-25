# Progress Log

## Week 1: Setup + Python via data

### Day 1, 2026-10-25 (hours: 4)

**Did:**
- Created public GitHub repo `brain-tumor-ai` with README, Python .gitignore and MIT license (via GitHub Desktop)
- Set up a Python 3.12 virtual environment (`.venv`) and installed numpy, pandas, matplotlib, pillow and jupyter
- Wrote `requirements.txt` with the 5 direct dependencies pinned to exact versions
- Created the project folder structure (`data/raw`, `notebooks`, `scripts`, `src`, `reports/figures`) with `.gitkeep` files
- Added `data/` to `.gitignore` before downloading the dataset
- Downloaded the Brain Tumor MRI Dataset (Masoud Nickparvar, CC BY 4.0) into `data/raw/`
- Wrote `scripts/check_env.py`: prints library versions and image counts per split and class
- Added Setup, Dataset and Known data issues sections to the README
- Found suspected augmented (`aug`) meningioma images in the dataset

**Errors and fixes:**
- Error: ImportError: DLL load failed ... Application Control policy
  Cause: Windows Smart App Control blocked pandas' compiled files
  Fix: turned off Smart App Control
- Error: AttributeError: 'WindowsPath' object has no attribute '________'
  Cause: I ran the script with the blanks still in it, so Python looked for a
  method literally named "________", which doesn't exist
  Fix: replaced the blanks with .iterdir() and .is_dir()
- Error: printed 4 files instead of 3
  Cause: count starts at 0 and the check was count <= 3, which is true for
  0, 1, 2 and 3: four values (off-by-one bug)
  Fix: changed the check to count < 3

**Learned:**
- .venv is a separate environment (sandbox) for one project, so its packages
  don't interfere with other projects.
- Tracebacks bottom-up: the last line tells you what went wrong; the top lines
  show where it started in your code.
- Generator: produces values one at a time, on demand, instead of building
  them all in memory at once.

**Why-answers:**
1. Pinning all 50+ sub-packages freezes their versions, so upgrading pandas
   later can fail because it needs newer sub-packages. pip freeze on Windows
   may also include Windows-only packages that break installs on Linux.
2. data/ is ignored, so everything inside it is ignored too, including a
   .gitkeep. Git would never commit it, so it does nothing.
3. A dataset in a Git repo makes it heavy, can violate patient privacy, and
   may break the dataset's license.
4. path.iterdir() returns a generator because it is lazy: it doesn't load all
   directory contents into memory at once.

**Data finding:**
- Suspected augmented images: only the meningioma folders contain files named
  "aug" (e.g. Tr-aug-me_1.jpg), probably added to balance the classes.
- Two risks for model evaluation:
  1. Augmented images in the test set can inflate accuracy.
  2. If augmented copies of the same original scan appear in both Training and
     Testing, that is data leakage.
- Not confirmed yet; inferred from filenames. To check on Day 2.

**Tomorrow:**
- Day 2