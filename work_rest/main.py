from pynput import mouse, keyboard

# work_time已经工作
# 定时提醒
# 1分钟不操作，停止计时

def update_work_status(*args, **kwargs):
    print(args, kwargs)


class WorkClock:

    def __init__(self, away_time: int, max_work_time: int):
        """init clock

        Args:
            away_time (int):[unit:seconds] without operation time, used to calculate when you leave;
            max_work_time (int):[unit:minutes] notify to relax when you has worked this time;
        """
    
    def operate_once(self):
        pass

    def without_operate(self):
        pass


def run():
    """
    Collect events until released
    """
    with mouse.Listener(on_click=update_work_status, on_move=update_work_status, on_scroll=update_work_status) as mouse_listener:
        with keyboard.Listener(on_press=update_work_status) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()


if __name__ == "__main__":
    run()
