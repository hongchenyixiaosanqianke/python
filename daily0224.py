import os
import time
class A:
    def qidong(self):
        sum = 0
        for i in range(3):
            aaa = os.popen('adb shell am start -W com.kongfz.app/com.kongfz.app.home.mvvm.homepage.HomeActivity')
            print(aaa)
            for t in aaa:
                if 'Total' in t:
                    a = t.strip().split(':')[1]
                    print(a)
                    sum += int(a)
                else:
                    if 'Wait' in t:
                        a = t.strip().split(':')[1]
                        print(a)
                        sum += int(a)
            time.sleep(5)
            os.popen('adb shell am force-stop com.kongfz.app')

            time.sleep(5)
        print("平均冷启时间：",sum/3)
a = A()
a.qidong()
