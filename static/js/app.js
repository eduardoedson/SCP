function refreshMask () {
  $('.telefone').mask("000000000", {placeholder:"_ ____-____"});
  $('.ddd').mask("00", {placeholder:"__"});
  $('.cpf').mask("00000000000", {placeholder:"___.___.___-__"});
  $('.cep').mask("00000-000", {placeholder:"_____-___"});
  $('.rg').mask("0.000.000", {placeholder:"_.___.___"});
}

$(document).ready(function (){
  refreshMask();
});
