import os,sys
import requests
import threading
import argparse
from tqdm import tqdm
from time import sleep
def clz():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
clz()

bann = '''
                 ___
               ,-----,
              /\|   |/\         Fetch All URL From The "PyFetch"
             |-- \_/ --|          T.me : https://t.me/RootKrd
          .-----/   \-----.           ____              ______         __            __  
         /   ,   . .   ,   \         / __ \   __  __   / ____/  ___   / /_  _____   / /_ 
        /  /`|    |    |'\, \       / /_/ /  / / / /  / /_     / _ \ / __/ / ___/  / __ \\
        `\ \  \-  |  -/  /`/'      / ____/  / /_/ /  / __/    /  __// /_  / /__   / / / /
          `\\_)`-- --'(_//         /_/       \__, /  /_/       \___/ \__/  \___/  /_/ /_/ 
            |_|`-- --'|_|  _______        /____/      
             ,'`-   -'`.,-'       `-.
            |\--------/||            `-.      _,------.
           |\---------/`|    .--.       `----'   ___--.`--.
            |\---------/\. ."    `.            ,'      `---'
             ``-._______.-'        `-._______.-'   Date Apr-13-2023

'''
print(bann)

def ufetch(url, output_file):
    api = f"https://web.archive.org/cdx/search/cdx?url={url}/*&output=text&fl=original&collapse=urlkey"
    response = requests.get(api)
    if response.status_code == 200:
        urls = response.text.strip().split('\n')
        for url in urls:
            output_file.write(url + '\n')
def main():
    parser = argparse.ArgumentParser(description='Fetch All URL From The "uFetch"')
    parser.add_argument('-u', '--url', type=str, required=True, help='The URL to fetch URLs for.')
    parser.add_argument('-t', '--threads', type=int, default=10, help='The number of threads to use for fetching URLs (Default 10).')
    parser.add_argument('-o', '--output', type=str, required=True, help='The name of the output file to write URLs to.')
    args = parser.parse_args()
    urls = set()
    clz()
    print(bann)
    for i in tqdm(range(20)):
        sleep(0.1)
    with open(args.output, 'w') as output_file:
        threads = []
        for i in range(args.threads):
            t = threading.Thread(target=ufetch, args=(args.url, output_file))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
if __name__ == '__main__':
    main()
