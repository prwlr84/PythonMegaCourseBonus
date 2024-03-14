import zipfile
import pathlib


def unzip_archive(path, dest):
    dest_path = pathlib.Path(dest)
    path = pathlib.Path(path)
    with zipfile.ZipFile(path, 'r') as a:
        a.extractall(dest_path)


if __name__ == '__main__':
    print('cmprss')