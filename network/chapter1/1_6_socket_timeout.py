#-*-coding=UTF-8-*-
#首先创建了一个套接字对象，套接字构造方法的第一个参数是地址族，第二个参数是套接字类型。
#调用gettimeout()方法获取套接字超时时间，再调用settimeout()方法修改超时时间。
#传给settimeout()方法的参数可以是秒数（非负浮点数），也可以是None。
#这个方法在处理阻塞式套接字操作时使用。如果把超时时间设为None，则金庸了套接字操作的超时检测。
import socket

def test_socket_timeout():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Default socket timeout: %s" %s.gettimeout()

	s.settimeout(100)
	print "Current socket timeout: %s" %s.gettimeout()

if __name__ == '__main__':
	test_socket_timeout()
