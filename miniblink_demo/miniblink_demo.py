#!d:\cccc2020\TOOL\python-3.9.1-embed-win32\python.exe

from MBPython import miniblink


a=Tk()
a.state('zoom')#全屏
a.update()#更新窗口状态和信息

mbpython=miniblink.Miniblink
mb=mbpython.init(r'd:\cccc2020\CODE\workspace\miniblink\miniblink_demo\Debug\node.dll')#操作核心

wke=mbpython(mb)#得到wke控制权
window=wke.window#miniblink的界面容器

webview=window.wkeCreateWebWindow(2,a.winfo_id(),0,0,a.winfo_width(),
                                  a.winfo_height())#核心组件，大小与窗口尺寸一样
mb.wkeLoadURLW(webview,'http://www.baidu.com/')#载入百度网页
window.wkeShowWindow(webview)#显示组件
#下面这行代码在单独使用miniblink时用
#window.wkeRunMessageLoop()

a.mainloop()