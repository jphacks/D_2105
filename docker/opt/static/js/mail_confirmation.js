function CheckEmail_1() {
    //IE対応の為変更
    //var mail = mail1.value; //メールフォームの値を取得
    //var mailConfirm = mail2.value; //メール確認用フォームの値を取得
    var mail = document.getElementById("email1").value; //メールフォームの値を取得
    var mail_confirmation = document.getElementById("email2").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (mail != mail_confirmation){
      alert("メールアドレスが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
 };
