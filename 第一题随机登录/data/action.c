Action()
{

	web_add_cookie("w0hC_2132_sid=ppVhi7; DOMAIN=127.0.0.1");

	web_add_cookie("w0hC_2132_lastvisit=1581491511; DOMAIN=127.0.0.1");

	web_add_cookie("w0hC_2132_lastact=1581496394%09forum.php%09ajax; DOMAIN=127.0.0.1");

	web_add_cookie("w0hC_2132_forum_lastvisit=D_2_1581495132D_36_1581495135D_37_1581495137D_38_1581495139D_39_1581495140; DOMAIN=127.0.0.1");

	web_add_cookie("w0hC_2132_visitedfid=39D38D37D36D2; DOMAIN=127.0.0.1");

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

	lr_think_time(22);

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
		"Name=username", "Value=zhaozhenyu01", ENDITEM, 
		"Name=password", "Value=123456", ENDITEM, 
		"Name=quickforward", "Value=yes", ENDITEM, 
		"Name=handlekey", "Value=ls", ENDITEM, 
		LAST);

	web_add_cookie("w0hC_2132_lastact=1581496526%09forum.php%09; DOMAIN=127.0.0.1");

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