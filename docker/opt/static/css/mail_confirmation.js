<form onSubmit="return CheckEmail_1()">
  <div>
    <label for="email1">メール:</label>
  </div>
  <div>
    <input type="email" id="email1" required>
  </div>
  <div>
    <label for="email2">メール確認用:</label>
  </div>
  <div>
    <input type="email" id="email2" required>
  </div>
  <p>
    <input type="image" id="submit">
  </p>
</form>

<script language="JavaScript" type="text/javascript">
<!--
  function CheckEmail_1() {
    //IE対応の為変更
    //var mail = mail1.value; //メールフォームの値を取得
    //var mailConfirm = mail2.value; //メール確認用フォームの値を取得
    var mail = document.getElementById("email_1").value; //メールフォームの値を取得
    var mailConfirm = document.getElementById("email2").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (mail != mailConfirm){
      alert("メールアドレスが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
  };
// -->
</script>
