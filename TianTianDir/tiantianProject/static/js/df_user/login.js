/**
 * Created by python on 18-5-9.
 */
$(function () {

    // 用于检测是否合规
    var error_name = false;
    var error_password = false;

	$('#username').blur(function () {
        check_username();
    });

	$('#pwd').blur(function () {
        check_pwd();
    });

	// 点击提交时检查
	$('#login_form').submit(function () {
       check_username();
       check_pwd();
       return error_name==false && error_password==false
    });

	// check
	function check_username() {
        var $username = $('#username');
        var len = $username.val().length;
        if(len<5||len>20) {
            $username.next().html('请输入5-20个字符的用户名');
            $username.next().show();
            error_name = true;
        }
        else {
            // 查询是否有此用户
            $.get('/user/username_exist/?user_name='+$username.val(),function (data) {
               if(data.count==0){
                   $username.next().html('用户名未注册');
                   $username.next().show();
                   error_name = true;
               }
               else {
                   $username.next().hide();
                   error_name = false
               }
            });
        }
    }

    function check_pwd() {
        var $pwd = $('#pwd');
        var len = $pwd.val().length;
        if(len<8||len>20) {
            $pwd.next().html('密码最少8位，最长20位');
            $pwd.next().show();
            error_password = true;
        }
        else {
            $pwd.next().hide();
            error_password = false;
        }
    }


});