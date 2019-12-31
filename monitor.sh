#!/bin/sh

function netstat_linux()
{
    #deal with linux netstat
    echo 'Detecting [linux] netstat ...'
    date +%s > ./monitor.log/linux/active_internet_connection.log
    echo -e '\r\n' >> ./monitor.log/linux/active_internet_connection.log 
    ansible linux -m command -a 'netstat -ntp' >> ./monitor.log/linux/active_internet_connection.log
    echo 'Detecting [linux] netstat done.'
}

function ps_linux()
{
    #deal with linux ps
    echo 'Detecting [linux] ps ...'
    date +%s > ./monitor.log/linux/ps.log
    echo -e '\r\n' >> ./monitor.log/linux/ps.log
    ansible linux -m command -a 'ps -aux' >> ./monitor.log/linux/ps.log
    echo 'Detecting [linux] ps done.'
}

function memory_linux()
{
    #deal with linux memory
    echo 'Detecting [linux] memory ...'
    date +%s > ./monitor.log/linux/memory.log
    echo -e '\r\n' >> ./monitor.log/linux/memory.log
    ansible linux -m command -a 'free -m' >> ./monitor.log/linux/memory.log
    echo 'Detecting [linux] memory done.'
}

function hdisk_linux()
{
    #deal with linux hdisk
    echo 'Detecting [linux] hdisk ...'
    date +%s > ./monitor.log/linux/hdisk.log
    echo -e '\r\n' >> ./monitor.log/linux/hdisk.log
    ansible linux -m command -a 'df -PT -B 1' >> ./monitor.log/linux/hdisk.log
    echo 'Detecting [linux] hdisk done.'
}

function netstat_hpunix()
{
    #deal with hpunix netstat
    echo 'Detecting [hpunix] netstat ...'
    date +%s > ./monitor.log/hpunix/active_internet_connection.log
    echo -e '\r\n' >> ./monitor.log/hpunix/active_internet_connection.log
    cat ./monitor.log/hpunix/active_internet_connection.log > ./monitor.log/hpunix/lsof.log
    ansible hpunix -m command -a 'netstat -an' >> ./monitor.log/hpunix/active_internet_connection.log
    ansible hpunix -m command -a '/usr/local/bin/sudo /usr/local/bin/lsof -i -n -P' >> ./monitor.log/hpunix/lsof.log
    echo 'Detecting [hpunix] netstat done.'
}

function ps_hpunix()
{
    #deal with hpunix ps
    echo 'Detecting [hpunix] ps ...'
    date +%s > ./monitor.log/hpunix/ps.log
    echo -e '\r\n' >> ./monitor.log/hpunix/ps.log
    ansible hpunix -m command -a 'ps -ef' >> ./monitor.log/hpunix/ps.log
    echo 'Detecting [hpunix] ps done.'
}

function memory_hpunix()
{
    #deal with hpunix memory
    echo 'Detecting [hpunix] memory ...'
    date +%s > ./monitor.log/hpunix/memory.log
    echo -e '\r\n' >> ./monitor.log/hpunix/memory.log
    ansible hpunix -m command -a 'free -m' >> ./monitor.log/hpunix/memory.log
    echo 'Detecting [hpunix] memory done.'
}

function hdisk_hpunix()
{
    #deal with hpunix hdisk
    echo 'Detecting [hpunix] hdisk ...'
    date +%s > ./monitor.log/hpunix/hdisk.log
    echo -e '\r\n' >> ./monitor.log/hpunix/hdisk.log
    ansible hpunix -m command -a 'bdf' >> ./monitor.log/hpunix/hdisk.log
    echo 'Detecting [hpunix] hdisk done.'
}

clear
while true
do

netstat_linux &
ps_linux &
#netstat_hpunix &
#ps_hpunix &
memory_linux &
hdisk_linux &
#memory_hpunix &
#hdisk_hpunix &


wait
python monitor.py

sleep 210s
done
