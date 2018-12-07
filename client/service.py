# install pywin32 -> https://pypi.org/project/pywin32/
# agar service bisa start maka harus ditambahkan path ini di environment variable
# C:\Python27\Lib\site-packages\pywin32_system32

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
from ais_sender import telnet_TCP
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s %(threadName)s] %(message)s',
                    datefmt='%H:%M:%S')

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "AisSender"
    _svc_display_name_ = "Ais Sender Python"
    _svc_request_ = True

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        logging.info('Stopping service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        logging.info(' ** Start Services ** ')
        while(True) :
        	if self.stop_requested:
        		break
        	telnet_TCP()
        logging.info(' ** Close Services ** ')


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)