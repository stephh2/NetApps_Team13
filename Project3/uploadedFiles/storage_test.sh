#!/bin/bash
IP=$1
PORT=5000

for i in {2..15}
do
    curl  --header "Content-Type: application/json" \
          --request POST \
          --data "{\"Name\": \"n$i\", \"Author\": \"au$i\"}" \
          http://$IP:$PORT/book/add
    echo ""
done

curl  --header "Content-Type: application/json" \
      --request GET \
      http://$IP:$PORT/book/list
echo ""

for i in {2..5}
do
curl  --header "Content-Type: application/json" \
      --request DELETE \
      --data "{\"Name\": \"n$i\", \"Author\": \"au$i\"}" \
      http://$IP:$PORT/book/delete
    echo ""
done

curl  --header "Content-Type: application/json" \
      --request GET \
      http://$IP:$PORT/book/list

echo ""
for i in {2..15}
do
    count=$[$i * 30]
    curl  --header "Content-Type: application/json" \
          --request PUT \
          --data "{\"Name\": \"n$i\", \"Author\": \"au$i\", \"Count\": $count}" \
          http://$IP:$PORT/book/buy
    echo ""
done

curl  --header "Content-Type: application/json" \
      --request GET \
      http://$IP:$PORT/book/list

for i in {2..15}
do
    count=$[$i * 20]
    curl  --header "Content-Type: application/json" \
          --request PUT \
          --data "{\"Name\": \"n$i\", \"Author\": \"au$i\", \"Count\": $count}" \
          http://$IP:$PORT/book/sell
    echo ""
done

curl  --header "Content-Type: application/json" \
      --request GET \
      http://$IP:$PORT/book/list

# echo ""
for i in {2..15}
do
curl  --header "Content-Type: application/json" \
      --request GET \
      http://$IP:$PORT/book/count?Action=COUNT\&Name=n$i\&Author=au$i
echo ""
done
