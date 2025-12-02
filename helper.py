from datetime import datetime


class Helper:

    @staticmethod
    def formated_time(time_str_24):
        time_obj = datetime.strptime(time_str_24, "%H:%M")
        hour_12 = int(time_obj.strftime("%I"))
        minute = time_obj.strftime("%M")
        am_pm = time_obj.strftime("%p")
        time_12 = f"{hour_12}:{minute} {am_pm}"

        return time_12

