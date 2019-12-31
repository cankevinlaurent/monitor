# -*- coding: utf-8 -*-

import os
import sys
import re
import sqlite3
import time
import codecs
import MySQLdb

###############################################################################


class MyExcept(Exception):
    '''
    My defined exception handler.

    '''

    def __init__(self, msg='Error: unknown.'):
        print msg

    def __del__(self):
        exit(0)

##############################################################################


class MysqlDB:
    '''
    handle mysql database

    '''

    conn = None
    cursor = None
    
    def __init__(self):
        self.conn = MySQLdb.connect(host='10.128.28.37', user='zipkin', passwd='zipkinp', db='zipkin', use_unicode=True, charset='utf8')
        #self.conn = MySQLdb.connect(host='localhost', user='root', passwd='root.SHM', db='zipkin', use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def clear_aic(self):
        self.cursor.execute('TRUNCATE TABLE active_internet_connection')

    def clear_ps(self):
        self.cursor.execute('TRUNCATE TABLE ps')

    def clear_memory(self):
        self.cursor.execute('TRUNCATE TABLE memory')

    def clear_hdisk(self):
        self.cursor.execute('TRUNCATE TABLE hdisk')

    def insert_aic_record(self, record):
        '''
        insert record to active_internet_connection
        user grantees the conn.commit()
        
        '''

        self.cursor.execute('INSERT INTO active_internet_connection(proto,recvq,sendq,localip,localport,foreignip,foreignport,state,pid,progname,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (
                record[0], #proto
                int(record[1]), #recvq
                int(record[2]), #sendq
                record[3], #localip
                int(record[4]), # localport
                record[5], #foreignip
                int(record[6]), #foreignport
                record[7], #state
                int(record[8]) if record[8] is not None else None, #pid
                record[9], #progname
                int(record[10]) #timestamp
            )
        )

    def insert_ps_record(self, record):
        '''
        insert record to ps
        user grantees the conn.commit()
        
        '''

        self.cursor.execute('INSERT INTO ps(localip,user,pid,cpu,mem,vsz,rss,tty,stat,start,time,command,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (
                record[0], #localip
                record[1], #user
                int(record[2]), #pid
                float(record[3]) if record[3] is not None else None, #cpu
                float(record[4]) if record[4] is not None else None, #mem
                int(record[5]) if record[5] is not None else None, #vsz
                int(record[6]) if record[6] is not None else None, #rss
                record[7], #tty
                record[8], #stat
                record[9], #start
                record[10], #time
                record[11], #command
                int(record[12]) #timestamp
            )
        )

    def insert_memory_record(self, record):
        '''
        insert record to memory
        user grantees the conn.commit()

        '''

        self.cursor.execute('INSERT INTO memory(ip,total,used,free,shared,buffers,cached,minus_buffers_cache_used,plus_buffers_cache_free,swap_total,swap_used,swap_free,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (
                record[0], #ip
                int(record[1]), #total
                int(record[2]), #used
                int(record[3]), #free
                int(record[4]), #shared
                int(record[5]), #buffers
                int(record[6]), #cached
                int(record[7]), #minus_buffers_cache_used
                int(record[8]), #plus_buffers_cache_free
                int(record[9]), #swap_total
                int(record[10]), #swap_used
                int(record[11]), #swap_free
                int(record[12]) #timestamp
            )
        )

    def insert_hdisk_record(self, record):
        '''
        insert record to hdisk
        user grantees the conn.commit()

        '''

        self.cursor.execute('INSERT INTO hdisk(ip,filesystem,type,blocks_byte,used,available,capacity,mounted_on,timestamp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
           (
                record[0], #ip
                record[1], #filesystem
                record[2], #type
                int(record[3]), #blocks_byte
                int(record[4]), #used
                int(record[5]), #available
                record[6], #capacity
                record[7], #mounted_on
                int(record[8]) #timestamp
            )
        )

##############################################################################


class SqliteDB:
    '''
    handle my database

    '''

    def __init__(self, database='monitor.db'):
        try:
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()
        except:
            raise MyExcept('Error: Initiate database.')

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass

    def clear_aic(self):
        try:
            self.cursor.execute('DELETE FROM active_internet_connection')
            self.cursor.execute('UPDATE sqlite_sequence SET seq = 0 where name = "active_internet_connection"')
        except:
            raise MyExcept('Error: clear table error.')
            
    def clear_ps(self):
        try:
            self.cursor.execute('DELETE FROM ps')
            self.cursor.execute('UPDATE sqlite_sequence SET seq = 0 where name = "ps"')
        except:
            raise MyExcept('Error: clear table error.')
            
    def clear_memory(self):
        try:
            self.cursor.execute('DELETE FROM memory')
            self.cursor.execute('UPDATE sqlite_sequence SET seq = 0 where name = "memory"')
        except:
            raise MyExcept('Error: clear table error.')

    def clear_hdisk(self):
        try:
            self.cursor.execute('DELETE FROM hdisk')
            self.cursor.execute('UPDATE sqlite_sequence SET seq = 0 where name = "hdisk"')
        except:
            raise MyExcept('Error: clear table error.')

    def insert_aic_record(self, record):
        '''
        insert record to active_internet_connection
        user grantees the conn.commit()
        
        '''

        self.cursor.execute('INSERT INTO active_internet_connection(proto,recvq,sendq,localip,localport,foreignip,foreignport,state,pid,progname,timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
            (
                record[0], #proto
                int(record[1]), #recvq
                int(record[2]), #sendq
                record[3], #localip
                int(record[4]), # localport
                record[5], #foreignip
                int(record[6]), #foreignport
                record[7], #state
                int(record[8]) if record[8] is not None else None, #pid
                record[9], #progname
                int(record[10]) #timestamp
            )
        )
    
    def insert_ps_record(self, record):
        '''
        insert record to ps
        user grantees the conn.commit()
        
        '''

        self.cursor.execute('INSERT INTO ps(localip,user,pid,cpu,mem,vsz,rss,tty,stat,start,time,command,timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (
                record[0], #localip
                record[1], #user
                int(record[2]), #pid
                float(record[3]) if record[3] is not None else None, #cpu
                float(record[4]) if record[4] is not None else None, #mem
                int(record[5]) if record[5] is not None else None, #vsz
                int(record[6]) if record[6] is not None else None, #rss
                record[7], #tty
                record[8], #stat
                record[9], #start
                record[10], #time
                record[11], #command
                int(record[12]) #timestamp
            )
        )
            
    def insert_memory_record(self, record):
        '''
        insert record to memory
        user grantees the conn.commit()

        '''

        self.cursor.execute('INSERT INTO memory(ip,total,used,free,shared,buffers,cached,minus_buffers_cache_used,plus_buffers_cache_free,swap_total,swap_used,swap_free,timestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (
                record[0], #ip
                int(record[1]), #total
                int(record[2]), #used
                int(record[3]), #free
                int(record[4]), #shared
                int(record[5]), #buffers
                int(record[6]), #cached
                int(record[7]), #minus_buffers_cache_used
                int(record[8]), #plus_buffers_cache_free
                int(record[9]), #swap_total
                int(record[10]), #swap_used
                int(record[11]), #swap_free
                int(record[12]) #timestamp
            )
        )

    def insert_hdisk_record(self, record):
        '''
        insert record to hdisk
        user grantees the conn.commit()

        '''

        self.cursor.execute('INSERT INTO hdisk(ip,filesystem,type,blocks_byte,used,available,capacity,mounted_on,timestamp) VALUES(?,?,?,?,?,?,?,?,?)',
            (
                record[0], #ip
                record[1], #filesystem
                record[2], #type
                int(record[3]), #blocks_byte
                int(record[4]), #used
                int(record[5]), #available
                record[6], #capacity
                record[7], #mounted_on
                int(record[8]) #timestamp
            )
        )

##############################################################################


class FileProcess:
    '''
    involved files

    '''

    def __init__(self):
        self.linux_aic = os.path.abspath('./monitor.log/linux/active_internet_connection.log')
        self.linux_ps = os.path.abspath('./monitor.log/linux/ps.log')
        self.linux_memory = os.path.abspath('./monitor.log/linux/memory.log')
        self.linux_hdisk = os.path.abspath('./monitor.log/linux/hdisk.log')
        
        self.hpunix_aic = os.path.abspath('./monitor.log/hpunix/active_internet_connection.log')
        self.hpunix_lsof = os.path.abspath('./monitor.log/hpunix/lsof.log')
        self.hpunix_ps = os.path.abspath('./monitor.log/hpunix/ps.log')
        self.hpunix_memory = os.path.abspath('./monitor.log/hpunix/memory.log')
        self.hpunix_hdisk = os.path.abspath('./monitor.log/hpunix/hdisk.log')
    
    def getfile(self, filename):
        try:
            fp = codecs.open(filename, 'r', 'utf-8')
            lines = []
            for line in fp.readlines():
                lines.append(line)
            return lines
        except:
            raise MyExcept('Error: read file.')
        finally:
            fp.close()

    def proc_linux_aic(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0]
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif 'tcp' not in line: continue
            elif '-' in line: continue
            elif '127.0.0.1' in line: continue
            else:
                line = re.sub('::ffff:', '', line)
                sublst = re.split('\s+|:|/', line, 9)
                sublst.append(timestamp)
                lst.append(sublst)
        return lst

    def proc_hpunix_aic(self, aic_lines, lsof_lines):
        lsof_lst = self.proc_hpunix_lsof(lsof_lines)
        lst = []
        if len(aic_lines) == 0: return lst
        timestamp = aic_lines[0].strip()
        for line in aic_lines:
            line = line.strip()
            if len(line) == 0: continue
            elif 'tcp' not in line: continue
            elif '*' in line: continue
            elif '::' in line: continue
            elif '127.0.0.1' in line: continue
            else:
                sublst = []
                linelst = line.split()
                sublst.append(linelst[0]) #proto
                sublst.append(linelst[1]) #recvq
                sublst.append(linelst[2]) #sendq
                siplst = linelst[3].split('.')
                sep = '.'
                sublst.append(sep.join(siplst[0:4])) #localip
                sublst.append(siplst[4]) #localport
                diplst = linelst[4].split('.')
                sublst.append(sep.join(diplst[0:4]))
                sublst.append(diplst[4])
                sublst.append(linelst[5])
                sublst.append(None)
                sublst.append(None)
                sublst.append(timestamp)
                for lt in lsof_lst:
                    if sublst[3] == lt[4] and sublst[4] == lt[5] and sublst[10] == lt[3]:
                        sublst[8] = lt[1]
                        sublst[9] = lt[2]
                lst.append(sublst)
        return lst

    def proc_hpunix_lsof(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0].strip()
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif 'TCP' not in line: continue
            elif '*:' in line: continue
            elif '127.0.0.1' in line: continue
            else:
                line = re.sub('IPv4', timestamp, line) #insert timestamp
                sublst = []
                linelst = line.split()
                sublst.extend(linelst[0:3]) #command pid user
                sublst.append(linelst[4]) #timestamp
                localip = linelst[8].split(':')[0]
                localport = linelst[8].split(':')[1].split('->')[0]
                sublst.append(localip) #localip
                sublst.append(localport) #localport
                lst.append(sublst)
        return lst

    def proc_linux_ps(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0]
        lines[0] = ''
        current_ip = None
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif '| UNREACHABLE!' in line: continue
            elif '"changed":' in line: continue
            elif '"msg":' in line: continue
            elif '"unreachable":' in line: continue
            elif '| SUCCESS |' in line:
                current_ip = line.split(' | ')[0]
                continue
            elif not re.search(r'\d', line): continue
            else:
                sublst = []
                sublst.append(current_ip)
                sublst.extend(re.split('\s+', line, 10))
                sublst.append(timestamp)
                lst.append(sublst)
        return lst

    def proc_hpunix_ps(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0]
        lines[0] = ''
        current_ip = None
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif '| UNREACHABLE!' in line or '"changed":' in line or '"msg":' in line or '"unreachable":' in line: continue
            elif not re.search(r'\d', line): continue
            elif '| SUCCESS |' in line:
                current_ip = line.split(' | ')[0]
                continue
            else:
                sublst = []
                sublst.append(current_ip)
                linelst = re.split('\s+', line, 8)
                sublst.append(linelst[0]) #user
                sublst.append(linelst[1]) # pid
                sublst.append(None) #cpu
                sublst.append(None) #mem
                sublst.append(None) #vsz
                sublst.append(None) #rss
                if ':' in linelst[4]:
                    sublst.append(linelst[5]) #tty
                    sublst.append(None) #stat
                    sublst.append(linelst[4]) #start
                    sublst.append(linelst[6]) #time
                    sublst.append(linelst[7]) #command
                else:
                    sep = ''
                    sublst.append(linelst[6]) #tty
                    sublst.append(None) #stat
                    sublst.append(sep.join(linelst[4:6])) #start
                    sublst.append(linelst[7]) #time
                    sublst.append(linelst[8]) #command
                sublst.append(timestamp)
                lst.append(sublst)
        return lst

    def proc_linux_memory(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0]
        sublst = []
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif '| UNREACHABLE!' in line or '"changed":' in line or '"msg":' in line or '"unreachable":' in line: continue
            elif '| SUCCESS |' in line:
                current_ip = line.split(' | ')[0]
                continue
            elif 'Mem:' in line:
                sublst.append(current_ip)
                line = re.sub('Mem:', '', line)
                sublst.extend(line.split())
                continue
            elif '-/+ buffers/cache:' in line:
                line = line.replace('-/+ buffers/cache:', '')
                sublst.extend(line.split())
            elif 'Swap:' in line:
                line = re.sub('Swap:', '', line)
                sublst.extend(line.split())
                sublst.append(timestamp)
                lst.append(sublst)
                sublst = []
            else: continue
        return lst

    def proc_linux_hdisk(self, lines):
        lst = []
        if len(lines) == 0: return lst
        timestamp = lines[0]
        lines[0] = 'Filesystem'
        current_ip = None
        for line in lines:
            line = line.strip()
            if len(line) == 0: continue
            elif '| UNREACHABLE!' in line or '"changed":' in line or '"msg":' in line or '"unreachable":' in line: continue
            elif line == '}': continue
            elif '| SUCCESS |' in line:
                current_ip = line.split(' | ')[0]
                continue
            elif 'Filesystem' in line: continue
            else:
                sublst = []
                sublst.append(current_ip)
                sublst.extend(line.split())
                sublst.append(timestamp)
                lst.append(sublst)
        return lst

##############################################################################


if __name__ == '__main__':

    IS_MYSQL_USED = True
    IS_DATABASE_NEED_TOBE_CLEARED = False
    IS_STDOUT_SHOW = False
    IS_RESTORE = True

    if IS_MYSQL_USED: mydb = MysqlDB() #connect to mysql
    else: mydb = SqliteDB() #connect to sqlite

    fileprocess = FileProcess()
    
    #linux_aic
    lst = fileprocess.proc_linux_aic(
        fileprocess.getfile(fileprocess.linux_aic))
    if IS_DATABASE_NEED_TOBE_CLEARED: mydb.clear_aic()
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_aic_record(record)
    if IS_RESTORE: mydb.conn.commit()
    print 'Netstat [linux] restored.'

    #hpunix_aic
    lst = fileprocess.proc_hpunix_aic(
        fileprocess.getfile(fileprocess.hpunix_aic),
        fileprocess.getfile(fileprocess.hpunix_lsof))
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_aic_record(record)
    if IS_RESTORE: mydb.conn.commit()
    print 'Netstat [hpunix] restored.'

    #linux_ps
    lst = fileprocess.proc_linux_ps(
        fileprocess.getfile(fileprocess.linux_ps))
    if IS_DATABASE_NEED_TOBE_CLEARED: mydb.clear_ps()
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_ps_record(record)
    print 'Ps [linux] restored.'

    #hpunix_ps
    lst = fileprocess.proc_hpunix_ps(
        fileprocess.getfile(fileprocess.hpunix_ps))
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_ps_record(record)
    if IS_RESTORE: mydb.conn.commit()
    print 'Ps [hpunix] restored.'

    #linux_memory
    lst = fileprocess.proc_linux_memory(
        fileprocess.getfile(fileprocess.linux_memory))
    if IS_DATABASE_NEED_TOBE_CLEARED: mydb.clear_memory()
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_memory_record(record)
    if IS_RESTORE: mydb.conn.commit()
    print 'Memory [linux] restored.'

    #linux_hdisk
    lst = fileprocess.proc_linux_hdisk(
        fileprocess.getfile(fileprocess.linux_hdisk))
    if IS_DATABASE_NEED_TOBE_CLEARED: mydb.clear_hdisk()
    for record in lst:
        if IS_STDOUT_SHOW: print record
        if IS_RESTORE: mydb.insert_hdisk_record(record)
    if IS_RESTORE: mydb.conn.commit()
    print 'Hdisk [linux] restored.'
