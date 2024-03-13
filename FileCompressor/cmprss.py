import zipfile
import pathlib


def make_archive(paths, dest):
    dest_path = pathlib.Path(dest, 'cmprss.zip')
    with zipfile.ZipFile(dest_path, 'w') as a:
        for path in paths:
            path = pathlib.Path(path)
            a.write(path, arcname=path.name)


if __name__ == '__main__':
    print('cmprss')