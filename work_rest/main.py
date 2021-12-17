import time
from typing import Callable
from pynput import mouse, keyboard
from win10toast import ToastNotifier


class WorkClock:

    def __init__(self, notify_func: Callable, away_time: int=60, max_work_time: int=50 * 60):
        """init clock

        Args:
            notify_func(function): called when you must to relax;
            away_time (int):[unit:seconds] without operation time, used to calculate when you leave;
            max_work_time (int):[unit:seconds] notify to relax when you has worked this time;
        """
        self._worked_total = 0
        self._max_work_second = max_work_time
        self._last_work_time = time.time()
        self._notify_func = notify_func
        self._away_second = away_time
    
    def operate_once(self, *args, **kwargs):
        """record mouse or keyboard events
        """
        current_time = time.time()

        if current_time - self._last_work_time < self._away_second:
            self._worked_total += current_time - self._last_work_time
            print(f"当前工作时长{self._worked_total}")
            if self._worked_total >= self._max_work_second:
                self._notify_func()
                self._worked_total = 0
        
        # consider as relax time
        self._last_work_time = current_time


def notify_in_win():
    ToastNotifier().show_toast(title="休息提醒", msg="工作很久啦，休息下吧", duration=10, threaded=True)


def run():
    """
    Collect events until released
    """
    clock = WorkClock(notify_in_win, max_work_time=30 * 60)
    with mouse.Listener(on_click=clock.operate_once, on_move=clock.operate_once, on_scroll=clock.operate_once) as mouse_listener:
        with keyboard.Listener(on_press=clock.operate_once) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()


if __name__ == "__main__":
    run()
