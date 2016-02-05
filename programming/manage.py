#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings.dev")
    ##환경변수를 사전형태로 가지고있다. -> 우리가 지정안하면 이 주소가 쓰인다.
    ## settings.dev or prod -> 개발할때는 settings를 개발용으로 둔다.
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
