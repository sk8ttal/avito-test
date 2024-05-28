import subprocess
import os

def run_pytest():
    folder_path = 'tests/tests_eco_inpact'
    tests = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    for test in tests:
        try:
            result = subprocess.run(["pytest", f"{folder_path}/{test}"],
                                    check=False,
                                    text=True,
                                    stdout=subprocess.PIPE
                                    )
        finally:
            print('stdout:', result.stdout)
        
if __name__ == '__main__':
    run_pytest()
