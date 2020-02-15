Action()
{

	web_url("forum.php", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=static/image/common/background.png", ENDITEM, 
		"Url=static/image/common/newarow.gif", ENDITEM, 
		"Url=static/image/common/px.png", ENDITEM, 
		"Url=static/image/common/nv.png", ENDITEM, 
		"Url=static/image/common/nv_a.png", ENDITEM, 
		"Url=static/image/common/search.png", ENDITEM, 
		"Url=static/image/common/pn.png", ENDITEM, 
		"Url=static/image/common/arrwd.gif", ENDITEM, 
		"Url=static/image/common/qmenu.png", ENDITEM, 
		"Url=static/image/common/pt_item.png", ENDITEM, 
		"Url=static/image/common/chart.png", ENDITEM, 
		"Url=static/image/common/titlebg.png", ENDITEM, 
		"Url=static/image/common/scrolltop.png", ENDITEM, 
		"Url=static/image/common/tip_bottom.png", ENDITEM, 
		LAST);



	web_submit_data("member.php", 
		"Action=http://127.0.0.1:8888/discuz/upload/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1", 
		"Method=POST", 
		"TargetFrame=", 
		"RecContentType=text/xml", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t2.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=fastloginfield", "Value=username", ENDITEM, 
		"Name=username", "Value={uname}", ENDITEM, 
		"Name=password", "Value={pwd}", ENDITEM, 
		"Name=quickforward", "Value=yes", ENDITEM, 
		"Name=handlekey", "Value=ls", ENDITEM, 
		LAST);


	web_url("forum.php_2", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=static/image/common/notice.gif", ENDITEM, 
		"Url=static/image/common/user_online.gif", ENDITEM, 
		"Url=static/image/common/style_switch.png", ENDITEM, 
		LAST);

	return 0;
}