import lldb
## 调试用第一个import FB开源的 正式用第二个是字节内部的
# import chisel.fbchisellldbbase as fb
import fblldbbase as fb
# 调用当前对象的埋点debug信息

def lldbcommands():
    return [PrintTrackerInfo()]


class PrintTrackerInfo(fb.FBCommand):
    def name(self):
        return "pft"

    def description(self):
        return "Print Tracker Node List Debug Info"

    def args(self):
        return [
            fb.FBCommandArgument(arg='object', type='NSObject *', help='print object tracker debug info')
        ]

    def run(self, arguments, option):
        someObject = fb.evaluateInputExpression(arguments[0])
        lldb.debugger.HandleCommand('po [((NSObject *)%s) fh_printTrackerNodeListShowEmptyTrackerNode:NO]' % someObject)


