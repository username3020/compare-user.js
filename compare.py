import sys
import re
import dictdiffer
from tabulate import tabulate


def create_dict(file):
    dic = {}

    with open(file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for line in content:
        if line.startswith("user_pref"):
            results = re.match('user_pref\(\"(.+)\",\s*(.+)\s*\);', line)
            setting_name = results[1]
            setting_value = results[2]
            dic[setting_name] = setting_value
    return dic


def main(file1, file2, print_lines):
    dic1 = create_dict(file1)
    dic2 = create_dict(file2)

    currlist = []
    done = False

    print("Differences between {} and {}:".format(file1, file2))

    for diff in list(dictdiffer.diff(dic1, dic2)):

        if diff[0] == "change":
            currlist.append([diff[1][0], diff[2][0], diff[2][1]])

        if not done and diff[0] == "add":
            done = True
            if print_lines:
                for line in currlist:
                    print('user_pref("{}", {});'.format(line[0], line[2]))
            print(tabulate(currlist, headers=['Name', file1, file2],
                           tablefmt='orgtbl'))

        if diff[0] == "add":
            print("Only in {}".format(file1))
            if print_lines:
                for line in diff[1]:
                    print('user_pref("{}", {});'.format(line[0], line[1]))
            print(tabulate(diff[1], headers=['Name', 'Setting'],
                           tablefmt='orgtbl'))

            print("Only in {}".format(file2))
            if print_lines:
                for line in diff[2]:
                    print('user_pref("{}", {});'.format(line[0], line[1]))
            print(tabulate(diff[2], headers=['Name', 'Setting'],
                           tablefmt='orgtbl'))

        if diff[0] == "remove":
            print("Removed in {}".format(file1))
            if print_lines:
                for line in diff[1]:
                    print('user_pref("{}", {});'.format(line[0], line[1]))
            print(tabulate(diff[1], headers=['Name', 'Setting'],
                           tablefmt='orgtbl'))

            print("Removed in {}".format(file2))
            if print_lines:
                for line in diff[2]:
                    print('user_pref("{}", {});'.format(line[0], line[1]))
            print(tabulate(diff[2], headers=['Name', 'Setting'],
                           tablefmt='orgtbl'))


if __name__ == '__main__':
    print_lines = False
    if len(sys.argv) == 1:
        print("No arguments provided, using default filenames.")
        file1 = "user.js"
        file2 = "user.custom.js"
    elif len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    elif len(sys.argv) == 4:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        if sys.argv[3] == "-printLines":
            print_lines = True

    main(file1, file2, print_lines)
