from subprocess import call

from pyngrok import ngrok


def clone_github_private_repo(email: str, name: str) -> None:
    private_repo_commands = f'sh scripts/private_repo_clone.sh {email} {name}'
    call(private_repo_commands.split())


def connect_ngork():
    url = ngrok.connect(port=9000)
    return url


if __name__ == '__main__':
    print('Installing code-server for Google Colab')
    code_server_install_command = f'sh scripts/code_server_install.sh'
    call(code_server_install_command.split())

    email = input('Give email address for git config settings: ')
    name = input('Give name for git config settings: ')
    clone_github_private_repo(email, name)
    print('Add SSH key to your GitHub account')

    url = connect_ngork()
    code_server_start_command = f'nohup code-server --port 9000 --auth none'
    call(code_server_start_command.split())
    print('Now go to below address to use code-server')
    print(url)
