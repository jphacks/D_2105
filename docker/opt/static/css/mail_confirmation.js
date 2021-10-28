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
<<<<<<< HEAD
    //var mail = mail1.value; //メールフォームの値を取得
    //var mailConfirm = mail2.value; //メール確認用フォームの値を取得
=======
    //var mail = email_1.value; //メールフォームの値を取得
    //var mailConfirm = emailConfirm_1.value; //メール確認用フォームの値を取得
>>>>>>> 209b4b6d1cd18670b12afd079b3a3125a9a6a5df
    var mail = document.getElementById("email_1").value; //メールフォームの値を取得
    var mailConfirm = document.getElementById("email2").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (mail != mailConfirm){
      alert("パスワードと確認用パスワードが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
  };
// -->
</script>
