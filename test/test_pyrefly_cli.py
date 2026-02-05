import os
from pathlib import Path
import subprocess
import time
import unittest

parent_directory = Path(__file__).resolve().parent.parent

first_path = parent_directory / "src/issue_unused_ignores/first.py"
second_path = parent_directory / "src/issue_unused_ignores/second.py"
third_path = parent_directory / "src/issue_unused_ignores/third.py"

def run_pyrefly_check():
    cmd = ["pyrefly", "check", "--remove-unused-ignores", "src/issue_unused_ignores/first.py", "src/issue_unused_ignores/second.py", "src/issue_unused_ignores/third.py"]
    subprocess.run(cmd, cwd=parent_directory)

def cleanup():
    cmd = ["git", "reset", "--hard", "HEAD", "--", "src/issue_unused_ignores/first.py", "src/issue_unused_ignores/second.py", "src/issue_unused_ignores/third.py"]
    subprocess.run(cmd, cwd=parent_directory)

class TestPyreFlyCLI(unittest.TestCase):
    
    # `pyrefly check --remove-unused-ignores`
    # the above command always modifies every file, even when:
    # 1. there are no "# pyrefly: ignore" comments
    # 2. there are used "# pyrefly: ignore" comments
    #
    # this shouldn't happen, only files with unused 
    # "# pyrefly: ignore" comments should be modified
    def test_pyreflyCheck_shouldNotModifyUnrequiredFiles_whenRemoveUnusedIgnoresFlagIsPassed(self):
        initial_first_time_stamp = os.path.getmtime(first_path)
        initial_second_time_stamp = os.path.getmtime(second_path)
        initial_third_time_stamp = os.path.getmtime(third_path)
        
        run_pyrefly_check()
        
        post_first_time_stamp = os.path.getmtime(first_path)
        post_second_time_stamp = os.path.getmtime(second_path)
        post_third_time_stamp = os.path.getmtime(third_path)
        
        # src/issue_unused_ignores/first.py and src/issue_unused_ignores/second.py should go unmodified after running cmd
        self.assertEqual(
            initial_first_time_stamp, post_first_time_stamp, 
            "first.py was modified when it should not have been."
        )
        self.assertEqual(
            initial_second_time_stamp, post_second_time_stamp,
            "second.py was modified when it should not have been."
        )
        # src/issue_unused_ignores/third.py should be modified after running cmd as it has an unused ignore
        self.assertNotEqual(
            initial_third_time_stamp, post_third_time_stamp,
            "third.py was unmodified, when it should have been modifed."
        )

if __name__ == "__main__":
    unittest.main()
    print(os.getcwd())