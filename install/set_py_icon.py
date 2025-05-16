import winreg
import os
import sys

def set_python_icon(icon_path):
    try:
        # 아이콘 파일 존재 여부 확인
        if not os.path.exists(icon_path):
            raise FileNotFoundError(f"아이콘 파일을 찾을 수 없습니다: {icon_path}")

        # 레지스트리 경로
        key_path = r"Software\Classes\Python.File\DefaultIcon"

        # Python.File의 DefaultIcon 항목 설정
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'"{icon_path}",0')

        print(f"아이콘 설정이 완료되었습니다. .py 파일은 이제 {icon_path} 아이콘을 사용합니다.")

    except FileNotFoundError as e:
        print(f"오류: {e}")
    except PermissionError:
        print("오류: 이 작업을 수행하려면 관리자 권한이 필요합니다. 스크립트를 관리자 모드로 실행하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    # 사용자 지정 아이콘 경로 (필요에 따라 수정하세요)
    icon_path = r"C:\RapsoDi\python-3d.ico"  # py-icon.ico의 실제 경로로 변경
    set_python_icon(icon_path)
