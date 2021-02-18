java -jar selenium-server-standalone-3.141.59.jar -role hub

goto start
-role hub:启动一个Hub服务，作为分布式管理中心，等待Webdriver客户端进行注册和请求
默认接受注册的地址为：http://localhost:4444/grid/register,默认启动端口4444
http://localhost:4444/grid/console,显示"view config"即表示Hub启动成功
B Node可以通过http://A_Npde_ip:4444/grid/console来进行访问
java -jar selenium-server-standalone-3.141.59.jar -role webdriver -bub http://A_Npde_ip:4444/grid/register -Dwebdriver.firefox.driver
="E:\PycharmProject\mbh\drivers\chromedriver.exe" -port 6655 -maxSession5 -browser browserName="firefox",maxInstances=5
role:参数值webdriver表示Node的名字
hub:参数值管理中心URL地址，Node会连接这个地址进行注册
port:参数值表示Node节点服务的端口号为6655，建议使用大于5000的端口号
:start