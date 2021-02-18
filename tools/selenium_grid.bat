cd /d C:\grid
start java -jar selenium-server-standalone-3.141.59.jar -role hub
start java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555 -hub http://localhost:4444/grid/register
start java -jar selenium-server-standalone-3.141.59.jar -role node -port 5556 -hub http://localhost:4444/grid/register
start java -jar selenium-server-standalone-3.141.59.jar -role node -port 5557 -hub http://localhost:4444/grid/register