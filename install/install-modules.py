import sys
import os
import glob
import shutil
import subprocess
import pkg_resources
import sys
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_module_installed(module_name):
    """모듈이 설치되어 있는지 확인"""
    try:
        pkg_resources.get_distribution(module_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def install_module(module_name):
    """모듈 설치"""
    try:
        logger.info(f"{module_name} 설치 중...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        logger.info(f"{module_name} 설치 완료")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"{module_name} 설치 실패: {e}")
        return False


# 설치할 모듈 리스트
modules = [
    "natsort",
    "pillow",
    "pdf2image",
    "PyPDF2",
    "selenium",
    "webdriver_manager",
    "requests",
    "pandas",    
    "numpy",
    "openpyxl",
    "matplotlib",
    "pyautogui",
    "bs4",
    "pywin32"
]

# 각 모듈 설치 확인 및 설치
for module in modules:
    if is_module_installed(module):
        logger.info(f"{module} 이미 설치됨")
    else:
        success = install_module(module)
        if not success:
            logger.warning(f"{module} 설치 실패로 인해 프로그램이 계속 진행됩니다")

# WIN32 모듈 관련 dll 복사
py_ins_folder = os.path.dirname(sys.executable).replace("\\", "/")
py_ins_pywin32_folder = py_ins_folder + "/Lib/site-packages/pywin32_system32" 

py_ins_win32_folder = py_ins_folder + "/Lib/site-packages/win32"
py_ins_win32_lib_folder = py_ins_folder + "/Lib/site-packages/win32/lib"

dll_files = glob.glob(py_ins_pywin32_folder + "/*.dll")

for file in dll_files:
    #os.chmod(file, 0o777)
    shutil.copy2(file, py_ins_win32_folder)
    shutil.copy2(file, py_ins_win32_lib_folder)
