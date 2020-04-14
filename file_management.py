import shutil
import time
import os

directory = 'C:/Users/bnh03/Desktop'

new_directories = [
    "University",
    "Unsorted"
]

actions = {
    'Images': ('.png', '.jpg', '.gif', '.svg', '.jpeg', '.dxf'),
    'Videos': ('.mp4', '.mov', '.avi'),
    'Programs': ('.exe', '.bin', '.msi'),
    'Compressed': ('rar', 'zip'),
    'Audio': ('.wav', '.mp3', '.ogg', '.flac'),
    'Documents': ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.pdf'),
    'OS': ('.iso'),
    'Python': ('.py'),
    'Other': None
}

uni_strings = [
    "ENGG433",
    "ENGG439",
    "ENGG456",
    "ENGG461",
    "INFO411",
    "MATH313",
    "MECH311",
    "MECH431",
    "Assignment",
    "Lab",
    "lab"
    ]


def check_directory(dir, search, neg=False):
    if search in os.listdir(dir):
        return not neg
    else:
        return neg


def create_directories(dir):
    for direct in new_directories:
        if check_directory(dir, direct, neg=True):
            os.mkdir(dir + '/' + direct)
    for dir_name in actions.keys():
        if check_directory(dir, dir_name, neg=True):
            os.mkdir(dir + '/' + dir_name)


def clear_new_folders(dir):
    clean_directory = dir + '/Unsorted'
    for file in os.listdir(dir):
        if (('New' in file) or ('New' in file)) and (('folder' in file) or ('Folder' in file)):
            print(file)
            operating_directory = dir + '/' + file
            for unsorted_file in os.listdir(operating_directory):
                file_location = operating_directory + '/' + unsorted_file
                try:
                    shutil.move(file_location, clean_directory)
                except IOError:
                    print('Permission Denied: ' + file_location)


def remove_empties(dir):
    count = 0
    for file in os.listdir(dir):
        if (file == 'desktop.ini') or ('My ' in file) or (file in actions.keys()):
            count += 1
            # print(file + ' excluded')
        else:
            operating_directory = dir + '/' + file
            if len(os.listdir(operating_directory)) == 0:
                try:
                    os.rmdir(operating_directory)
                except IOError:
                    print(file + ' Not removed.')


def move_folders(dir, str_array, folder_name):
    for file in os.listdir(dir):
        if any(uni_string in file for uni_string in str_array):
            source_path = dir + '/' + file
            destination_path = dir + '/' + folder_name
            shutil.move(source_path, destination_path)


def downloads_organizer(dir):
    for file in os.listdir(dir):
        if os.path.isfile(directory + '/' + file):
            source_path = dir + '/' + file
            for destination, extensions in actions.items():
                if extensions is None or file.endswith(extensions):
                    destination_path = os.path.join(dir, destination, file)
                    try:
                        shutil.move(source_path, destination_path)
                    except IOError:
                        print("Permission Denied: " + file)
                    break


def print_directory(dir):
    for file in os.listdir(dir):
        print(file)


def collate_pycharm(dir):
    count = 0
    if check_directory(dir, "PyCharm", neg=True):
        os.mkdir(dir + '/PyCharm')
    for file in os.listdir(dir):
        if file == 'desktop.ini' or ('My ' in file):
            count += 1
            # print(file)
        else:
            operating_directory = dir + '/' + file
            if '.idea' in os.listdir(operating_directory):
                shutil.move(operating_directory, dir + '/PyCharm')


if __name__ == "__main__":
    try:
        # clear_new_folders(directory)
        # remove_empties(directory)
        # collate_pycharm(directory)
        print_directory(directory)
        # create_directories(directory)
        # downloads_organizer(directory)
        # move_folders(directory, uni_strings, "University")
        # time.sleep(10)

    except KeyboardInterrupt:
        print('interrupted!')