Action()
{

	web_add_cookie("w0hC_2132_lastvisit=1581493665; DOMAIN=127.0.0.1");

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
		"Url=static/image/common/px.png", ENDITEM, 
		"Url=static/image/common/newarow.gif", ENDITEM, 
		"Url=static/image/common/pn.png", ENDITEM, 
		"Url=static/image/common/nv_a.png", ENDITEM, 
		"Url=static/image/common/nv.png", ENDITEM, 
		"Url=static/image/common/search.png", ENDITEM, 
		"Url=static/image/common/arrwd.gif", ENDITEM, 
		"Url=static/image/common/qmenu.png", ENDITEM, 
		"Url=static/image/common/titlebg.png", ENDITEM, 
		"Url=static/image/common/pt_item.png", ENDITEM, 
		"Url=static/image/common/chart.png", ENDITEM, 
		"Url=static/image/common/scrolltop.png", ENDITEM, 
		"Url=static/image/common/tip_bottom.png", ENDITEM, 
		LAST);

	lr_think_time(20);

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

	web_add_cookie("w0hC_2132_checkpm=1; DOMAIN=127.0.0.1");

	web_add_cookie("w0hC_2132_noticeTitle=1; DOMAIN=127.0.0.1");

	web_url("forum.php_2", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=static/image/common/user_online.gif", ENDITEM, 
		"Url=static/image/common/notice.gif", ENDITEM, 
		"Url=static/image/common/style_switch.png", ENDITEM, 
		"Url=static/js/common_extra.js?61K", ENDITEM, 
		LAST);

	web_add_cookie("w0hC_2132_smile=1D1; DOMAIN=127.0.0.1");

	lr_think_time(7);

	web_url("selenium", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t4.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=static/image/common/titlebg_sd.png", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/fav.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/feed.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/arw_r.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/arw_l.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/refresh.png", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/atarget.png", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/js/smilies.js?61K", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/editor/editor.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/common/pollsmall.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=data/cache/common_smilies_var.js?61K", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/biggrin.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/smile.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/sad.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/cry.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/shocked.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/tongue.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/funk.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/hug.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/dizzy.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/victory.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/time.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/handshake.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/shutup.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/kiss.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/call.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/sleepy.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/huffy.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/shy.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/titter.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/sweat.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/mad.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/loveliness.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/lol.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		"Url=static/image/smiley/default/curse.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=2", ENDITEM, 
		LAST);

	lr_think_time(8);

	web_url("?BBS", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t5.inf", 
		"Mode=HTML", 
		LAST);

	web_url("loadrunner", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=36", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t6.inf", 
		"Mode=HTML", 
		EXTRARES, 
		"Url=static/image/common/dot.gif", "Referer=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=36", ENDITEM, 
		LAST);

	web_url("?BBS_2", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t7.inf", 
		"Mode=HTML", 
		LAST);

	web_url("android", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=37", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t8.inf", 
		"Mode=HTML", 
		LAST);

	web_url("?BBS_3", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t9.inf", 
		"Mode=HTML", 
		LAST);

	web_url("jmeter", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=38", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t10.inf", 
		"Mode=HTML", 
		LAST);

	web_url("?BBS_4", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t11.inf", 
		"Mode=HTML", 
		LAST);

	web_url("qtp", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php?mod=forumdisplay&fid=39", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"Snapshot=t12.inf", 
		"Mode=HTML", 
		LAST);

	lr_think_time(4);

	web_url("?BBS_5", 
		"URL=http://127.0.0.1:8888/discuz/upload/forum.php", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t13.inf", 
		"Mode=HTML", 
		LAST);

	return 0;
}