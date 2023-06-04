import sys
import os
import shutil


if __name__ == '__main__':

    # Parse command line arguments
    # ---

    if len(sys.argv) < 3:
        print(f'Usage:   \tpython check.py <problem_id> '
              f'<src_path> [<compiler_path>]')
        print(f'Example: \tpython check.py A '
              f'{os.path.join("solutions", "A.c")}')
        print(f'Example: \tpython check.py B '
              f'{os.path.join("solutions", "B.c")} {os.path.join("bin", "g++")}')
        exit(1)

    root_dir = os.path.dirname(os.path.realpath(__file__))

    problem_id = sys.argv[1]
    if len(problem_id) != 1 or not problem_id.isalpha():
        print('Problem id must be a single letter')
        exit(1)
    
    problems_dir = os.path.join(root_dir, 'problems')
    problem_dirname = ''
    for dirname in os.listdir(problems_dir):
        if dirname.startswith(problem_id.upper() + '_'):
            problem_dirname = dirname
            break
    if not problem_dirname:
        print('Problem does not exist')
        exit(1)
    problem_dir = os.path.join(problems_dir, problem_dirname)
    if not os.path.isdir(problem_dir):
        print('Problem does not exist')
        exit(1)

    user_src_path = sys.argv[2]
    if not os.path.isfile(user_src_path):
        print('Solution file does not exist')
        exit(1)

    compiler_path = sys.argv[3] if len(sys.argv) > 3 else 'g++'

    # Compile user's solution and judge's solution
    # ---

    tmp_dir = os.path.join(root_dir, 'tmp')
    if not os.path.exists(tmp_dir):
        os.mkdir('tmp')

    user_bin_path = os.path.join(tmp_dir, 'user_soln')
    os.system(f'{compiler_path} {user_src_path} -o {user_bin_path}')
    if not os.path.exists(user_bin_path):
        print('Compilation failed')
        exit(1)

    judge_src_path = os.path.join(problem_dir, '.judge', 'correct_solution.c')
    if not os.path.exists(judge_src_path):
        print('Judge solution does not exist')
        exit(1)

    judge_bin_path = os.path.join(tmp_dir, 'judge_soln')
    os.system(f'{compiler_path} {judge_src_path} -o {judge_bin_path}')
    if not os.path.exists(judge_bin_path):
        print('Judge solution compilation failed')
        exit(1)

    # Run tests
    # ---

    print()
    print(
        f'🔍 Testing your solution (at {user_src_path}) for Problem {problem_id}...')
    print()

    tests_dir = os.path.join(problem_dir, 'tests')
    results = []

    for test_file_name in sorted(os.listdir(tests_dir)):
        if os.path.isdir(test_file_name):
            continue
        test_num = int(test_file_name.split('.')[0])
        print(f'🏁 {f"Test #{test_num}":>9}: ', end='')

        test_file_path = os.path.join(tests_dir, test_file_name)
        judge_ans_path = os.path.join(tmp_dir, 'judge_ans.txt')
        user_ans_path = os.path.join(tmp_dir, 'user_ans.txt')

        os.system(f'{user_bin_path} < {test_file_path} > {user_ans_path}')
        os.system(f'{judge_bin_path} < {test_file_path} > {judge_ans_path}')

        user_ans = list(map(lambda x: x.strip(),
                            filter(lambda x: not x.isspace(),
                                   open(user_ans_path).readlines())))

        judge_ans = list(map(lambda x: x.strip(),
                             filter(lambda x: not x.isspace(),
                                    open(judge_ans_path).readlines())))

        passed = (user_ans == judge_ans)

        if passed:
            results.append(True)
            print('Passed 🟢')
        else:
            results.append(False)
            print('Failed 🔴')


    # Give final verdict
    # ---

    print(f'🌟 {"Passed":>9}: {results.count(True)}/{len(results)} Tests')
    print(f'🎯 {"Verdict":>9}: ', end='')
    if all(results):
        print('Accepted ✅')
    else:
        print('Wrong Answer ❌')
    

    # Clean up
    # ---

    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
