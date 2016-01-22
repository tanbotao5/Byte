var sOldCurrentValue='',sNewCurrentValue='';
var isInit=true;

//计时，以判断数值变化
function test()
{ 	
	if(sOldCurrentValue!=sNewCurrentValue)
	{
		sOldCurrentValue=sNewCurrentValue;
		SendMessage(sNewCurrentValue);
	}
	else
	{
			
	}
} 
window.setInterval("test()",500);

//设置参数按钮
function btnSet()
{
	SendMessage("cam="+$('#camera_id').val());
	SendMessage("mon="+$('#monitor_id').val());
}

//设置预置位
function btnSetSpre()
{
	SendMessage("spre_value="+$('#preset_id').val());
	var spre=document.getElementById("spre_id");
	spre.value="spre="+$('#preset_id').val();
}

//调用预值位
function btnSetVpre()
{
	SendMessage("vpre_value="+$('#preset_id').val());
	var vpre=document.getElementById("spre_id");
	vpre.value="vpre="+$('#preset_id').val();
	
}

function setFocus()
{
	if($('#focus').val()>=0)
	SendMessage("ffocus="+$('#focus').val());
	else
	{
		SendMessage("hfocus="+$('#focus').val());
	}
}


function setUp()
{
	SendMessage("up="+$('#up').val());
}

function setDown()
{
	SendMessage("down="+$('#down').val());
}

function setLeft()
{
	SendMessage("left="+$('#left').val());
}

function setRight()
{
	SendMessage("right="+$('#right').val());
}
	
//向后台发送参数
function SendMessage(sMessage)
{
	//采用Post方式	
	var sUrl="camera.html";	//提交的地址
	$.post(sUrl, 
	   { 	
		  requestContent:sMessage
	   }, 
		function (xml) 
	   {
		//f反馈的结果
			if(sMessage=="cam="+$('#camera_id').val())
	    	{
				var cam_value=document.getElementById("spre_id");
				cam_value.value="cam="+$('#camera_id').val();
	    	}
			else if(sMessage=="mon="+$('#monitor_id').val())
			{
				var mon_value=document.getElementById("spre_id");
				mon_value.value="mon="+$('#monitor_id').val();
	    	}
	   } 
	);
}
	
/*function BodyInit()
{

}*/
/*$(document).ready(function() {
      $("#camera_id").SetValidateSettings({
         FormValidate: {
             Empty: {
                Value: true
             },
             Type: {
                Value: "UInt16",
                Message: "必须是正整数类型"
             },
             MaxValue: {
                 Value: 128,
                 Message: "摄像机编码不能大于128"
             },
             MinValue: {
                 Value: 1,
             Message: "摄像机编码不能小于1"
             }
        },
     });
	 
	 $("#monitor_id").SetValidateSettings({
         FormValidate: {
             Empty: {
                Value: true
             },
             Type: {
                Value: "UInt16",
                Message: "必须是正整数类型"
             },
             MaxValue: {
                 Value: 32,
                 Message: "监视器编码不能大于32"
             },
             MinValue: {
                 Value: 1,
             Message: "监视器编码不能小于1"
             }
        },
     });
	 
	 $("#preset_id").SetValidateSettings({
         FormValidate: {
             Empty: {
                Value: true
             },
             Type: {
                Value: "UInt16",
                Message: "必须是正整数类型"
             },
             MaxValue: {
                 Value: 255,
                 Message: "预置位编码不能大于255"
             },
             MinValue: {
                 Value: 1,
             Message: "预置位编码不能小于1"
             }
        },
     });
});*/

//摄像机编号增加按钮
function addCam_id()
{
	var value= document.getElementById("camera_id").value;
	if(value<128)
	value++;
	else if(value=128)
	alert("已经是最大的编号啦！");
	document.getElementById("camera_id").value=value;
}
//摄像机编号减小按钮
function minusCam_id()
{
	var value= document.getElementById("camera_id").value;
	if(value>1)
	value--;
	else if(value=1)
	alert("已经是最小的编号啦！");
	document.getElementById("camera_id").value=value;
}
//监视器编号增加按钮
function addMon_id()
{
	var value= document.getElementById("monitor_id").value;
	if(value<128)
	value++;
	else if(value=128)
	alert("已经是最大的编号啦！");
	document.getElementById("monitor_id").value=value;
}
//监视器编号减小按钮
function minusMon_id()
{
	var value= document.getElementById("monitor_id").value;
	if(value>1)
	value--;
	else if(value=1)
	alert("已经是最小的编号啦！");
	document.getElementById("monitor_id").value=value;
}
//预置位编号增加按钮
function addPreset_id()
{
	var value= document.getElementById("preset_id").value;
	if(value<128)
	value++;
	else if(value=128)
	alert("已经是最大的编号啦！");
	document.getElementById("preset_id").value=value;
}
//预置位编号减小按钮
function minusPreset_id()
{
	var value= document.getElementById("preset_id").value;
	if(value>1)
	value--;
	else if(value=1)
	alert("已经是最小的编号啦！");
	document.getElementById("preset_id").value=value;
}

