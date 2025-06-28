from StaticClass import BaseMethods as bs

import functools
import datetime
import os

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        dateNow = datetime.datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(bs.getLogPath(), f"log-{dateNow}.log")
        if not os.path.exists(bs.getLogPath()):
            os.makedirs(bs.getLogPath())

        try:
            result = func(*args, **kwargs)
            with open(log_file, "a", encoding="utf-8") as f:

                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if args:
                    cls_name = type(args[0]).__name__
                else:
                    cls_name = "NieznanaKlasa"

                f.write(f"[{now}] Wywołano: {cls_name} {func.__name__} | wynik: {result}\n")

            return result
        except Exception as e:
            with open(log_file, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if args:
                    cls_name = type(args[0]).__name__
                else:
                    cls_name = "NieznanaKlasa"

                f.write(f"[{now}] Błąd w funkcji: {cls_name} {func.__name__} | wyjątek: {e}\n")

            return e
    return wrapper