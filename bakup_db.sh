#!/bin/bash

echo Starting backup process...
echo

_now=`date +%m-%d-%Y`
_cur_dir=$(pwd)

echo current date: $_now

db_name=${1:-db.sqlite3}
backup_dir=${2:-backup}

if [ "$db_name" == db.sqlite3 ]; then
	echo DB name not defined, using default: $db_name
else
	echo DB name found, using: $db_name
	if [ ! -a $db_name ]; then
		echo File does not exist, quitting...

	else
		echo File found, proceeding...
	fi
fi

db_backup_name=backup_$db_name\_$_now.sqlite3

echo

if [ ! -d "$backup_dir" ]; then
	echo Backup directory not found, creating folder...
	mkdir ../backup
else
	echo Backup directory found, proceeding...
fi

echo

echo "Copying $db_name in $backup_dir/$db_backup_name"

if cp $db_name ../$backup_dir/$db_backup_name
then
	echo $db_name successfully backed up as $db_backup_name
	echo
	echo Backup completed
else
	echo "Backup Failed, exit status $?"
	exit 1
fi

echo
