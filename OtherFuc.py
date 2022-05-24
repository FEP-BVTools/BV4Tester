import os
import time
from time import gmtime, strftime

class UseFulFuc:
    def GetInitParameter(InitInfoFileName,ResetIP):
        if os.path.exists(InitInfoFileName) and ResetIP==0:
            IPFile=open(InitInfoFileName)
            IPPosion=IPFile.readline().strip()
        else:
            while(1):
                IPPosion=input('請輸入IP位置:')
                if IPPosion!='':
                    f=open(InitInfoFileName,mode='w+')
                    f.write(IPPosion)
                    break
                else:
                    print('IP不可為空值!!')
        return IPPosion

    def Ctrlprint(words, sw):
        if (sw == 1):
            print(words)

    def ShowTimeType(TimeType):
        if TimeType == 'H':
            print('目前時間單位:小時')
        elif TimeType == 'm':
            print('目前時間單位:分鐘')
        elif TimeType == 'Y':
            print('目前時間單位:年份')
        elif TimeType == 'M':
            print('目前時間單位:月份')

    def ChangeTimeProcess(Bvdate, DeltaTime, TimeType):
        #BvdateString = Bvdate.decode("ascii").rstrip()
        struct_time = time.strptime(Bvdate.rstrip(), "%Y:%m:%d:%H:%M:%S")  # 轉成時間元組
        time_stamp = int(time.mktime(struct_time))  # 轉成時間戳

        if TimeType == 'H':
            DeltaTime = DeltaTime * 3600
        else:
            DeltaTime = DeltaTime * 60

        TargetStamp = time_stamp + DeltaTime

        t = time.localtime(TargetStamp)
        result = time.strftime("%m%d%H%M%Y.%S", t)

        return result

    def InitTimeActionFuc(InitTimeAction):
        if InitTimeAction == '1':
            TargetInitTime = strftime("%m%d%H%M.%S", gmtime())
        elif InitTimeAction == '2':
            TargetInitTime = str(time.strftime("%m%d"))
            TargetInitTime = TargetInitTime + "0000.00"
        elif InitTimeAction == '3':
            TargetInitTime = strftime("%m%d%H%M.%S", time.localtime())
        return TargetInitTime

if __name__ == '__main__':
    struct_time =UseFulFuc.InitTimeActionFuc('3')
    print(struct_time)