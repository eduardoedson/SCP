function refreshMask () {
  $('.telefone').mask("(00) 0 0000-0000", {placeholder:"(__) _ ____-____"});
  $('.ddd').mask("00", {placeholder:"__"});
  $('.cep').mask("00000-000", {placeholder:"_____-___"});
  $('.dateinput').mask('00/00/0000', {placeholder:"__/__/____"});
}

function refreshDatePicker() {
    $.datepicker.setDefaults($.datepicker.regional['pt-BR']);
    $('.dateinput').datepicker();
}

$(document).ready(function (){
  refreshMask();
  refreshDatePicker();
});
