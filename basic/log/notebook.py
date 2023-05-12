from IPython import get_ipython


def is_jupyter_notebook():
    print(get_ipython())
    return "ZMQInteractiveShell" in str(get_ipython())
