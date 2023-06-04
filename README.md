# Beginner Problems With Checker

Some beginner-level algorithmic problems designed at the behest of a professor at my university for the purpose of providing a mild introduction to competitive programming to the freshers. Includes tests and a checker.

## How to use

1. Clone the repository or download the zip file and extract it.
2. Go to the directory of the problem you want to solve, read the problem description in `description.pdf`, and write your solution wherever you want.
3. Run the checker with `python3 checker.py <problem-id> <path-to-your-solution>`. For example, if you want to check your solution to problem `A` and your solution is in `~/Desktop/solution.cpp`, run `python3 checker.py A ~/Desktop/solution.cpp`. The checker will run your solution against all the tests and tell you if your solution is correct or not.

## How to add your own problems

The `.judge` folder under each problem directory contains 4 files:

1. `description.md`: The problem description in Markdown format.
2. `correct_solution.c`: A correct solution to the problem in C.
3. `tests_script.py`: A Python script that generates the tests. The script must have a global variable `tests` which is a list of strings, each string being a test test input.
4. (optional) `tutorial.md`: A tutorial for the problem in Markdown format.

To add your own problem, create a new directory under `problems` and add the above 4 files to it. Additionally, if you want to convert the Markdown files to PDF, you need to have `pandoc` installed.

After creating the problem, run the Python script `.judge/gen.py` to generate all the tests and convert Makrdown to PDF if needed.
