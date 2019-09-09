import subprocess
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
default_build_dir = os.path.join(script_dir, '../build')


def _get_cmake_invocation(args):
    invocation = ['cmake', root_dir, '-G', 'Ninja']
    invocation.append('-DCMAKE_BUILD_TYPE=RELEASE')

    return invocation


def _get_build_invocation(args):
    invocation = ['cmake', '--build', default_build_dir]

    return invocation


def main():
    args = []
    if not os.path.exists(default_build_dir):
        os.mkdir(default_build_dir)
    subprocess.check_call(_get_cmake_invocation(args), cwd=default_build_dir)
    subprocess.check_call(_get_build_invocation(args), cwd=root_dir)


if __name__ == "__main__":
        main()

