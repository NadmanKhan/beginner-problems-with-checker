# Beginner Problems With Checker

Some beginner-level algorithmic problems designed at the behest of a professor at my university for the purpose of providing a mild introduction to competitive programming to the freshers. Includes tests and a checker.

## How to use

Dependencies: Python 3, GCC

1. Clone the repository or download the zip file and extract it.
2. Go to the directory of the problem you want to solve, read the problem description in `description.pdf`, and write your solution wherever you want.
3. Run the checker with `python checker.py <problem-id> <path-to-your-solution>`. For example, if you want to check your solution to problem `A` and your solution is in `c:\Users\John\Desktop\solution.cpp`, run `python checker.py A c:\Users\John\Desktop\solution.cpp`. If the GCC compiler is not in your PATH, you can specify the path to it in the third argument, e.g. `python checker.py A c:\MinGW\bin\g++.exe c:\Users\John\Desktop\solution.cpp`.

## More problems

These problems are good for a start, but if you want to delve into the world of competitive programming, you should start solving problems on online judges like [Codeforces](https://codeforces.com/), [AtCoder](https://atcoder.jp/), [LightOJ](https://lightoj.com/), [SPOJ](https://www.spoj.com/), [CodeChef](https://www.codechef.com), [HackerRank](https://www.hackerrank.com) etc. There is also a nice website called [Vjudge](https://vjudge.net/) that acts as a "virtual judge" and allows you to solve problems from multiple online judges in one place.

Here are some more easy problems to get you started:

1. "IQ Test" on [Codeforces](https://codeforces.com/problemset/problem/25/A) or on [Vjudge](https://vjudge.net/problem/CodeForces-25A)
1. "Compare the Triplets" on [HackerRank](https://www.hackerrank.com/contests/may-world-codesprint/challenges/compare-the-triplets) or on [Vjudge](https://vjudge.net/problem/HackerRank-compare-the-triplets)
1. "Mini-Max Sum" on [HackerRank](https://www.hackerrank.com/contests/university-codesprint/challenges/mini-max-sum) or on [Vjudge](https://vjudge.net/problem/HackerRank-mini-max-sum)
1. "0 or 1 Swap" on [AtCoder](https://atcoder.jp/contests/abc135/tasks/abc135_b?lang=en) or on [Vjudge](https://vjudge.net/problem/AtCoder-abc135_b)
1. "Valid Triangles" on [CodeChef](https://www.codechef.com/problems/FLOW013) or on [Vjudge](https://vjudge.net/problem/CodeChef-FLOW013)

## How to add your own problems

Dependencies: Python 3, Pandoc (optional)

The `.judge` folder under each problem directory contains 4 files:

1. `description.md`: The problem description in Markdown format.
2. `correct_solution.c`: A correct solution to the problem in C.
3. `tests_script.py`: A Python script that generates the tests. The script must have a global variable `tests` which is a list of strings, each string being a test test input.
4. (optional) `tutorial.md`: A tutorial for the problem in Markdown format.

To add your own problem, create a new directory under `problems` and add the above 4 files to it. Additionally, if you want to convert the Markdown files to PDF, you need to have `pandoc` installed.

After creating the problem, run the Python script `.judge/gen.py` to generate all the tests and convert Makrdown to PDF if needed.
