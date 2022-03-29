'''
*概述
*
'''
from BVFTPFuctions import FTPFuc
from OtherFuc import UseFulFuc
from SSHFuction import SSHClass

if __name__ == '__main__':
    username = "pi"
    password = "mitac2019pi"

    #控制參數區
    DebugSw=1
    Cmd=0

    # 取得初始化參數
    BVIP=UseFulFuc.GetInitParameter('InitFile.ini')
    UseFulFuc.Ctrlprint('BVIP:'+BVIP, DebugSw)
    #登入BV4
    SSH=SSHClass(BVIP,username,password)
    #設定Debug線程
    #t = threading.Thread(target=ser.DebugCtrl)

    while (Cmd != 99):
        #輸出選單
        print("1.下載並刪除資料")
        print("2.清除資料")
        print("3.時間變更")
        print("4.時間初始化")
        print("5.即時傳輸資料")
        print("6.讀卡機電源關閉")
        print("98.重新連線")
        print("99.離開")
        Cmd=input('請輸入要執行的功能:\n')

        try:
            if Cmd == '1':
                print("開始取得資料...")
                TargetFile = FTPFuc.CheckFileExist(BVIP,username,password)
                if len(TargetFile) > 0:
                    # 下載Log資料
                    FTPFuc.GetInboxfile(TargetFile, BVIP,username,password)
                    # 刪除資料
                    FTPFuc.DeleteTargetFolder(TargetFile, BVIP,username,password)
                else:
                    print("無交易資料!!!")
            elif Cmd == '2':
                TargetFile = FTPFuc.CheckFileExist(BVIP,username,password)
                UseFulFuc.Ctrlprint(TargetFile, 1)
                if len(TargetFile) > 0:
                    FTPFuc.DeleteTargetFolder(TargetFile, BVIP,username,password)
                else:
                    print("無交易資料!!!")
            elif Cmd=='3':
                ChangeTimeAction=input('請輸入變更時間(不變更輸入0)')
                if ChangeTimeAction=='':
                    ChangeTimeAction='0'
                SSH.SetBVTimeProcess(ChangeTimeAction)
            elif Cmd == '4':
                print("1.設為現在時間(UTC)")
                print("2.設為早上00點(UTC)")
                print("3.設為現在時間(UTC+8)")
                InitTimeAction = input('請輸入執行項目')
                if InitTimeAction == '1' or InitTimeAction == '2' or InitTimeAction == '3':
                    SSH.InitTimeProcess(InitTimeAction)
                else:
                    print("指令錯誤!!!")
            elif Cmd == '5':
                SSH.CheckOnline()
            elif Cmd == '6':
                SSH.ReaderPowerOff()

            elif Cmd=='98':
                SSH = SSHClass(BVIP, username, password)
            elif Cmd == '99':
                break
            else:
                print("無該功能!")

        except:
            print("連線失敗!!")


