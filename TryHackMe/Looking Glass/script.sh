#!/usr/bin/bash
echo "If it hang for too long press Enter :)"
echo -en "\n"
BOOL=true
IP=$1
# GET THE BEST MIN AND MAX
arrayname=( 9000 9250 9500 9750 10000 10250 10500 10750 11000 11250 11500 11750 12000 12250 12500 12750 13000 13250 13500 13750 14000 )
for m in "${arrayname[@]}"
do
  	RESULT=$(ssh -q -o StrictHostKeyChecking=no $IP -p $m)
  	if [ $BOOL ]
  	then
	  	if [[ $RESULT == *"Lower"* ]]
		then
		    echo "You need Higher Port"
		    MIN_PORT=$m
		else
		    echo "You need Lower Port"
		    MAX_PORT=$m
		    BOOL=false
		    break
		fi
	fi
done

echo "MIN PORT" + $MIN_PORT
echo "MAX PORT" + $MAX_PORT
BOOL=true
for i in $(seq $MIN_PORT 50 $MAX_PORT)
do
	RESULT=$(ssh -q -o StrictHostKeyChecking=no $IP -p $i)
	echo $i
	if [[ $RESULT == *"Lower"* ]]
	then
	    echo "You need Higher Port"
	else
	    echo "You need Lower Port"
	    MIN_PORT="$(($i-50))"
	    MAX_PORT=$i
	    for j in $(seq $MIN_PORT $MAX_PORT)
	    do
	        RESULT=$(ssh -q -o StrictHostKeyChecking=no $IP -p $j)
	        echo -en "\n"
		if [[ $RESULT == *"Lower"* ]]
		then
		    echo "Port : " $j
		    echo "Result : " $RESULT
		    echo "You need Higher Port"
		else
		    echo "You found the Port!" $j
		    exit 0
		fi
	    done
	    
	fi
done




