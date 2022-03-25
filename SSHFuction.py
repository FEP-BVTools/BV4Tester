import paramiko
from OtherFuc import UseFulFuc

class SSHClass:
    def __init__(self, server,user,pw):

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(server, username=user, password=pw, timeout=1)
        print('登入成功')

    def CmdMode(self):
        print('已進入命令模式,離開輸入qq')
        while(1):
            cmd=input('(CmdMode):')
            if cmd=='qq':
                print('離開命令模式')
                break

            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            result = stdout.readlines()
            print (result)

    def SetBVTimeProcess(self, ChangeTimeAction):
        TimeType = 'H'
        while (1):
            UseFulFuc.ShowTimeType(TimeType)
            try:
                if TimeType == 'H' or TimeType == 'm':
                    print("時間變更量:", ChangeTimeAction)
                    stdin, stdout, stderr =self.ssh.exec_command('date "+%Y:%m:%d:%H:%M:%S"\r\n'.encode())
                    Bvdate = stdout.readline()  # 替代為時間
                    print('NowTime:'+Bvdate)
                    TargetDate = UseFulFuc.ChangeTimeProcess(Bvdate, eval(ChangeTimeAction), TimeType)
                    Cmdline='sudo date {}'.format(TargetDate).encode()
                    self.ssh.exec_command(Cmdline)

                else:#尚未完善
                    print('植入日期')
                    if TimeType == 'Y':
                        # 取得BV年份
                        self.ser.write('date "+%Y"\r\n'.encode())
                        Bvdate = self.ser.readline()  # 該段為指令回應值
                        Bvdate = self.ser.readline()  # 替代為時間

                        TargetYear = str(eval(Bvdate.decode("ascii").rstrip()) + eval(ChangeTimeAction))

                        # 取得完整時間格式
                        self.ser.write('date "+%m%d%H%M.%S"\r\n'.encode())
                        Bvdate = self.ser.readline()  # 該段為指令回應值
                        Bvdate = self.ser.readline()  # 該段為指令回應值
                        Bvdate = self.ser.readline()  # 替代為時間
                        EntireBvdate = Bvdate.decode("ascii").rstrip()

                        # 設定日期
                        TargetDate = TargetYear + EntireBvdate
                        self.ser.write('date {}\r\n'.format(TargetDate).encode())

                break
            except:
                print('except process!')
                if len(ChangeTimeAction) == 1 and ChangeTimeAction.isalpha():
                    if ChangeTimeAction == 'H' or ChangeTimeAction == 'm' or ChangeTimeAction == 'Y' or ChangeTimeAction == 'M':
                        print("已變更時間單位!")
                        TimeType = ChangeTimeAction
                    else:
                        print('輸入格式錯誤!!!')
                        break
    def InitTimeProcess(self,InitTimeAction):
        TargetInitTime=UseFulFuc.InitTimeActionFuc(InitTimeAction)
        self.ssh.exec_command('sudo date {}'.format(TargetInitTime).encode())
        self.ssh.exec_command('sudo hwclock --systohc'.encode())#同步到硬體時間

if __name__ == '__main__':
    SSH=SSHClass('10.42.0.51','pi','mitac2019pi')
    #SSH.CmdMode()
    SSH.InitTimeProcess('3')