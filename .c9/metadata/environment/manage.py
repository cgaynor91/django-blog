{"filter":false,"title":"manage.py","tooltip":"/manage.py","undoManager":{"mark":0,"position":-1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":0},"action":"remove","lines":["#!/usr/bin/env python","import os","import sys","","if __name__ == \"__main__\":","    os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")","    try:","        from django.core.management import execute_from_command_line","    except ImportError:","        # The above import may fail for some other reason. Ensure that the","        # issue is really that Django is missing to avoid masking other","        # exceptions on Python 2.","        try:","            import django","        except ImportError:","            raise ImportError(","                \"Couldn't import Django. Are you sure it's installed and \"","                \"available on your PYTHONPATH environment variable? Did you \"","                \"forget to activate a virtual environment?\"","            )","        raise","    execute_from_command_line(sys.argv)",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":20,"column":39},"action":"insert","lines":["import os","import sys","","if __name__ == \"__main__\":","    os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")","    try:","        from django.core.management import execute_from_command_line","    except ImportError:","        # The above import may fail for some other reason. Ensure that the","        # issue is really that Django is missing to avoid masking other","        # exceptions on Python 2.","        try:","            import django","        except ImportError:","            raise ImportError(","                \"Couldn't import Django. Are you sure it's installed and \"","                \"available on your PYTHONPATH environment variable? Did you \"","                \"forget to activate a virtual environment?\"","            )","        raise","    execute_from_command_line(sys.argv)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":27},"end":{"row":5,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":46,"mode":"ace/mode/python"}},"timestamp":1583259649058,"hash":"061598ccdf948a3d248fc3bb7a078dae02cec539"}