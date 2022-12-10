# WxBotByChatGPT
基于ChatGPT的微信聊天机器人，平台：Windows11、Py#3.6、PcWxClient3.8.0

1.使用说明
    需要手动设置ChatGPT的Authorization以及session_token，配置在config内，由于chatgpt暂时未开放api，所以此工具实现方式是通过模拟网页来向chatgpt进行请求。

    另外由于微信众所周知的原因，以前的wxpy及itchat等库无法使用，所以采用的方案为模拟用户操作pc微信客户端进行消息收发，故在使用此工具时需要打开pc微信并登录。

2.已知问题
    读取对话框的方式为依次轮询，所有好友列表依次读取查看是否有新消息，所有导致读取消息较慢，而且由于chatgpt在不重置task时，所有消息都会有上下文连接，可能存在不同好友在问连贯问题时“串台”。另外因为网络原因chatgpt返回消息时间较长，并且可能存在回答中断问题