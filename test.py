import os
import sys
import io  # 問題点1:1行に複数のインポート 問題点2:ioをインポートしているが未使用


def greetingPath(msg, name):  # 命名規則にエラー。後述のオプションで説明
    print(sys.argv)
    path = os.get_exec_path()  # 問題点3:path変数が未使用
    print(f"{msg}, {name}")