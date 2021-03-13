function updateTypeName(select){
    $('label[for="id_typeName"]').html(select.options[select.selectedIndex].text)
}