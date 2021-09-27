"""
BOJ 문제 목록에 따라 소스 코드와 입출력 텍스트를 만듦.

사용법
1. 문제 목록 페이지에서 문제들 정보를 Ctrl + C 한 후, 
2. problem_info.txt에 Ctrl + V.
"""

import os
from pathlib import Path
from datetime import date


# input.txt를 읽어오기 위해 소스 첫 부분에 써주는 코드
input_snippet = '''\
from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline'''


# 오늘 날짜에 맞는 폴더를 만듦
def makeDirectoryForToday():
    # 오늘 날짜
    today = date.today()
    dir_name = f"{today.month:02}{today.day:02}"

    # 새로운 폴더의 경로
    problem_set_dir = f"{Path(__file__).parent}\{dir_name}"

    # 폴더가 이미 있으면 오류, 없으면 새로 만들기
    try: 
        if not os.path.exists(problem_set_dir):
            os.makedirs(problem_set_dir)
    except OSError as e:
        print(e)

    # 새로운 폴더 경로 반환
    return problem_set_dir


def createProblemSet(problem_file):
    text_dir = Path(__file__).parent
    target_dir = makeDirectoryForToday()

    text = open(f"{text_dir}\{problem_file}", "rt", encoding='UTF8')
    for line in text:
        info = line.split('\t')
        problem_num = info[0].strip()
        problem_name = info[1].strip().replace('/', '')

        # python 파일 생성
        file_name = problem_num + '. ' + problem_name
        f = open(f"{target_dir}\{file_name}.py", "w", encoding="UTF8")
        
        # 파일 처음에 input 읽어오는 문구 작성
        f.write(input_snippet)
        f.close()

        # input txt 생성
        f = open(f"{target_dir}\{file_name} input.txt", "w", encoding="UTF8")
        f.close()

        # output txt 생성
        # f = open(f"{target_dir}\{file_name} output.txt", "w", encoding="UTF8")
        # f.close()

    text.close()


if __name__ == "__main__":
    createProblemSet("problem_info.txt")