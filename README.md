# Python Lessons for FRC™

Welcome to the wonderful world of Python programming! Whether you've got years of experience or you're completely new 
to the concept of software, these lessons are designed to give an interactive, comprehensive (enough) introduction to 
programming in Python, specifically in the environment of FIRST™ Robotics.


## Getting Started
### What You'll Need
Each item has a link to a download, which you can use directly or as reference.
- [Python 3](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/) - This will be your primary editor for these lessons.
- [Python VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://jupyter.org/install)
  - This is installed from the command line. This can be accessed in VS Code by typing ctrl+` (backtick, upper left of keyboard).
- [Jupyter VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 
  - This is optional, since VS Code has native support for Jupyter Notebooks.
  - Alternatively, you can use [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) for a more feature-complete 
    experience, though this does complicate the workflow.
<!-- - [Draw.io integration VS Code extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) - for easily making flowcharts -->

Each of the extensions can be installed directly within VS Code.  

### Getting the Lessons
You can get the lessons by first forking the repository on Github. If you're on the main repository page (which you probably
are if you're reading this) and you're logged in to Github, then you can go up to the "Fork" button in the upper right corner.
Click that, and you'll have your own copy of the lessons. You can then use your method of choice to download the files locally.

#### Downloading via `git` with Visual Studio Code (Recommended)
On the main GitHub repository page (likely the page you're on right now), click on the green "Code" button. On the 
dropdown that appears, click on the "HTTPS" tab, then copy the URL that appears under the tab (you can click the copy button 
immediately to the right). 

Open a new VS Code window, making sure there isn't any project open. In the "Explorer" tab on the right, click the "Clone 
Repository" button, then paste the URL you copied into the popup that appears, then press Enter. Pick a location for the 
repository (on Windows, somewhere under "My Documents" is recommended, particularly in a dedicated Python folder)

#### Downloading via `zip`
On the main GitHub repository page (likely the page you're on right now), click on the green "Code" button. On the 
dropdown that appears, click the "Download ZIP" button, then place in a location of your choice (on Windows, somewhere 
under "My Documents" is recommended, especially for this approach).

### Using the Lessons
These instructions assume you'll be using VS Code, so you'll need to adjust your approach if that's not what you're using. 
However, the VS Code approach is strongly encouraged, especially if you're newer to programming.

Once you've opened the lessons, you'll can open a specific lesson by double-clicking on the file that pops up. Each lesson is 
prefixed by a number, so they should be in vertical order, except the projects, which are ordered differently because they're 
folders. Specifically, the lessons are in the "ipynb" files.

Once you open a lesson, you can start reading. Any time you get to a section with code that looks like it's in a specially 
highlighted box, you can press the "Run" button that appears to the left of the box (the triangle pointing right). This will 
run the code in the box, including any changes you may have made. Additionally, these sections are editable, so you can 
rewrite the code way way you wish. The same goes for any normal text. That just requires a double-click, and is how you do 
written exercises (as opposed to programming exercises).

Some later lessons have code that grades the programming exercises, specifically in pass/fail fashion. These are code cells,
just like any other, and can be run using the "Run" button. It's strongly encouraged to not change these, as that can change 
the ability to grade that exercise. However, there are techniques used in these graders that aren't taught in the lessons, 
so they could be useful learning references in and of themselves.

### Caveats
#### Design Expectations
These lessons are designed to be done by students on their own time, and as such they are structured more like an 
interactive textbook, rather than a lesson plan. Additionally, the exercises are designed such that the student 
is expected to get all the answers correct before moving on, and as such it is largely incompatible with standard 
letter-grading systems. This is not intended for large-classroom use, but for more of a flipped, one-on-one approach, which 
is suited to the extracurricular, mentor-based system that is used by many FRC teams. If you use these lessons for 
anything outside these design expectations, you're mileage may vary, and good luck.

#### Content Expectations
The author of these lessons is not an expert in Python, and these should not be considered a thorough exploration of 
the Python programming language, or any other tools used in these lessons. There are almost certainly going to be 
inaccurate or incorrect material contained within. In many cases, these are the result of simplification for 
educational purposes, in order to accommodate all learning levels.



## License
This repository and all derivative repositories are licensed under a modified version of the [CC-BY-4.0](./LICENSE.txt) 
license. This means that you can use and distribute these lessons as you see fit, as long as you disclose the changes you 
made to them, if any, and keep the license with it. There is an added exception to license, an informal explanation of 
which follows. (See the license file for the full text).

#### Exception
If you publish the lessons with solutions to the exercises on, for example, Github, you are not 
required to indicate that you're including the solutions - other changes must still be declared. This is intended 
primarily so that students that don't have any licensing experience can publish their solutions without violating copyright.


## Contributing
If you want to help improve these lessons, feel free to make a pull request. Listing the changes you made will make 
your pull request more likely to be accepted (this has nothing to do with the license - it just makes maintainers' lives easier).


[Original material](https://github.com/KellenWatt/python-lessons) is ©2022 Kellen Watt
