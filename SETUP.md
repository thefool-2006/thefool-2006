# How to install (delete this file before pushing if you like)

1. On GitHub, create a PUBLIC repo named exactly `rachi2006` (same as your username).
2. Upload `README.md` and the `assets/` folder to it (keep the folder structure).
   If the repo already exists, replace its README.md.
3. Replace `YOUR-LINKEDIN-ID` in README.md, and `add-your-linkedin` in tools/build_terminal.py.

## Add your real dotted portrait
    pip install pillow
    python tools/photo_to_dots.py your_photo.jpg assets/portrait_dots.svg
    python tools/build_terminal.py        # rebuilds assets/terminal.svg with your face
Commit the new assets/terminal.svg. Until then a placeholder silhouette is shown.

## Edit text
Change the INFO / STACK / GRID lists at the top of tools/build_terminal.py and re-run it.
Edit REPOS in tools/build_projects.py the same way (e.g. add DevMind, SkillPath, NOVA once public).
