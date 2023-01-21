#!/usr/bin/env bash
start_ts=$(date +%s)

while :
do
    (echo -n > /dev/tcp/$1/$2) > /dev/null
    if [[ $? -eq 0 ]]; then
        break
    fi
    sleep 1
done

end_ts=$(date +%s)

echo "$1:$2 is available after $((end_ts - start_ts)) seconds"
