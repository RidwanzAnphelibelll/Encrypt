# Jangan Di Ubah Ya Dek!!!

import os, base64, sys, time
from pprint import pformat
# Emoji unicode list
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]

MAX_STR_LEN = 70
OFFSET = 10

# Basic colors
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

# Snippets
ask = green + '\n[' + white + '?' + green + '] '+ yellow
success = green + '\n[' + white + '√' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
info= yellow + '\n[' + white + '+' + yellow + '] '+ cyan

# Current Directory
pwd=os.getcwd()
# Normal slowly printer
def sprint(sentence, second=0.05):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
# Base64 encoder function
def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")

def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )

# Encrypt Bash code by npm package "bash-obfuscate"
def encryptsh():
    in_file = input(ask + "Input Filename  > "+cyan)
    if not os.path.exists(in_file):
        sprint(error+'File not found')
        encryptsh()
    os.system("bash-obfuscate " + in_file + " -o .temp")
    if not os.path.exists(".temp"):
        try:
            sprint(info+"Installing Bash-Obfuscate....\n")
            os.system("apt install nodejs -y && npm install -g bash-obfuscate")
            os.system("bash-obfuscate " + in_file + " -o .temp")
        except:
            sprint(error+" Bash-Obfuscate not installed! Install it by:\n"+green+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
            exit(1)
    out_file= input(ask + "Output Filename  > " + green)   
    with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
        filedata = temp_f.read()
        out_f.write(""+filedata)
    os.remove(".temp")
    sprint(f"{success}{out_file} saved in {pwd}")
    exit()
    
# Encrypting python file into base64 variable, easily decryptable
def encryptvar():
    var= input(ask + "Variable to be used(Must Required)  > " + green)
    if (var==""):
        sprint(error + " No variable")
        encryptvar()
    if (var.find(" ")!= -1):
        sprint(error+" Only one word!")
        encryptvar()
    iteration = input(ask + "Iteration count for variable  > " + green)
    try:
        iteration = int(iteration)
    except Exception:
        iteration = 50
    VARIABLE_NAME = var * iteration
    in_file = input(ask+ "Input file  > "+cyan)
    if not os.path.isfile(in_file):
        print(error+' File not found')
        encryptvar()
    out_file = input(ask + "Output file  > " + green)
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f,open(out_file, 'w') as out_f:
       file_content = in_f.read()
       obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
       out_f.write(""+obfuscated_content)
    sprint(f"{success}{out_file} saved in {pwd}")
    exit()

# Encrypting python file into emoji
def encryptem():
    in_file= input(ask +"Input File  > "+cyan )
    if not os.path.isfile(in_file):
        print(error+' File not found')
        encryptem()
    out_file= input(ask + "Output File  > " + green)
    with open(in_file) as in_f, open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("")
        out_f.write(encode_string(in_f.read(), alphabet))
        sprint(f"{success}{out_file} saved in {pwd}")
        exit()

# Main function
def main():
    os.system("clear")
    print(f"{green}[1]{yellow} Encrypt{cyan} Bash")
    print(f"{green}[2]{yellow} Encrypt{cyan} Python into Variable")
    print(f"{green}[3]{yellow} Encrypt{cyan} Python into Emoji")
    print(f"{green}[4]{yellow} More Tools")
    print(f"{green}[0]{yellow} Exit")   
    choose = input(f"{ask}{blue}Choose an option : {cyan}")
    while True:
        if choose == "1" or choose=="01":
            encryptsh()
        elif choose == "2" or choose=="02":
            encryptvar()
        elif choose == "3" or choose=="03":
            encryptem()
        elif choose == "4" or choose=="04":
            if os.path.exists("/data/data/com.termux/files/home"):
               
                os.system("xdg-open 'https://github.com/RidwanzAnphelibelll'")
            main()
        elif choose == "0":
            exit()
        else:
            main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sprint(info+"Thanks for using. Have a good day!")
        exit()
    except Exception as e:
        sprint(error+str(e))