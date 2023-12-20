#!/bin/bash

RED='\e[31m'
GREEN='\e[32m'
RESET='\e[0m'

declare -i step=1
declare -i hits=0
declare -i misses=0
declare -a numbers=()

while :
    do
    echo -e "Step: ${step}"

    read -p "Please enter number from 0 to 9 (q - quit): " input

    case "${input}" in
        [0-9])
            random_number=$(( RANDOM % 10 ))

            if (( random_number == input )); then
                echo -e "Hit! My number: ${random_number}"
                hits+=1
                answer_color="${GREEN}${random_number}${RESET}"
            else
                echo -e "Miss! My number: ${random_number}"
                misses+=1
                answer_color="${RED}${random_number}${RESET}"
            fi

            numbers=("${numbers[@]}" "${answer_color}")

            hit_percent=$(( hits * 100 / step ))
            miss_percent=$(( 100 - hit_percent ))

            echo -e "Hit: ${hit_percent}%, Miss: ${miss_percent}%"

            if (( "${#numbers[@]}" >= "10")); then
                echo -e "Numbers: ${numbers[@]: -10}"
            else
                count="${#numbers[@]}"
                echo -e "Numbers: ${numbers[@]: -count}"
            fi

            step+=1
        ;;
        q)
            echo "Bye"
            echo "Exit..."
            exit 0
        ;;
        *)
            echo "Not valid input"
            echo "Please repeat"
        ;;
    esac

done
