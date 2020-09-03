import argparse
from subprocess import call


def get_args():
    parser = argparse.ArgumentParser("ArgumentParser to clone a private Github repository from Google Colab.")

    parser.add_argument('--name', type=str, help='Give name for Git config settings')
    parser.add_argument('--email', type=str, help='Give valid email address for Git config settings')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()
    commands = f'sh private_repo_clone.sh {args.email} {args.name}'
    call(commands.split())
