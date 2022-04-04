import os
import config


def make_dirs() -> None:
    os.makedirs(os.path.join(config.BASEDIR, 'users_data', 'cookies'), exist_ok=True)

    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'marks'), exist_ok=True)

    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'discipline_sources'), exist_ok=True)

    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'homeworks'), exist_ok=True)

    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'news'), exist_ok=True)

    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'requests', 'questionnaire'), exist_ok=True)
    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'requests', 'doc'), exist_ok=True)
    os.makedirs(os.path.join(config.PATH_TO_STUDENTS_TRACKING_DATA, 'requests', 'reference'), exist_ok=True)
