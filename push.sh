#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 COMMIT_MESSAGE"
    exit 1
fi

function log_info
{
    msg="$1"
    echo -e "\033[32m[`date '+%Y-%m-%d %H:%M:%S'`] [INFO] ${msg}\033[0m"
}

function log_warn
{
    msg="$1"
    echo -e "\033[33m[`date '+%Y-%m-%d %H:%M:%S'`] [WARN] ${msg}\033[0m"
}

function log_error
{
    msg="$1"
    echo -e "\033[31m[`date '+%Y-%m-%d %H:%M:%S'`] [ERROR] ${msg}\033[0m"
}

curr_dir=`dirname $0`
cd ${curr_dir}

git add . --all
git commit -m "$1"
git push origin master
if [ $? -eq 0 ]
then
    log_info "all done"
else
    log_error "failed"
fi


