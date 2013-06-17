'class of Utils for device connection'
'-------------------------------------'
try:
    for p in os.environ['PYTHONPATH'].split(';'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass
from com.dtmilano.android.viewclient import ViewClient, View
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

class UtilTool:
    @staticmethod
    def connectToDevice():
        print 'starting...'
        d = MonkeyRunner.waitForConnection(10)
        if not d:
            raise Exception("device not found")
        else:
            pass
        return d

    @staticmethod
    def init(device):
        print 'init the test environment..ing.'
        #get Device connection
        #device = UtilTool.connectToDevice()
        #lanuch Contacts app
        device.startActivity(component='com.android.contacts/.activities.PeopleActivity')
        MonkeyRunner.sleep(15)
        #print device
        #get a ViewClient instance
        vc = ViewClient(device,'emulator-5554')
        MonkeyRunner.sleep(10)
        #get Window content of current page
        vc.dump()
        MonkeyRunner.sleep(5)
        return vc
        
