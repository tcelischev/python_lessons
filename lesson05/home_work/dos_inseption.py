'''
2018.09.22 def deletedir done. Tselischev
2018.09.21 def createdir done. Tselischev
2018.09.20 Created. Tselischev
'''

import os
import datetime

now = str(datetime.datetime.now())
createnewdir_log = ['[dirName, creationDate, errStatus, textMessage]']

def createnewdir(maxqntdir=1):
    '''
    Create new subdirrectory 'dir_xx' at current dirrectory. If exist - add count. Default = 1.
    :param maxqntdir: max quantity of subdirrectories
    :return: List of new subdirrectory or error msg
    '''
    global createnewdir_log
    dir_prefix = 'dir_'
    numd = 1 # номер проверяемой дирректории
    count = 0 # счетчик успешно созданных
    maxqntdir += 1
    for i in range(1, maxqntdir):
        suffix = str(numd).zfill(2)
        dir_name = dir_prefix + suffix
        try:
            if not os.path.exists(dir_name) and numd <= maxqntdir:
                suffix = str(numd).zfill(2)
                dir_name = dir_prefix + suffix  # пробовал через join - получаю 0dir_1 вместо dir_01 ?
                os.mkdir(dir_name)
                numd += 1
                count += 1
                createnewdir_log.append('[{}, {}, 0, Dirrectory successfully created. New dir created {}]'.format(dir_name, now, count))
            elif os.path.exists(dir_name):
                numd += 1
                # suffix = str(numd).zfill(2)
                # dir_name = dir_prefix + suffix
                createnewdir_log.append('[{}, {}, 1, Dirrectory already exists.]'.format(dir_name, now))
            elif numd > maxqntdir:
                createnewdir_log.append('["", {}, 2, Out of max quantity of dirrectories {}.'.format(maxqntdir, now))
                break
        except OSError as err:
            createnewdir_log.append('["", "", 3, ' + err + ']')
    return createnewdir_log

[print(line) for line in createnewdir(3)]

# >>>>>>>>>>>-DELETE_function-<<<<<<<<<<<<<<
def deletedir(start_dir_num = 1, end_dir_num = 1):
    '''
    DELETE subdirrectories like 'dir_xx' at current dirrectory  by range. If delete successful - add count.
    :param start_dir_num: start subdirrectory
    :param end_dir_num: end subdirrectory
    :return: List of deleted subdirrectory or error msg
    '''
    dir_prefix = 'dir_'
    numd = start_dir_num # номер проверяемой дирректории
    count = 0 # счетчик
    end_dir_num += 1
    deleted_dir_log = ['[dirName, delstatus, deletionDate, textMessage]']
    for i in range(start_dir_num, end_dir_num):
        suffix = str(numd).zfill(2)
        dir_name = dir_prefix + suffix
        try:
            if os.path.exists(dir_name) and numd <= end_dir_num:
                suffix = str(numd).zfill(2)
                dir_name = dir_prefix + suffix
                os.rmdir(dir_name)
                numd += 1
                count += 1
                deleted_dir_log.append('[{}, 0, {}, Dirrectory successfully Deleted.]'.format(dir_name, now))
            elif not os.path.exists(dir_name):
                numd += 1
                deleted_dir_log.append('[{}, 1, {}, Dirrectory doesn\'t  exists.]'.format(dir_name, now))
            elif numd > maxqntdir:
                deleted_dir_log.append('["", 2, {}, Out of max quantity of dirrectories {}.'.format(end_dir_num, now))
                break
        except OSError as err:
            deleted_dir_log.append('["", 3, {}, ', err, ']')
    return deleted_dir_log

[print(line) for line in deletedir(2, 4)]

input('press enter to quit')






### [print(line, end = '\n') for line in createnewdir(13)]

# TODO function for dirrectory listing

# TODO make current file copy into current dir
