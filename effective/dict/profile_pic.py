from collections import defaultdict

path = 'sagor.jpg'


def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise


# pictures = defaultdict(open_picture)
# handle = pictures[path]
# handle.seek(0)
# image_data = handle.read()


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
print(image_data)
