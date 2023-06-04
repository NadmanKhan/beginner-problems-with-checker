import os
import sys
import shutil
import importlib

if __name__ == '__main__':

    do_log = len(sys.argv) > 1 and sys.argv[1] == 'log'

    dotjudge_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(dotjudge_dir)
    problems_dir = os.path.join(root_dir, 'problems')

    def gen_pdf_from_md(md_path, out_dir, out_name):
        if not os.path.isfile(md_path):
            return False
        os.system(f'pandoc {md_path} -o {os.path.join(out_dir, out_name)}')
        return True

    tests_module = None

    for problem_dir_name in os.listdir(problems_dir):
        if not problem_dir_name[0].isupper():
            continue
        problem_dir_path = os.path.join(problems_dir, problem_dir_name)
        if not os.path.isdir(problem_dir_path):
            continue

        problem_name = problem_dir_path.replace('_', ' ')
        dotjudge_dir = os.path.join(problem_dir_path, '.judge')
        if not os.path.isdir(dotjudge_dir):
            print(
                f'Problem "{problem_name}" does not have a `.judge` directory!')
            continue

        # Generate `description.pdf`
        # ---

        description_path = os.path.join(dotjudge_dir, 'description.md')
        if not gen_pdf_from_md(description_path, problem_dir_path, 'description.pdf'):
            print(
                f'Problem "{problem_name}" does not have a `description.md` file!')
            continue

        # Generate `tutorial.pdf`
        # ---

        tutorial_path = os.path.join(dotjudge_dir, 'tutorial.md')
        if not gen_pdf_from_md(tutorial_path, problem_dir_path, 'tutorial.pdf'):
            print(
                f'Problem "{problem_name}" does not have a `tutorial.md` file!')
            continue

        # Generate tests folder from `tests_script.py`
        # ---

        tests_script_path = os.path.join(dotjudge_dir, 'tests_script.py')
        if not os.path.isfile(tests_script_path):
            print(
                f'Problem "{problem_name}" does not have a `tests_script.py` file!')
            continue

        sys.path.append(dotjudge_dir)
        tests_module = (
            importlib.reload(tests_module)
            if tests_module is not None else
            importlib.import_module('tests_script')
        )
        tests: list[str] = tests_module.tests
        sys.path.pop()

        tests_dir = os.path.join(problem_dir_path, 'tests')
        if os.path.isdir(tests_dir):
            shutil.rmtree(tests_dir)
        os.mkdir(tests_dir)

        if do_log:
            print(f'Generating tests for problem "{problem_name}"...')

        for test_idx, test in enumerate(tests):
            with open(os.path.join(tests_dir, f'{test_idx:02d}.txt'), 'w') as file:
                file.write(f'{test}\n')
                if do_log:
                    print(f'Written test: {test_idx}')
