# LearnPython_TheHardWay
- SOURCE: Learn Python the Hard Way. Third Edition
- CODE: Python 3.6
- OS: Ubuntu 18.04 LTS


### ex45.py - 'YOU MAKE A GAME: Lost in the forest'
- dependency: engine.py
- bash run: python3 ex45.py main_path


### ex46.py - 'A Project Skeleton'
#### Study Drills
4. Python script that's runnable in Ubuntu:
Start script with: #!/usr/bin/env python3
Change permissions to executable: chmod +x bin_sum.py
Check it by running: ./bin_sum.py
5. Mention bin_sum in the setup.py:
config = {
...
    'scripts': ['bin/bin_sum'],
...
}
When installed check with: dir(ex46_sum)
6. 
Use setup.py to test: working in progress
Run pip from package directory to install it: pip3 install ./ex46
Check installed package with: pip3 freeze
Check if it works importing all submodules: 
>>> import ex46_sum.ex46_sum 
>>> ex46_sum.ex46_sum.simple_sum()
Remember to unistall it!