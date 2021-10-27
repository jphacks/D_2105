window.MTNetFormDataLayer = window.MTNetFormDataLayer || [];
function mail_check() {
  MTNetFormDataLayer.push(arguments); }
  mail_check("validator", {
  validator: function(values) {
    var email, confirm, confirmId;
    values.forEach(function(v) {
      if (v.label === "email1") {
        email = v.value;
      } else if (v.label === "email2") {
        confirm = v.value;
        confirmId = v.id;
      }
    });

    if (email && confirm && email !== confirm) {
      return {s
        id: confirmId,
        message: "「メールアドレス（確認）」が一致していません。",
      };
    }
  },
});
