from functions.get_files_info import get_files_info

def test_get_files_info():

    # success
    print(get_files_info("calculator", "."))

    # error
    print(get_files_info("calculator", "/bin"))

    # error
    print(get_files_info("calculator", "../"))

    # error
    print(get_files_info("calculator", "main.py"))

test_get_files_info()