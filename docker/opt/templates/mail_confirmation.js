window.MTNetFormDataLayer = window.MTNetFormDataLayer || [];
function MTNetForm() { MTNetFormDataLayer.push(arguments); }
MTNetForm("validator", {
  validator: function(values) {
    var email, confirm, confirmId;
    values.forEach(function(v) {
      if (v.label === "メールアドレス") {
        email = v.value;
      } else if (v.label === "メールアドレス（確認）") {
        confirm = v.value;
        confirmId = v.id;
      }
    });

    if (email && confirm && email !== confirm) {
      return {
        id: confirmId,
        message: "「メールアドレス（確認）」が一致していません。",
      };
    }
  },
});
