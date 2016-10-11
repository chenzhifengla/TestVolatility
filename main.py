# -*- coding: utf-8 -*-

import logging
from volatility import execute
import threading

def initLogger():
    """
    # 配置logging，用于全局日志记录
    :return:
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[func:%(funcName)s() line:%(lineno)d] %(threadName)s-%(levelname)s: %(message)s',
                        datefmt='%Y/%m/%d %X',)
    logger = logging.getLogger()

def start():
    profiles = ["WinXPSP3x86", "LinuxCentOS65x64"]
    paths = [["-f /lab/winxp.raw", "-l vmi://winxp"], ["-f /lab/CentOS.raw", "-l vmi://centos6.5"]]
    #commands = [["pslist", "sockscan", "devicetree", "ssdt"], ["linux_pslist", "linux_netstat", "linux_check_tty", "linux_check_syscall"]]
    commands = [["pslist", "sockscan", "ssdt"], ["linux_pslist", "linux_netstat", "linux_check_tty",]]


    # threads = []
    # for i, profile in enumerate(profiles):
    #     for path in paths[i]:
    #         for command in commands[i]:
    #             thread = threading.Thread(target=execute, args=(profile, path, command))
    #             #self.threadsVm[vmname] = threading.Thread(target=self.generateSingleController, args=(vmname,), name="Thread-" + str(vmname))
    #             #execute(profile, path, command)
    #             thread.setDaemon(True)
    #             thread.start()
    #             threads.append(thread)
    # for thread in threads:
    #     thread.join()

    profiles = ["WinXPSP3x86", "LinuxCentOS65x64"]
    paths = [["-f /lab/winxp.raw", "-f /lab/CentOS.raw"], ["-l vmi://winxp", "-l vmi://centos6.5"]]
    commands = [["pslist", "sockscan", "devicetree", "ssdt"], ["linux_pslist", "linux_netstat", "linux_check_tty", "linux_check_syscall"]]

    for path in paths:
        for i, p in enumerate(path):
            for command in commands[i]:
                execute(profiles[i], p, command)

    # for i, profile in enumerate(profiles):
    #     for path in paths[i]:
    #         for command in commands[i]:
    #             execute(profile, path, command)

if __name__ == "__main__":

    initLogger()
    start()