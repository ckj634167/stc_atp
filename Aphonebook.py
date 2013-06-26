'Phonebook Test Case'
'-------------------------------------'
#Define a class of contact



import sys
import os

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(';'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass

from com.dtmilano.android.viewclient import ViewClient, View
from com.dtmilano.android.Utils import UtilTool
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

class Contact:
    package='com.android.contacts'
    activity='.activities.PeopleActivity'
    but_create_new_contact=''
    
    #comp = package + '/' + activity
    def addContact(self,Ncontacts):
        #get Device connection
        #device = UtilTool.connectToDevice()
        #lanuch Contacts app
        #device.startActivity(component='com.android.contacts/.activities.PeopleActivity')
        #MonkeyRunner.sleep(15)
        #print device
        #get a ViewClient instance
        #vc = ViewClient(device,'emulator-5554')
        #MonkeyRunner.sleep(10)
        #get Window content of current page
        #vc.dump()
        #MonkeyRunner.sleep(5)
        #print vc
        
        #get device connection
        device = UtilTool.connectToDevice()
        #init the testing environment
        vc = UtilTool.init(device)
        print 'test environment is ready'
        #get button named as Create a new contact
        for i in range(0,Ncontacts):
            if not vc.findViewWithText('Create a new contact'):
                vc.dump()
                print 'hey_if'
                MonkeyRunner.sleep(10)
                tv_add_contact = vc.findViewWithContentDescription('Add Contact')
                tv_add_contact.touch()
                MonkeyRunner.sleep(15)
                vc.dump()
                name = vc.findViewWithText('Name')
                name.type('Contact00'+str(i))
                vc.findViewWithText('Done').touch()
                MonkeyRunner.sleep(10)
                device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(15)
            else:
                print 'hey_else'
                vc.dump()
                MonkeyRunner.sleep(10)
                but_create_new_contact = vc.findViewWithTextOrRaise('Create a new contact')
                but_create_new_contact.touch()
                MonkeyRunner.sleep(20)
                vc.dump()
                name = vc.findViewWithText('Name')
                name.type('Contact00'+str(i))
                vc.findViewWithText('Done').touch()
                MonkeyRunner.sleep(10)
                device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(15)
                
        #get current view and check the result
        MonkeyRunner.sleep(15)
        vc.dump()
        contacts_number = vc.findViewWithText(str(Ncontacts)+' contacts')
        print contacts_number
        text = contacts_number.getText()
        if text==str(Ncontacts)+' contacts':
            print 'passed'
        else:
            print 'failed'
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        
    def deleteContact(self):
        #get Device connection
        #device = UtilTool.connectToDevice()
        #lanuch Contacts app
        #device.startActivity(component='com.android.contacts/.activities.PeopleActivity')
        #MonkeyRunner.sleep(15)
        #vc = ViewClient(device,'emulator-5554')
        #get device connection
        device = UtilTool.connectToDevice()
        #init the testing environment
        vc = UtilTool.init(device)
        print 'test environment is ready'
        print 'Starting to delete contact one by one'
        for i in range(0,2):
            MonkeyRunner.sleep(15)
            vc.dump()
            c = vc.findViewWithText('Contact00'+str(i))
            c.touch()
            MonkeyRunner.sleep(2)
            device.press('KEYCODE_DEL',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(15)
            vc.dump()
            but_confirm = vc.findViewWithText('OK')
            but_confirm.touch()
            MonkeyRunner.sleep(10)
            print 'Contact00'+str(i)+'is being deleted'
        MonkeyRunner.sleep(10)
        vc.dump()
        contacts_number = vc.findViewWithText('No contacts.')
        text = contacts_number.getText()
        if text=='No contacts.':
            print 'passed'
        else:
            print 'failed'
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    def editContact(self):
        pass


    
