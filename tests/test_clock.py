import time
from unittest.mock import MagicMock
from work_rest.main import WorkClock


def test_alawys_working():
    notify_func = MagicMock()
    clock = WorkClock(notify_func, away_time=10, max_work_time=1)
    clock.operate_once()
    time.sleep(1)
    clock.operate_once()
    notify_func.assert_called_once()


def test_with_relax():
    notify_func = MagicMock()
    clock = WorkClock(notify_func, away_time=0.5, max_work_time=1)
    time.sleep(1)
    clock.operate_once()
    notify_func.assert_not_called()
    time.sleep(0.4)
    clock.operate_once()
    time.sleep(0.4)
    clock.operate_once()
    time.sleep(0.2)
    clock.operate_once()
    notify_func.assert_called_once()

def test_alawys_working_notify_once():
    notify_func = MagicMock()
    clock = WorkClock(notify_func, away_time=10, max_work_time=1)
    clock.operate_once()
    time.sleep(1)
    clock.operate_once()
    clock.operate_once()
    notify_func.assert_called_once()
