import winreg
import os
import sys

def set_python_idle_association():
    try:
        # Python 설치 경로에서 idle.bat 경로 찾기
        python_path = sys.executable
        idle_bat_path = os.path.join(os.path.dirname(python_path), "Lib", "idlelib", "idle.bat")
        
        if not os.path.exists(idle_bat_path):
            raise FileNotFoundError(f"idle.bat 파일을 찾을 수 없습니다: {idle_bat_path}")

        # 레지스트리 경로
        key_path = r"Software\Classes\.py"
        shell_key_path = r"Software\Classes\Python.File\shell\open\command"

        # .py 확장자 연결 설정
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Python.File")

        # idle.bat로 실행 명령 설정
        command = f'"{idle_bat_path}" "%1" %*'
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, shell_key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)

        print("설정이 완료되었습니다. 이제 .py 파일을 더블클릭하면 IDLE로 열립니다.")
        
    except FileNotFoundError as e:
        print(f"오류: {e}")
    except PermissionError:
        print("오류: 이 작업을 수행하려면 관리자 권한이 필요합니다. 스크립트를 관리자 모드로 실행하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    set_python_idle_association()